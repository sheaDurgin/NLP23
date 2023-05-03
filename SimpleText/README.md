# SimpleText Task 1

This repository includes all of the programs and optimal results for my team's (Team Donut Graph, comprised of SJ Franklin and I, Shea Durgin) submission for SimpleText Task 1.

## Table of Contents

- [Installation](#Installation)
- [Text-Files](#Text-Files)
- [Steps-to-Run](#Steps-to-Run)
- [Model-and-Results](#Model-and-Results)
- [Baseline-Results](#Baseline-Results)
- [Our-Results](#Our-Results)
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

You can install them using pip:

    pip install torch tqdm sentence_transformers transformers textstat ranx
    
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
- Run cross_encoder.py with the baseline results file made from the top 2000 jsons and new results file as arguments
- Run combine_scores.py with the new results file as the first argument and the selective baseline as the second argument
- Run evaluation.py with the new results file from combine_scores.py as the argument
- Run get_readability_scores_with_json.py with the new results file (use the combined and normalized version) as the argument

## Model and Results

Our final results come from a combination of the ms-marco-electra-base cross encoder and the intial baseline results from elastic search. The cross encoder does its own reranking of the initial results from elastic search, then that output is directed into a comination program that does a final reranking using a combination of their scores. This results in higher NDCG and MAP scores than both individual results.

## Baseline Results

    NDCG@10: 0.399
    MAP: 0.461
    flesch average: 31.58531276140922
    smog average: 14.593094153731943
    Coleman Liau average: 15.39346035876951

## Our Results

    NDCG@10: 0.464
    MAP: 0.505
    flesch average: 31.585312761409227
    smog average: 14.593094153731947
    Coleman Liau average: 15.39346035876951

## Conclusion

With the use of a cross encoder and a combination algorithm, we were able to improve the baseline results. If we were to continue on the project, we would attempt to fine-tune the cross encoder on the labelled data and implement a way to select more readable passages than just the entire abstract (as our current implementation has no improvement in the readability department). 
