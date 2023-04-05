# Predicting Duplicate Questions using Natural Language Processing

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

In this project, we explore different NLP techniques to predict duplicate forum questions. We use two different approaches: a fasttext embedding model with cosine similarity, and a feedforward neural network trained on positive samples and negative samples.


## Installation

To install and run this project on your local machine, please follow the steps below:

Download the project files by cloning this repository or downloading the ZIP file and extracting it to a folder on your computer.

Download the Posts.xml file from the following link: https://archive.org/download/stackexchange/law.stackexchange.com.7z/Posts.xml. You may need to extract the file from the compressed 7z file format using a file archiving tool such as 7-Zip.

Open the folder containing the project files in a code editor or IDE such as Visual Studio Code.

Install Jupyter Notebook and its dependencies on your local machine. One way to do this is by installing Anaconda, which includes Jupyter as well as many other commonly used Python packages.

Open the Assignment_Notebook.ipynb file in Jupyter Notebook by typing the following command in your terminal or Anaconda prompt: jupyter notebook NLP_Assignment_2.ipynb

Run each code cell in the notebook file in order to execute the code.

Please note that this project requires Python 3.6 or higher, as well as several Python packages including gensim, scipy, nltk, numpy, torch, and matplotlib.

## Results

The results of the project are presented in the notebook, including accuracy scores and visualizations.

## Conclusion

In conclusion, we have explored different NLP techniques to predict duplicate forum questions. The results show that both the fasttext embedding model and the feedforward neural network have differing effectiveness. With the neural network reigning supreme.
