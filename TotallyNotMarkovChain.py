import pickle
import random
import string
from nltk import word_tokenize

class df2corpus(object):
	def __init__(self, data):
		self.data = data
	def preprocess(self):
		df = self.data.fillna('')
		titles = [title for title in df['Title']]
		posts =[post for post in df['Post']]
		newlist = zip(titles,posts)
		corpus = [item for tupl in newlist for item in tupl]
		return corpus

class text2dict(object):
	def __init__(self, words):
		self.words= words
		self.dictionary = {}

	def generate_trigrams(self, word):
		if len(word)< 3:
			return
		for i in range(len(word)-2):
			yield (word[i], word[i+1], word[i+2])
	def chaining(self):
		word = ' '.join(self.words)
		word = word_tokenize(word)
		for word1, word2, word3 in self.generate_trigrams(word):
			key = (word1, word2)
			if key not in self.dictionary: # if combination of word1 and word 2 does not exit, create new dict entry
				self.dictionary[key] = [word3]
			else:
				self.dictionary[key].append(word3) # if they do exit, append word3 to exisiting entry
		return self.dictionary

	def truncate_dict(self):
		self.new_dictionary = {key:value for key, value in self.dictionary.items() if len(value) != 0}
		return self.new_dictionary
	
	def pickle_output(self):
		pickle.dump(self.dictionary, open('chain.p', 'wb'))

class MakeChains(object):
	def __init__(self, dictionary, sent_length):
		self.dictionary = dictionary
		self.sent_length = sent_length
	def generate_sentence(self):
		start = [key for key in self.dictionary.keys()] # list of alll keys in dictionary
		first_gram = random.choice(start) # get random key
		sentence = list(first_gram)
		current_gram= first_gram
		while len(sentence) <= self.sent_length:
		 	try:
		 		next_word = random.choice(self.dictionary[current_gram]) #choose random next word according to dict
		 		if isinstance(next_word,str) == False: # if next word is not a string (end of sent)
		 			return ''.join(' '+ word if not word.startswith("'") and word not in string.punctuation else word for word in sentence) # add space + word in list if not punctuation
		 		sentence.append(next_word) # append next word to sentence
		 		"""
		 		Shift current gram to last 2 words -ie from (word1, word2) to  (word2, word3)

		 		""" 
		 		current_gram = (sentence[-2], sentence[-1]) 
		 	except (IndexError, KeyError) as e: # exceptions handling
		 		sentence.append('.') # force end of sentence
		 		current_gram= random.choice(start) # re-initiate
		return sentence
'''
Note: better exceptions handling required, and ideally a more elegent solution - rather than random initiation of new word triplets
		- potentially solved by larger datasets to curb dead ends
'''