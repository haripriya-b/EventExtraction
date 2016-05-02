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
	
    articles = corefResolution.create_text_input(inputFile)
    entities_in_article = generate_entity_features(articles)
    who = getWho(inputFile, entities_in_article)
    #print(who_and_prob)
    
    if len(who) >0:
     	who_n_what = get_who_and_what(who)
    else:
    	who_n_what = ("", "")
    print("who_n_what: ", who_n_what)
    when = getWhen(entities_in_article,articles,who_n_what[0])
    print("when: ",when)
    where = getWhere(inputFile, entities_in_article)
    organization = getOrganization(entities_in_article)
    print('Organization: ', organization)
    print('where: ', where)
    for articleID in articles.keys():
    	publicationDate = articles[articleID].date
    	link = articles[articleID].url
    event1 = Event(articleID, who_n_what[0], who_n_what[1], where[0][0], when, "", organization, publicationDate,link)
    return event1


def formTree():
	import nltk
	from nltk.corpus import treebank
	def tree_create():
	    sentence = """“Mark Pincus steps down as CEO of Zynga"""
	    sentence1 = treebank.parsed_sents('wsj_0001.mrg')[1]
	    #print(type(sentence1))
	    sent3 = """ [ParentedTree('ROOT', [ParentedTree('FRAG', [ParentedTree('X', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('NP', [ParentedTree('NNS', ['names'])])]), ParentedTree('NP', [ParentedTree('NNP', ['David']), ParentedTree('NNP', ['Lee'])]), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['cfo'])]), ParentedTree(',', [',']), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('NP', [ParentedTree('JJ', ['longtime']), ParentedTree('NN', ['exec']), ParentedTree('NNP', ['Mark']), ParentedTree('NNP', ['Vranesh'])])])])]), ParentedTree('VP', [ParentedTree('VBZ', ['departs']), ParentedTree('NP', [ParentedTree('DT', ['The']), ParentedTree('NN', ['firm'])])])])])] """
	    sentence1 = """(ROOT
  (NP
    (NP (NNP Zynga) (NNS names))
    (NP
      (NP (NNP David) (NNP Lee) (NNP cfo))
      (, ,)
      (PP (IN as)
        (NP (JJ longtime) (JJ exec) (NNP Mark) (NNP Vranesh) (NNS departs))))
    (NP (DT The) (NN firm))))"""
	    sent1 = nltk.tree.Tree.fromstring(sentence1)
	    print(sent1)
	    tokens = nltk.word_tokenize(sentence)
	    tagged = nltk.pos_tag(tokens)
	    entities = nltk.chunk.ne_chunk(tagged)
	    sent1.draw()
	    
	tree_create()
	
	
#formTree()

def parseTree():
	import nltk
	from nltk.corpus import treebank
	sentence = """Zynga Names David Lee CFO, As Longtime Exec Mark Vranesh Departs The Firm"""
	tokens = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(tokens)
	entities = nltk.chunk.ne_chunk(tagged)
	
	result = nltk.parse(sentence)
	#result = nltk.parse.tagged_parse(tagged)
	
#	grammar = "NP: {<DT>?<JJ>*<NN>}"
#	print(tagged)
#	cp = nltk.RegexpParser(grammar)
#	result = cp.parse(tagged)
	print(result)
	result.draw()
	#print(tagged)
	#tagged.draw()
	
#parseTree()



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

