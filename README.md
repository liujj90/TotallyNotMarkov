# TotallyNotMarkov
Robot (Markov chain) pretending to be a human pretending to be a robot pretending to be a human.

## About
TotallyNotMarkov scrapes /r/totallynotrobots for title and post texts, builds a dictionary of tri-grams, and passes it through a markov chain to generate random sentences

required packages for this script to work: Python, Pandas, praw, pickle, nltk (for word_tokenize)

### 1. Scrape
getdata.py is a python-based script for scraping reddit (in this case /r/TotallyNotRobots), for post and title information. This process is powered by praw: more info [about praw](https://praw.readthedocs.io/en/stable/ "praw documentation")
The data from this script is stored in csv format using pandas.

### 2. Build dictionary
TotallyNotMarkovChain.py then converts the dataframe (from csv) into a corpus using the df2corpus.preprocess() function
Dictionary is built by passing the corpus into text2dict.chaining()
	- see TotallyNotMarkov.ipynb for example

### 3. Generate random sentences
Generate the sentences by calling MakeChains.generate_sentence() on dictionary
	- see TotallyNotMarkov.ipynb for example

