from event import Event
import os
import csv
import corefResolution
from guess_who import getWho
from guess_what import get_who_and_what
from FeatureExtractor import generate_entity_features
from guess_where import getWhere
from guess_when import getWhen
from guess_organization import getOrganization
		

def Extractor(inputFile):
	
    articles = corefResolution.create_title_input(inputFile)
    entities_in_article = generate_entity_features()
    who_and_prob = getWho(inputFile, entities_in_article)
    print(who_and_prob)
    who = []
    for (ent, prb) in who_and_prob:
        who.append(ent)
    who_n_what = get_who_and_what(who)
    print("who_n_what: ", who_n_what)
    when = getWhen(entities_in_article,articles,who_n_what[0])
    print("when: ",when)
    where = getWhere(inputFile, entities_in_article)
    organization = getOrganization(entities_in_article)
    print(organization)
    print('where: ', where)
    for articleID in articles.keys():
    	publicationDate = articles[articleID].date
    	link = articles[articleID].url
    event1 = Event(articleID, who_n_what[0], who_n_what[1], where[0][0], when, "", organization, publicationDate,link)
    return event1
   

writer = csv.DictWriter(open("../data/test_output.csv",'a'), fieldnames = ["articleId","who", "what", "when","where","organization"])
writer.writeheader()
with open("../data/test_all.txt","r") as dataFile:
	article = dataFile.readline()
	while article != "":
		with open("../data/test_one.txt", "w") as articleFile:
			articleFile.write(article)
		os.system("rm -R ../data/articles/title/*.txt")
		os.system("rm -R ../data/articles/text/*.txt")
		event1 = Extractor("../data/test_one.txt")
		row = {"articleId":event1.id, "who":event1.who, "what": event1.what, "when": event1.when, "where": event1.where, "organization": event1.org}
		writer.writerow(row)
		
		
		
		print("here",event1)
		print(event1.link)
		print(event1.org)
		article = dataFile.readline()