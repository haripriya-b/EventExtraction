'''
Created on 23-Mar-2016

@author: haripriya
'''

import json
from article import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import conlltags2tree
from nltk.tree import Tree


def splitToSentences(article):
	 sent_tokenize_list = sent_tokenize(article)
	 return sent_tokenize_list	

def NamedEntityRecognizer(sent_tokenize_list):
	'''
	Set the path to whereever the stanford-ner package is.
	'''
	st = StanfordNERTagger('../stanford-ner/english.muc.7class.distsim.crf.ser.gz','../stanford-ner/stanford-ner.jar'	,encoding='utf-8')
	classified_article = []
	for sent in sent_tokenize_list:
		#tokenized_text = word_tokenize(sent)
		classified_text = st.tag(sent.split())
		classified_article = classified_article + classified_text
	#	for ne in classified_text:
	#		if ne[1] != 'O':
	#			classified_article.append(ne)		
#	print ('\n')
	return classified_article


def IOBTagging(ne_tagged_set):
	IOB_tagged = []
	prev_tag = "O"
	for token, tag in ne_tagged_set:
		if tag == "O":
			IOB_tagged.append((token,tag))
			prev_tag = tag
			continue
		if tag != "O" and prev_tag == "O":
			IOB_tagged.append((token, "B-"+tag))
			prev_tag = tag
		elif tag!= "O" and prev_tag == tag:
			IOB_tagged.append((token, "I-"+tag))
			prev_tag = tag
		elif tag != "O" and prev_tag != tag:
			IOB_tagged.append((token, "B-"+tag))
			prev_tag = tag
			
	return IOB_tagged

def getMultiWordEntityTree(ne_tagged_set):
	IOBTagged = IOBTagging(ne_tagged_set)
	sent_tokens, sent_ne_tags = zip(*IOBTagged)
	sent_pos_tags = [pos for token, pos in pos_tag(sent_tokens)]
	
	sent_ne_pos = [(token, pos, ne) for token, pos, ne in zip(sent_tokens, sent_pos_tags, sent_ne_tags)]
	ne_tree = conlltags2tree(sent_ne_pos)
	return ne_tree
			
def PosTagger(sent_tokenize_list):
	pos_tagged_words = []
	#st = StanfordPOSTagger('/home/haripriya/AI/eventExtraction/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz',
	#			'/home/haripriya/AI/eventExtraction/stanford-ner-2015-12-09/stanford-ner-3.6.0.jar',
	#				   encoding='utf-8')
	for sent in sent_tokenize_list:
		pos_tagged_line = pos_tag(sent.split())
		#pos_tagged_line = st.tag(sent.split())
		pos_tagged_words.append(pos_tagged_line)
	return pos_tagged_words

	 
def getArticle(fileName):
	line = fileName.readline()
	if line != '':
		data = json.loads(line)
		article = data[0]
		 
		return Article(preprocessData(article["title"]), article["url"], preprocessData(article["text"]), preprocessData(article["desciption"]), article["articleId"])
	else:
		return ''
	
def preprocessData(text):
	addSpaceTo = [":", ",", ";", "\'"]
	temp = ""
	for ch in addSpaceTo:
		text = text.replace(ch, ' '+ch)
	return text
	
def main():
	'''
	Set the correct path of the data file
	'''
	dataFile = open("../data/test.txt")
	while (True):
		article = getArticle(dataFile)
		if article == '' : break
		text = article.getText()
		sent_list = splitToSentences(text)
		class_article = NamedEntityRecognizer(sent_list)
		print (class_article)
		pos_tagged = PosTagger(sent_list)
		print (pos_tagged)
		ne_tree = getMultiWordEntityTree(class_article)
		print(ne_tree)

main()	
#getArticle("data/test.txt")
