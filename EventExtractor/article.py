'''
Created on 23-Mar-2016

@author: haripriya
'''

class Article:
    
    def __init__(self, title, url, text, description, articleId, sentences, sent_in_title, date):
        self.title = title
        self.url = url
        self.text = text
        self.description = description
        self.articleId = articleId
        self.sent_in_title = sent_in_title
        self.sentences = sentences
        self.parseTree = ''
        self.date = date
        
        
    def __hash__(self):
        return hash(self.articleId)
    
    def __eq__(self, other):
        return self.articleId == other.articleId
'''    
    def getTitle(self):
        return self.title
        
    def getURL(self):
        return self.url
        
    def getText(self):
        return self.text
        
    def getDescription(self):
        return self.description
        
    def getArticleId(self):
        return self.articleId
'''
