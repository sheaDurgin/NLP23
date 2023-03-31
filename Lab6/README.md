# Sentiment Analysis on Tweets about Airlines

In this notebook, we will be performing sentiment analysis on tweets about airlines using a FeedForward neural network. The dataset we will be using is the Twitter US Airline Sentiment dataset from Kaggle.

The dataset contains 14,772 tweets, although we ignore ones with words that aren't in the Word2Vec model. Each tweet is labeled as positive, negative, or neutral. We will be treating this as a classification problem and building a model that can classify each tweet into one of the three sentiment categories.

## Table of Contents

- [Installation](#Installation)
- [Usage](#Usage)
- [Data-Preprocessing](#Data-Preprocessing)
- [Model-Architecture](#Model-Architecture)
- [Results](#Results)
- [Conclusion](#Conclusion)

## Installation

To run this notebook, you will need to install the following libraries:

    torch
    gensim
    numpy
    pandas
    tqdm
    matplotlib

You can install them using pip:

    pip install torch gensim numpy pandas tqdm matplotlib 
    
## Usage

- Download the Twitter US Airline Sentiment dataset from Kaggle.
- Run the notebook cells to preprocess the data, train the model, and evaluate its performance.
- Use the trained model to classify new tweets into sentiment categories.

## Data Preprocessing

First, we will load the dataset and perform some basic preprocessing steps. We will convert all the text to lowercase, remove any URLs, Twitter handles, and any non-alphabetic characters. We will also tokenize the tweets.

## Model Architecture

We will be using a FeedForward neural network to classify the tweets into sentiment categories. The input to the network will be a sequence of tokenized words. The network has 3 hidden layers with dimensions, 128 -> 64 -> 32. The output will be calculated with a combination of ReLU, dropout, and sigmoid. The output has a size of 3, positive, neutral, and negative. It uses the cross-entropy loss function and the Adam optimizer with a learning rate of 0.0003 and weight decay of 0.0001. Finally, the model will be trained for 100 epochs.

## Results

After training the model, we will evaluate its performance on the test set. We are evaluating based on the prediction accuracy.

## Conclusion

In this notebook, we have performed sentiment analysis on tweets about airlines using an FeedForward neural network. We have achieved good accuracy on the test set and demonstrated the effectiveness of FeedForward neural networks in capturing the temporal dependencies between words in a sequence. This model can be used to classify tweets into sentiment categories and help airlines understand customer feedback.
