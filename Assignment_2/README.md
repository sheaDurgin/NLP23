# NLP-Assignment-2

This project implemented a Naive Bayes classifier for topic classifcation using forum posts from stack exchange
As well as implementing the OpenAI package to send prompts to the GPT-3 language model and receive its response

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Installation

To install and run this project on your local machine, please follow the steps below:

Download the project files by cloning this repository or downloading the ZIP file and extracting it to a folder on your computer.

Download the Posts.xml file from the following link: https://archive.org/download/stackexchange/law.stackexchange.com.7z/Posts.xml. You may need to extract the file from the compressed 7z file format using a file archiving tool such as 7-Zip.

Open the folder containing the project files in a code editor or IDE such as Visual Studio Code.

Edit the config.ini file to include your OpenAI API key, which should be connected to your OpenAI account.

Install Jupyter Notebook and its dependencies on your local machine. One way to do this is by installing Anaconda, which includes Jupyter as well as many other commonly used Python packages.

Open the NLP_Assignment_2.ipynb file in Jupyter Notebook by typing the following command in your terminal or Anaconda prompt: jupyter notebook NLP_Assignment_2.ipynb

Run each code cell in the notebook file in order to execute the code.

Please note that this project requires Python 3.6 or higher, as well as several Python packages including OpenAI, numpy, sci-kit, and BeautifulSoup.

## Usage

To use this project, follow the installation instructions provided above. Once you have installed the necessary dependencies and packages, you can run the code in Jupyter Notebook by opening the NLP_Assignment_2.ipynb file and executing each code cell in order.

The Post.py file contains the Post class, which is used to represent a post from the Stack Exchange Posts.xml file. The post_parser_record.py file contains the PostParserRecord class, which is used to parse the Posts.xml file and extract the relevant information about each post.

The NLP_Assignment_2.ipynb file contains the main code for the project, including data preprocessing, training a machine learning model, and generating text using OpenAI's GPT-3 language model.

To generate text using the GPT-3 language model, simply provide a prompt as a parameter for the ask_openai function inside a print statement and run the code cell. The generated text will be displayed in the output cell.

## Contact

shea.durgin@maine.edu

