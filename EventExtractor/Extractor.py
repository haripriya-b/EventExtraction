'''
Created on 23-Mar-2016

@author: haripriya
'''

import json

from article import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def splitToSentences(article):
	 sent_tokenize_list = sent_tokenize(article)
	 return sent_tokenize_list	

def NamedEntityRecognizer(sent_tokenize_list):
	'''
	Set the path to whereever the stanford-ner package is.
	'''
	st = StanfordNERTagger('/home/haripriya/AI/eventExtraction/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/home/haripriya/AI/eventExtraction/stanford-ner-2015-12-09/stanford-ner-3.6.0.jar',
					   encoding='utf-8')
	classified_article = []
	for sent in sent_tokenize_list:
		#tokenized_text = word_tokenize(sent)
		classified_text = st.tag(sent.split())
		for ne in classified_text:
			if ne[1] != 'O':
				classified_article.append(ne)		
	print ('\n')
	return classified_article
	 
def getArticle(fileName):
	line = fileName.readline()
	if line != '':
		data = json.loads(line)
		article = data[0] 
		return Article(article["title"], article["url"], article["text"], article["desciption"], article["articleId"])
	else:
		return ''
	
def main():
	'''
	Set the correct path of the data file
	'''
	dataFile = open("/home/haripriya/workspace/AI/data/test.txt")
	while (True):
		article = getArticle(dataFile)
		if article == '' : break
		text = article.getText()
		sent_list = splitToSentences(text)
		class_article = NamedEntityRecognizer(sent_list)
		print (class_article)
	
main()	
#getArticle("data/test.txt")
