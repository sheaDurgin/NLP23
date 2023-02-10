#Lab 3
The notebook file takes in a stackexchange posts xml file and creates wordclouds and zipfs law word distribution diagrams based off common tokens in the most common tags
The two wordcloud sections are the same except step 3 uses a porter stemmer while step 2 doesn't
The last part generates a word distribution diagram to show that they all follow zipfs law

To run the notebook you will need the two accompanying python files as they hold the functions to parse the xml file. Several libraries are also required to be installed before running, these include nltk, wordcloud, matplotlib, and bs4.
