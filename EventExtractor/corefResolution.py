from __future__ import print_function


import subprocess
import json
import os

from article import Article
from stanford_corenlp_pywrapper.sockwrap import CoreNLP
from nltk.tokenize import sent_tokenize


def getArticle(fileName):
    line = fileName.readline()
    if line != '':
        data = json.loads(line)
        article = data[0]
        sentences = sent_tokenize(preprocessData(article["text"]))
        sent_in_title = sent_tokenize(preprocessData(article["title"]))
        return Article(preprocessData(article["title"]), article["url"], preprocessData(article["text"]), 
                       article["articleId"],"", sentences, sent_in_title)
    else:
        return Artilce("","","","",[],[])
    
def preprocessData(text):
    addSpaceTo = [":", ",", ";", "\'"]
    temp = ""
    for ch in addSpaceTo:
        text = text.replace(ch, ' '+ch)
    return text
    
def create_text_input(inputFile):
    articles = {}
    dataFile = open(inputFile)
    while True:
        article = getArticle(dataFile)
        if article.articleId == '' : break
        with open("../data/articles/text/" + str(article.getArticleId()) + ".txt", "w") as articleFile:
            articleFile.write(article.getText())
        articles[article.articleId()] = article
        #articles[article.articleId()] = {"articleId":article.getArticleId, "title": article.title(), "url": article.url(),
        #                                 "text": article.text(), "sent_in_title": article.sent_in_title(), }
    return articles

def create_title_input(inputFile):
    articles = create_text_input(inputFile)
    for article in articles:
        with open("../data/articles/title/" + str(article.getArticleId()) + ".txt", "w") as articleFile:
            articleFile.write(article.getTitle())
            
    return articles

def corefRes(inputFilesPath, core_nlp_path, part_of_article):

    os.system("cort-predict-raw -in " + inputFilesPath + " -model ../data/model-pair-train.obj " +
              "-extractor cort.coreference.approaches.mention_ranking.extract_substructures -perceptron " + 
              "cort.coreference.approaches.mention_ranking.RankingPerceptron -clusterer cort.coreference.clusterer.all_ante " + 
              "-corenlp " + core_nlp_path + " -suffix out > ../data/articles/" + part_of_article + "/requiredData.dat")

'''
    subprocess.call([
            "cort-predict-raw",
            "-in", inputFilesPath,
            "-model", "../data/model-pair-train.obj",
            "-corenlp", core_nlp_path,
            "-extractor", "cort.coreference.approaches.mention_ranking.extract_substructures",
            "-perceptron", "cort.coreference.approaches.mention_ranking.RankingPerceptron",
            "-clusterer", "cort.coreference.clusterer.all_ante"])
'''
    
    
    
def generate_entities(inputFile, core_nlp_path, part_of_article):    
    articles = create_title_input(inputFile) #"../data/test.txt")
    corefRes("../data/articles/" + part_of_article + "/*.txt", core_nlp_path, part_of_article) #"/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09")
    return articles