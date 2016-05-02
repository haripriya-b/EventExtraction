import json
import io
import feedparser as fp
from bs4 import BeautifulSoup
from stripogram import html2text
from newspaper import Article
import time
from numpy import append


businessFeeds = []

'''
companies = ['Amazon', 'Android', 'AOL', 'Apple', 'Facebook', 'Google', 'Groupon', 'ipad', 'iphone', 'LinkedIn', 'Microsoft'
                'Samsung', 'Square', 'Twitter', 'Yahoo', 'Zynga']

businessFeeds.append('http://feeds.reuters.com/reuters/INbusinessNews')				
subset = businessFeeds
subset =['http://feeds.reuters.com/reuters/INbusinessNews'] 
subset.append('http://feeds.feedburner.com/TechCrunchIT')
baseURL = 'http://feeds.feedburner.com/TechCrunch/'
for company in companies:
    subset.append(baseURL+company)
print (businessFeeds)
date1 = time.strftime("%x")
date1 = 'date' + date1 +  'a.txt'
'''

businessFeeds.append('http://www.bbc.com/news/technology')
businessFeeds.append('http://edition.cnn.com/tech')
subset = businessFeeds

f = io.open('for_where.txt', 'w')
articleId = 1000;
dict={}
lastModified = {}
for a_link in subset:
	lastModified[a_link] = 0

capture = []
index = 0
for str_link in subset:
	print (str_link)
	d = fp.parse(str_link, modified = lastModified[str_link])	
	print("status " ,d.status)
	if(d.status==200):
		l = [{}]
		print(d.feed.link)
		print(d.feed.title)
		for entry in d.entries:
			l=[{}]
			index = index+1
			L={}
			l[0]["date"]= entry.published
			
			l[0]['title' ]= entry.title
			print("title: " + entry.title)
			print("check3")
			l[0]["url"]=entry.link
			print("url: "+ entry.link)
			article=Article(entry.link)
			article.download()
			article.parse()			
		
			l[0]["articleId"] = articleId
			print("articleId: " + str(articleId))
			l[0]["text"]=article.text
			articleId = articleId+1	
			f.write(unicode(json.dumps(l, ensure_ascii=False)))
			f.write(unicode("\n"))
	elif d.status == 304:
		print('not updated yet')
		print(str_link)
		print(d.status)
	else:
		print(str_link)
		print(d.status)
		
		
print(capture)
