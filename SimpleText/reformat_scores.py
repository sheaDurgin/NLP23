import sys

def main():
    args = sys.argv[1:]
    my_filename1 = args[0]
    my_filename2 = args[1]
    output_file = args[2]

    dic = combine_results(my_filename1, my_filename2)

    print_top_topics_per_id(dic, output_file)

def combine_results(file1, file2):
    combined_scores = {}
    # read and combine scores from file1
    with open(file1, 'r') as f1:
        for line in f1:
            topic_id, _, doc_id, rank, score, _ = line.split()
            score = float(score)
            rank = int(rank)
            combined_score = score / (rank + 60)
            if topic_id in combined_scores:
                if doc_id in combined_scores[topic_id]:
                    combined_scores[topic_id][doc_id] += combined_score
                else:
                    combined_scores[topic_id][doc_id] = combined_score
            else:
                combined_scores[topic_id] = {}
    
    # read and combine scores from file2
    with open(file2, 'r') as f2:
        for line in f2:
            topic_id, _, doc_id, rank, score, _ = line.split()
            score = float(score)
            rank = int(rank)
            combined_score = score / (rank + 60)
            if topic_id in combined_scores:
                if doc_id in combined_scores[topic_id]:
                    combined_scores[topic_id][doc_id] += combined_score
                else:
                    combined_scores[topic_id][doc_id] = combined_score
            else:
                combined_scores[topic_id] = {}
    
    # sort the combined scores dictionary by topic ID in alphabetical order
    sorted_scores = {k: v for k, v in sorted(combined_scores.items(), key=lambda item: item[0])}
    
    # sort the scores for each topic by value
    for topic_id, doc_scores in sorted_scores.items():
        sorted_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
        sorted_scores[topic_id] = sorted_docs

    return sorted_scores

def print_top_topics_per_id(topics_dict, output_file):
    with open(output_file, "w") as f:
        for topic_id, top_docs in topics_dict.items():
            for rank, (doc_id, score) in enumerate(top_docs[:100], start=1):
                f.write(f"{topic_id} Q0 {doc_id} {rank} {score:.6f} COMBINED\n")

main()