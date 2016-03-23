'''
Created on 23-Mar-2016

@author: haripriya
'''

class Article:
    
    def __init__(self, title, url, text, description, articleId):
        self.title = title
        self.url = url
        self.text = text
        self.description = description
        self.articleId = articleId
        
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

