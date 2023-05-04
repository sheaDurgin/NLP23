# SimpleText Task 1

This repository includes all of the programs and optimal results for my team's (Team Donut Graph, comprised of SJ Franklin and I, Shea Durgin) submission for SimpleText Task 1.

## Table of Contents

- [Installation](#Installation)
- [Text Files](#Text-Files)
- [Steps to Run](#Steps-to-Run)
- [Model Details](#Model-Details)
- [Results](#Top-100-Per-Query-Baseline-Results)
- [Conclusion](#Conclusion)

## Installation

To run this code, you will need access to the [dataset](http://simpletext-project.com/2023/clef/) for task 1 of SimpleText CLEF lab, and login details to access their servers. I will be assuming you have access for the rest of the explanation.

The necessary installs for the code are as such

    torch
    tqdm
    sentence_transformers
    transformers
    textstat
    ranx
    markdown

You can install them using pip:

    pip install torch tqdm sentence_transformers transformers textstat ranx markdown
    
Clone the repository all to one folder to properly run. Directories may need to be changed to fit your machine.

## Text Files
- top_100_per_query_baseline.txt -> the top 100 results from elastic search for each query
- selective_baseline.txt -> the maybe top 100 results from elastic search for each query (no work done to get extra results)
- donut_graph_electra_base.txt -> results from cross_encoder.py using top_100_per_query_baseline.txt as argument
- donut_graph_run1_final_results.txt -> results from combine_scores.py using donut_graph_electra_base.txt and selective_baseline.txt

## Steps to Run

- Get the SimpleText dataset from CLEF
- Download the jsons using both download_elastic files
- Read the jsons to two baseline results txt file using readJSON.py on both json directories
- Run normalize.py with the selective baseline results as the first argument and a new filename as the second argument
- Run cross_encoder.py with the baseline results file made from the top 2000 jsons and new result filename as arguments
- Run combine_scores.py with the new results file as the first argument and the normalized selective baseline as the second argument, name of new file as third argument
- Run normalize.py with the new results from combine_scores.py as the first argument and new filename as second argument
- Run evaluation.py with the new results file from normalize.py as the argument
- Run get_readability_scores_with_json.py with the new results file (use the combined and normalized version) as the argument

## Model Details

Our final results come from a combination of the ms-marco-electra-base cross encoder and the two baseline results from elastic search. The cross encoder does its own reranking of the top 100 results from elastic search, then that output is directed into a comination program that does a final reranking using a combination of the cross encoder ranking and the selective baseline results. This results in higher NDCG and MAP scores than any of the individual results.

## Top 100 Per Query Baseline Results

    NDCG@10: 0.366
    MAP: 0.432
    flesch average: 31.585
    smog average: 14.593
    Coleman Liau average: 15.393
    
## Selective Baseline Results (Gives less total results)

    NDCG@10: 0.399
    MAP: 0.461
    flesch average: 31.585
    smog average: 14.593
    Coleman Liau average: 15.393
    
## Electra Reranking Results

    NDCG@10: 0.312
    MAP: 0.314
    flesch average: 31.585
    smog average: 14.593
    Coleman Liau average: 15.393

## Final Combination Results

    NDCG@10: 0.465
    MAP: 0.507
    flesch average: 31.585
    smog average: 14.593
    Coleman Liau average: 15.393

## Conclusion

With the use of a cross encoder and a combination algorithm, we were able to improve the baseline results in both NDCG@10 and MAP scores. If we were to continue on the project, we would attempt to fine-tune the cross encoder on the labelled data and implement a way to select more readable passages than just the entire abstract (as our current implementation has no improvement in the readability department). 
