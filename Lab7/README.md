# Sentiment Analysis on Tweets about Airlines

In this notebook, we will be performing sentiment analysis on tweets about airlines using a Long Short-Term Memory (LSTM) neural network. The dataset we will be using is the Twitter US Airline Sentiment dataset from Kaggle.

The dataset contains 14,772 tweets, although we ignore ones with words that aren't in the Word2Vec model. Each tweet is labeled as positive, negative, or neutral. We will be treating this as a classification problem and building a model that can classify each tweet into one of the three sentiment categories.

## Table of Contents

- [Data Preprocessing](#Data%20Preprocessing)
- [Model Architecture](<#Model Architecture>)
- [Results](#Results)
- [Conclusion](#Conclusion)

## Data%20Preprocessing

First, we will load the dataset and perform some basic preprocessing steps. We will convert all the text to lowercase, remove any URLs, Twitter handles, and any non-alphabetic characters. We will also tokenize the tweets and pad the sequences to a fixed length of 16.

## Model Architecture

We will be using an LSTM neural network to classify the tweets into sentiment categories. The input to the network will be a sequence of tokenized words. We will use an embedding layer to convert each word to a dense vector representation. The output of the embedding layer will be fed into the LSTM layers, which will learn to capture the temporal dependencies between the words in the sequence.

We will use a bidirectional LSTM with one layer and a hidden dimension of 128. The output of the LSTM layer will be fed into a fully connected layer with three output units, one for each sentiment category. We will use a tanh activation function to output the probabilities for each category.

We will use the cross-entropy loss function and the Adam optimizer with a learning rate of 0.004 and weight decay of 0.001. We will train the model for 25 epochs.

## Results

After training the model, we will evaluate its performance on the test set. We are evaluating based on average prediction accuracy over 100 iterations.

## Conclusion

In this notebook, we have performed sentiment analysis on tweets about airlines using an LSTM neural network. We have achieved good accuracy on the test set and demonstrated the effectiveness of LSTMs in capturing the temporal dependencies between words in a sequence. This model can be used to classify tweets into sentiment categories and help airlines understand customer feedback.
