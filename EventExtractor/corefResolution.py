import json
import os

from article import Article
from stanford_corenlp_pywrapper.sockwrap import CoreNLP
from nltk.tokenize import sent_tokenize

'''
@param: fileName (file pointer)
@return: Article()
Reads from a file containing articles in json format. Extracts the following
details for each article and returns an Article object:
1. articleID
2. title
3. url
4. text
Splits the title and text into lists of sentences and add them to the Article object. 
'''
def getArticle(fileName):
    line = fileName.readline()
    if line != '':
        data = json.loads(line)
        article = data[0]
        sentences = sent_tokenize(preprocessData(article["text"]))
        sent_in_title = sent_tokenize(preprocessData(article["title"]))
        return Article(preprocessData(article["title"]), article["url"], preprocessData(article["text"]), 
                       "", article["articleId"], sentences, sent_in_title, article["date"])
    else:
        return Article(None, None, None, None, None, None, None, None)
    
'''
@param: String
@return: String (the text with a space added in front of: [":", ",", ";", "\'"] )
Add a space in front of the following special characters: [":", ",", ";", "\'"]
'''
def preprocessData(text):
    addSpaceTo = [":", ",", ";", "\'"]
    temp = ""
    for ch in addSpaceTo:
        text = text.replace(ch, ' '+ch)
    return text
    
'''
@param inputFile: file containing articles in JSON format.
@return: a dictionary of articles in the following format:
        {articleId: Article(title, url, text, description, articleId, sentences, sent_in_title)}
For each article in the input file, creates a file ../data/articles/text/{articleId}.txt and writes the 
text of the article into that file.
'''
def create_text_input(inputFile):
    articles = {}
    dataFile = open(inputFile, "r")
    while True:
        article = getArticle(dataFile)
        if article.articleId == None : break
        with open("../data/articles/text/" + str(article.articleId) + ".txt", "w") as articleFile:
            articleFile.write(article.text)
        articles[article.articleId] = article
    return articles


'''
@param inputFile: file containing articles in JSON format.
@return: a dictionary of articles in the following format:
        {articleId: Article(title, url, text, description, articleId, sentences, sent_in_title)}
For each article in the input file, creates a file ../data/articles/title/{articleId}.txt and writes the 
title of the article into that file.

'''
def create_title_input(inputFile):
    articles = create_text_input(inputFile)
    for articleId in articles.keys():
        with open("../data/articles/title/" + str(articles[articleId].articleId) + ".txt", "w") as articleFile:
            articleFile.write(articles[articleId].title)
    return articles

'''
@param inputFilesPath: the name along with path of the input file that contains the articles in 
                       JSON format
@param core_nlp_path: the path for the Stanford core NLP folder
@param part_of_article: the part of the article (title/text) for which the cort coreference resolution 
                        has to be run.
@return: parseTrees.dat: a dictionary with key as the document identifier and value as the parented parse tree
                         for that particular document.
         who_train.csv : a csv file with the following data:
                         * articleId
                         * who: a potential subject of the article
                         * num_occ_text: number of occurrences of the entity in the text including its co-references
                         * num_occ_title: number of occurrences of the entity in the title including its co-references
                         * distribution: ((sum(index of occurrence of the entity))/(number of occurrences of that entity))/(number of word tokens)

The cort co-reference resolution is run on all the .txt files in the specified folder (title/text).


'''
def corefRes(inputFilesPath, core_nlp_path, part_of_article):

    os.system("cort-predict-raw -in " + inputFilesPath + " -model ../data/model-pair-train.obj " +
              "-extractor cort.coreference.approaches.mention_ranking.extract_substructures -perceptron " + 
              "cort.coreference.approaches.mention_ranking.RankingPerceptron -clusterer cort.coreference.clusterer.all_ante " + 
              "-corenlp " + core_nlp_path + " -suffix out > ../data/articles/" + part_of_article + "/parseTrees.dat")  
    
