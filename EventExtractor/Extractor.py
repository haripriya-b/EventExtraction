'''
Created on 23-Mar-2016

@author: haripriya
'''
from __future__ import division
import json
import csv
import re
from article import Article
from nltk.tag import StanfordNERTagger
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
import nltk
import corefResolution

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
		 
		return Article(preprocessData(article["title"]), article["url"], preprocessData(article["text"]), '''preprocessData(article["desciption"]),'''" ", article["articleId"])
	else:
		return ''
def mean_occurence(a_str, sub):
	length = len(a_str)
	count = 0
	start = 0
	final = 0
	while(True):
		temp= a_str.find(sub)
		if temp == -1:
			if(count >0):
				final = start/count
				return final/length
			else:
				return 0
		else:
			count+=1
			start = start + temp
			a_str = a_str[start+len(sub):]
			
#     p = [m.start() for m in re.finditer(sub, a_str)]
#     if len(p)>0:	
#     	return sum(p)/len(p)
#     else: 
#     	return 0
        	
def preprocessData(text):
	addSpaceTo = [":", ",", ";", "\'"]
	temp = ""
	for ch in addSpaceTo:
		text = text.replace(ch, ' '+ch)
	return text

def parseTree(tree):
	count = {}
	tupelist = []
	entities= ['LOCATION','PERSON','ORGANIZATION','DATE','MONEY']
	for entity in entities:
		count[entity] = {}
		
	for child in tree:
			if (type(child)==nltk.tree.Tree):
				if child.label() in entities:
					s = ""
					for c in child:
						s=s+" " + c[0]
					tupelist.append((child.label(),s))
					if s in count[child.label()].keys():
						
						count[child.label()][s] +=1 
					else:
						
						count[child.label()][s] =1
			#else:
				
	#print(tupelist)
	return count,tupelist			
				
				#print child[1]
				
def main(inputFile):
	articles = corefResolution.generate_entities(inputFile, "/home/prerit/ai/project/stanford-corenlp-full-2015-12-09", "text")
	csv_reader = csv.DictReader(open('who_train.csv','r'))
	entities_in_article_text = {}
	for row in csv_reader:
		if row["articleId"] not in entities_in_article_text.keys():
			entities_in_article_text[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
		else:
			entities_in_article_text[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
	print (entities_in_article_text)
	
	dummy = open("who_train.csv","w")
	dummy.close()
	
	
	articles = corefResolution.generate_entities(inputFile, "/home/prerit/ai/project/stanford-corenlp-full-2015-12-09", "title") 
	csv_reader = csv.DictReader(open('who_train.csv','r'))
	entities_in_article_title = {}
	for row in csv_reader:
		if row["articleId"] not in entities_in_article_title.keys():
			entities_in_article_title[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
		else:
			entities_in_article_title[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
	print (entities_in_article_title)
	
	dummy = open("who_train.csv","w")
	dummy.close()
	
	
	'''
	Merge text and title entities
	'''
	
	writer = csv.DictWriter(open('who_train.csv','a'), fieldnames = ["articleId","who", "num_occur_text", "num_occur_title","distribution","entity_type"])
	writer.writeheader()
	where_writer = csv.DictWriter(open('where_train.csv','a'), fieldnames = ["articleId","who", "num_occur_text", "num_occur_title","distribution","entity_type"])
	where_writer.writeheader()

	for id in entities_in_article_title.keys():
		for who in entities_in_article_title[id].keys():
			if who in entities_in_article_text[id].keys():
					entities_in_article_text[id][who][1] =int(entities_in_article_title[id][who][1]) + 1
			else:
				 entities_in_article_text[id][who] = entities_in_article_title[id][who]
			
	for id in entities_in_article_text.keys():
		for who in entities_in_article_text[id].keys():		
			row = {"articleId":id, "who":who, "num_occur_text": entities_in_article_text[id][who][0], "num_occur_title": entities_in_article_text[id][who][1], "distribution": entities_in_article_text[id][who][2], "entity_type": entities_in_article_text[id][who][3]}
			writer.writerow(row)
        
	
	
	'''
	
	for article in articles:
		title = article.getTitle()
		title_sent_list = splitToSentences(title)
		pos_tagged_title = PosTagger(title_sent_list)			
		title_class_article = NamedEntityRecognizer(title_sent_list)
		print(title_class_article)
		
		title_ne_tree = getMultiWordEntityTree(title_class_article)
		print(title_ne_tree)
		title_ne_tree.draw()
		'''
		
main("../data/test.txt")				
#main("../data/march26_final.txt")

"""		
def main():
	'''
	Set the correct path of the data file
	'''
	dataFile = open("../data/march26_final.txt")
	who_train = open('who_train.csv','w')
	writer = csv.DictWriter(open('who_train.csv','w'), fieldnames = ["articleId","who", "num_occur_text", "num_occur_title","distribution","entity_type"])
	writer.writeheader()
	while (True):
		article = getArticle(dataFile)
		if article == '' : break
		print("articleId ", article.getArticleId())
		text = article.getText()
		title = article.getTitle()
		print(title)
		
		title_sent_list = splitToSentences(title)
		#print title_sent_list
		sent_list = splitToSentences(text)
		title_class_article = NamedEntityRecognizer(title_sent_list)
		class_article = NamedEntityRecognizer(sent_list)
		print (class_article)
		pos_tagged = PosTagger(sent_list)
		pos_tagged_title = PosTagger(title_sent_list)
		print (pos_tagged)
		#print(pos_tagged_title)
		ne_tree = getMultiWordEntityTree(class_article)
		title_ne_tree = getMultiWordEntityTree(title_class_article)
		#print(ne_tree)
		#print "tree for title"
		#print(ne_tree)
		#ne_tree.draw()	
		print(type(ne_tree))
		#print len(title_ne_tree)
		text_count,tuplelist = parseTree(ne_tree)
		title_count,title_tuples = parseTree(title_ne_tree)
		print(text_count)
		print(tuplelist)
		for key in ['PERSON','LOCATION','ORGANIZATION']:
			#row={}
			for akey in text_count[key].keys():
				row = {}
				row["articleId"]=article.getArticleId()
				row["who"]=akey
				row["num_occur_text"] = text_count[key][akey]
				row["entity_type"] = key
				row["distribution"] = mean_occurence(text,akey)
				print("mean occurence",mean_occurence(text,akey))
				if akey in title_count[key].keys():
					row["num_occur_title"] = title_count[key][akey]
				else:
					row["num_occur_title"] = 0	
				writer.writerow(row)
				print(row)
						
	#print i
	#print title_ne_tree.label()
	#labelCount = {}
	
	#print labelCount
main()	
#getArticle("data/test.txt")
"""