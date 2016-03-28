from __future__ import print_function


import subprocess
import json
import os

from article import Article
from stanford_corenlp_pywrapper.sockwrap import CoreNLP


def getArticle(fileName):
    line = fileName.readline()
    if line != '':
        data = json.loads(line)
        article = data[0]
         
        return Article(preprocessData(article["title"]), article["url"], preprocessData(article["text"]), '''preprocessData(article["desciption"]),'''" ", article["articleId"])
    else:
        return ''
    
def preprocessData(text):
    addSpaceTo = [":", ",", ";", "\'"]
    temp = ""
    for ch in addSpaceTo:
        text = text.replace(ch, ' '+ch)
    return text
    
def create_text_input(inputFile):
    articles = []
    dataFile = open(inputFile)
    while True:
        article = getArticle(dataFile)
        if article == '' : break
        with open("../data/articles/text/" + str(article.getArticleId()) + ".txt", "w") as articleFile:
            articleFile.write(article.getText())
        articles.append(article)
    return articles

def create_title_input(inputFile):
    articles = create_text_input(inputFile)
    for article in articles:
        with open("../data/articles/title/" + str(article.getArticleId()) + ".txt", "w") as articleFile:
            articleFile.write(article.getTitle())
            
    return articles

def corefRes(inputFilesPath, core_nlp_path):

    os.system("cort-predict-raw -in " + inputFilesPath + " -model ../data/model-pair-train.obj -extractor cort.coreference.approaches.mention_ranking.extract_substructures -perceptron cort.coreference.approaches.mention_ranking.RankingPerceptron -clusterer cort.coreference.clusterer.all_ante -corenlp " + core_nlp_path + " -suffix out")

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
    corefRes("../data/articles/" + part_of_article + "/*.txt", core_nlp_path) #"/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09")
    return articles