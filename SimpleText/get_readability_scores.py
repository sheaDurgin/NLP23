import json
from readability import Readability
import requests
import sys


############# SMOG
# The SMOG Readability Formula (Simple Measure of Gobbledygook) is a popular method to use on health literacy materials.

############# FLESCH
# The U.S. Department of Defense uses the Reading Ease test as the standard test of readability for
# its documents and forms. Florida requires that life insurance policies have
# a Flesch Reading Ease score of 45 or greater.

############# Coleman Liau
# The Coleman-Liau Formula usually gives a lower grade value than any of the Kincaid,
# ARI and Flesch values when applied to technical documents.

def calculate_readability(lst_doc_id):
    # this method takes in a list of document ids and returns three readability scores based on their abstract
    dic_readability_scores = {}
    user, password = 'inex', 'qatc2011'
    pre_qid = ""
    counter = 1
    base_url = "https://guacamole.univ-avignon.fr/dblp1/_search?q=_id:"
    for doc_id in lst_doc_id:
        url = base_url + str(doc_id)
        result = requests.get(url, auth=(user, password)).content.decode("utf-8")
        obj = json.loads(result)
        abstract = obj['hits']['hits'][0]['_source']['abstract']
        r = Readability(abstract)
        # After installing the library, you have to go to each of the following libraries (ctrl+click)
        # and remove the if condition that raises an exception for not short length
        dic_readability_scores[doc_id] = {"flesch": r.flesch().score, "smog": r.smog().score, "Coleman Liau":r.coleman_liau().score}
    return dic_readability_scores

def json_abstracts(doc_ids, topic):
    json_path = ""
    # find the JSON file that contains the topic string in its filename
    for filename in os.listdir("jsons/"):
        if topic in filename:
            json_path = os.path.join("jsons/", filename)
            break
    else:
        raise ValueError(f"No JSON file found for topic '{topic}'")
    with open(json_path) as f:
        data = json.load(f)
        abstracts = {}
        for doc_id in doc_ids:
            for hit in data['hits']['hits']:
                if hit['_id'] == doc_id:
                    abstracts[doc_id] = hit['_source']['abstract']
                    break
            else:
                # if doc_id is not found in the JSON file, set abstract to None
                abstracts[doc_id] = None
        return abstracts

def read_trec_file(trec_file_path):
    result_dict = {}
    with open(trec_file_path, 'r') as f:
        for line in f.readlines():
            topic_id, _, doc_id, rank, score, _ = line.strip().split()
            if topic_id not in result_dict:
                result_dict[topic_id] = []
            result_dict[topic_id].append(doc_id)
    return result_dict

def fast_readability(filename):
    dic_readability_scores = {}
    file_dict = read_trec_file(filename)
    for topic in file_dict:
        doc_ids = [doc_id for doc_id in file_dict[topic]]
        abstract_dict = json_abstracts(doc_ids, topic)
        for doc_id in abstract_dict:
            dic_readability_scores[doc_id] = {"flesch": r.flesch().score, "smog": r.smog().score, "Coleman Liau":r.coleman_liau().score}
    return dic_readability_scores

args = sys.argv[1:]

filename = args[0]

readability_dic = fast_readability(filename)

for doc_id in readability_dic:
    print(readability_dic[doc_id])