'''
Created on 23-Mar-2016

@author: haripriya
'''

import csv
import corefResolution

'''
Creates a file with articleID, all possible entities, their types, number of occurrences in title and text
and their distribution.

 
'''
def generate_entity_features():
	corefResolution.corefRes("../data/articles/text/*.txt", "/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09", "text")
	csv_reader = csv.DictReader(open('train.csv','r'))
	entities_in_article_text = {}
	for row in csv_reader:
		if row["articleId"] not in entities_in_article_text.keys():
			entities_in_article_text[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
		else:
			entities_in_article_text[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
	#print (entities_in_article_text)
	
	dummy = open("train.csv","w")
	dummy.close()
	
	
	corefResolution.corefRes("../data/articles/title/*.txt", "/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09", "title") 
	csv_reader = csv.DictReader(open('train.csv','r'))
	entities_in_article_title = {}
	for row in csv_reader:
		if row["articleId"] not in entities_in_article_title.keys():
			entities_in_article_title[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
		else:
			entities_in_article_title[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
	#print (entities_in_article_title)
	
	dummy = open("train.csv","w")
	dummy.close()
	
	
	'''
	Merge text and title entities
	'''
	for id in entities_in_article_title.keys():
		for who in entities_in_article_title[id].keys():
			if who in entities_in_article_text[id].keys():
					entities_in_article_text[id][who][1] =int(entities_in_article_title[id][who][1]) + 1
			else:
				 entities_in_article_text[id][who] = entities_in_article_title[id][who]
	return entities_in_article_text

def write_features_to_file(outputFile):
	entities_in_article = generate_entity_features()		
	
	writer = csv.DictWriter(open(outputFile,'a'), fieldnames = ["articleId","who", "num_occur_text", "num_occur_title","distribution","entity_type"])
	writer.writeheader()
	
	for id in entities_in_article.keys():
		for who in entities_in_article[id].keys():		
			row = {"articleId":id, "who":who, "num_occur_text": entities_in_article[id][who][0], "num_occur_title": entities_in_article[id][who][1], "distribution": entities_in_article[id][who][2], "entity_type": entities_in_article[id][who][3]}
			writer.writerow(row)
		
#write_features_to_file("../data/test.txt", "../data/train_data.csv")				
