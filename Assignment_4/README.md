# Predicting Duplicate Questions using BERT

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

In this project, we explore how accurate the BERT model, which is pre-trained on quora duplicate questions, is at predicting duplicate stack exchange law forum questions. We use a few different approaches: no fine-tuning, fine-tuning using Multi Negative Ranking Loss and Constrative Loss with a 90/10 training and test split, then testing just the 10% test set on the first model with no fine-tuning. At the end we also tried replacing the quora BERT model with LEGAL-BERT to see the affect. 

## Installation

To install and run this project on your local machine, please follow the steps below:

Download the project files by cloning this repository or downloading the ZIP file and extracting it to a folder on your computer.

Download the Posts.xml file from the following link: https://archive.org/download/stackexchange/law.stackexchange.com.7z/Posts.xml. You may need to extract the file from the compressed 7z file format using a file archiving tool such as 7-Zip.

Open the folder containing the project files in a code editor or IDE such as Visual Studio Code.

Install Jupyter Notebook and its dependencies on your local machine. One way to do this is by installing Anaconda, which includes Jupyter as well as many other commonly used Python packages.

Open the Assignment_Notebook.ipynb file in Jupyter Notebook by typing the following command in your terminal or Anaconda prompt: jupyter notebook Assignment_4_Notebook.ipynb

Run each code cell in the notebook file in order to execute the code.

To run this notebook, you will need to install the following libraries:

    torch
    numpy
    sentence_transformers
    
You can install them using pip:

    pip install torch numpy sentence_transformers

## Results

The results of the project are presented in the notebook, including MRR and p@1 scores.

## Conclusion

In conclusion, we have explored different NLP techniques to predict duplicate forum questions. The results show that fine-tuning a pre-trained BERT model may not provide much to any benefit to your MRR and/or p@1 score. Also, it showed that a pre-trained model on the exact task you are doing may be better than a pre-trained model trained on a more matching corpus.
