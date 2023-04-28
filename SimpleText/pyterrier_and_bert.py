import string
import pyterrier as pt
import json
from Preprocessing_tools import *
import pandas as pd
from collections import Counter
from sentence_transformers import util
import re
import torch
import sys

pt.init(boot_packages=["com.github.terrierteam:terrier-prf:-SNAPSHOT"])
def read_json(file_path):
    item_list = []
    with open(file_path, encoding="utf-8") as json_file:
        for item in [json.loads(line) for line in json_file.readlines()]:
            source_dic = item['_source']
            docno = item['_id']
            title = source_dic['title']
            abstract = source_dic['abstract']
            item_list.append({'docno': str(docno), 'title': title, 'body': abstract})
    return item_list


def indexing(item_list, index_name):
    iter_indexer = pt.IterDictIndexer(index_name, meta={'docno': 20, 'title': 10000, 'body': 20000}, overwrite=True)
    RETRIEVAL_FIELDS = ['body', 'title']
    index = iter_indexer.index(item_list, fields=RETRIEVAL_FIELDS)
    return index


def generator(file_path):
    with open(file_path, encoding="utf-8") as json_file:
        for line in json_file.readlines():
            item = json.loads(line)
            source_dic = item['_source']
            docno = item['_id']
            title = source_dic['title']
            abstract = source_dic['abstract']
            yield {'docno': str(docno), 'title': title, 'body': abstract}


def new_indexing(file_path, index_name):
    iter_indexer = pt.IterDictIndexer(index_name, meta={'docno': 20, 'title': 10000, 'body': 20000}, overwrite=True)
    RETRIEVAL_FIELDS = ['body', 'title']
    index = iter_indexer.index(generator(file_path), fields=RETRIEVAL_FIELDS)
    return index

table = str.maketrans(dict.fromkeys(string.punctuation))

def get_queries(topic_dic):
    lst_queries = []
    for topic in topic_dic:
        query_id = topic.replace("_", ".")
        query, topic_text = topic_dic[topic]
        query = query + " " + topic_text
        query = query.replace("?", " ")
        query = query.replace("\"", " ")
        query = query.replace(":", " ")
        query = query.replace("\'", " ")
        query = query.replace("-", " ")
        query = query.replace("/", " ")
        query = query.translate(table)
        lst_queries.append([str(query_id), query])
    return lst_queries


def retrieval(index, lst_queries, result_file):
    # tf_idf = pt.BatchRetrieve(index, num_results=100, wmodel="TF_IDF")
    #bm25 = pt.BatchRetrieve(index, num_results=100, wmodel="PL2")
    # pipeline = (tf_idf % 100) >> bm25
    # Retrieval models
    bm25 = pt.BatchRetrieve(index, wmodel="BM25", normalize=True)
    dph = pt.BatchRetrieve(index, wmodel="DPH")

    # Query expansion techniques
    bo1 = pt.rewrite.Bo1QueryExpansion(index)
    rm3 = pt.rewrite.RM3(index)


    # Create pipelines
    bo1_pipeline = (bm25 % 3000) >> bo1 >> (dph % 500)
    rm3_pipeline = (bm25 % 3000) >> rm3 >> (dph % 500)

    queries = pd.DataFrame(lst_queries, columns=['qid', 'query'])
    #result = bm25.transform(queries)
    result = rm3_pipeline.transform(queries)

    # Normalize scores by maximum score per topic
    result["max_score"] = result.groupby("qid")["score"].transform("max")
    result["score"] = result["score"] / result["max_score"]
    result.drop(columns=["max_score"], inplace=True)

    pt.io.write_results(result, result_file, format='trec')
    print(result)


from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def bert_ranking(topic_dic, initial_retrieval, model):
    bert_ranked_docs = []
    max_scores = {}  # dictionary to store the max score for each topic_id

    for topic in topic_dic:
        query, topic_text = topic_dic[topic]
        query_embedding = model.encode(query + " " + topic_text, convert_to_tensor=True)
        initial_ret_topic = initial_retrieval[topic]

        corpus = []
        index_to_question_id = {}
        idx = 0

        for doc_id in initial_ret_topic:
            title, abstract = initial_ret_topic[doc_id]
            corpus.append(abstract)
            index_to_question_id[idx] = doc_id
            idx += 1

        corpus_embeddings = model.encode(corpus, convert_to_tensor=True, show_progress_bar=True)
        cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
        top_results = torch.topk(cos_scores, k=500)

        ranked_docs = [(index_to_question_id[int(idx)], score.item()) for score, idx in zip(top_results[0], top_results[1])]
        bert_ranked_docs.append((topic.replace("_", "."), ranked_docs))

        # Calculate max score for this topic and store in the dictionary
        max_scores[topic.replace("_", ".")] = max(score for doc_id, score in ranked_docs)

    # Normalize scores for each topic by the corresponding max score
    for i in range(len(bert_ranked_docs)):
        topic_id, ranked_docs = bert_ranked_docs[i]
        max_score = max_scores[topic_id]
        bert_ranked_docs[i] = (topic_id, [(doc_id, score / max_score) for doc_id, score in ranked_docs])

    return bert_ranked_docs

def write_bert_rankings(rankings, file_path):
    with open(file_path, "w") as f:
        for query_id, docs in rankings:
            for rank, (doc_id, score) in enumerate(docs, start=1):
                f.write(f"{query_id} Q0 {doc_id} {rank} {score} bert_model\n")


do_indexing = False
index_name = "./simple_text_idx"

if do_indexing:
    print("reading the json file")
    # item_list = read_json("dblp1.json")
    json_file_path = "dblp1.json"
    print("indexing the collection")
    index = new_indexing(json_file_path, index_name)
else:
    index = pt.IndexFactory.of(index_name)

args = sys.argv[1:]
run_bert = False
run_pyterrier = False

if args[0] == "bert":
    run_bert = True
    if args[1] == "pyterrier":
        run_pyterrier = True
elif args[0] == "pyterrier":
    run_pyterrier = True
    if args[1] == "bert":
        run_bert = True

if run_bert:
    print("reading json")
    initial_retrieval = read_all_jsons(target_dir="SimpleText/Top-2000_InitialQuery/")
    topic_dic = read_topic_file("SP12023topics.csv")
    from sentence_transformers import SentenceTransformer

    # Replace this with the model you want to use
    model_name = 'sentence-transformers/all-mpnet-base-v2'
    #model_name = 'sentence-transformers/all-distilroberta-v1'
    model = SentenceTransformer(model_name, device='cuda')

    print("bert ranking")
    bert_ranked_docs = bert_ranking(topic_dic, initial_retrieval, model)

    print("writing bert ranking file")
    write_bert_rankings(bert_ranked_docs, "mpnet_rank_nbt.txt")

if run_pyterrier:
    print("reading queries")
    topic_dic = read_topic_file("SP12023topics.csv")
    query_list = get_queries(topic_dic)

    print("pyterrier retrieval")
    retrieval(index, query_list, "pt_rank_nbt.txt")

