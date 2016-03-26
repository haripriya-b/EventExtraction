import json
import io
import feedparser as fp
from bs4 import BeautifulSoup
from stripogram import html2text
from newspaper import Article
import time
#soup = BeautifulSoup(open("feedsList.html"), 'html.parser')

#feedsList = []
#for a in soup.find_all('a', href=True):
#    feedsList.append(a['href'])

#feedsList = feedsList[13:]
#print(feedsList[100])

businessFeeds = []
#for link in feedsList:
#	if "business" in link.lower() and "business-standard.com" not in link.lower():
#		businessFeeds.append(link)
#		print(link + "\n")
		

companies = ['Amazon', 'Android', 'AOL', 'Apple', 'Facebook', 'Google', 'Groupon', 'ipad', 'iphone', 'LinkedIn', 'Microsoft'
                'Samsung', 'Square', 'Twitter', 'Yahoo', 'Zynga']

businessFeeds.append('http://feeds.reuters.com/reuters/INbusinessNews')				
#subset = feedsList[333:666]
subset = businessFeeds
subset =['http://feeds.reuters.com/reuters/INbusinessNews'] 
subset.append('http://feeds.feedburner.com/TechCrunchIT')
baseURL = 'http://feeds.feedburner.com/TechCrunch/'
for company in companies:
    subset.append(baseURL+company)
#subset = ['http://feeds.feedburner.com/TechCrunchIT']
print businessFeeds
date1 = time.strftime("%x")
date1 = 'date' + date1 +  'a.txt'
f = io.open('march26_final.txt', 'w')
articleId = 1;
dict={}
lastModified = {}
for a_link in subset:
	lastModified[a_link] = 0

capture = []
index = 0
for str_link in subset:
	print str_link
	d = fp.parse(str_link, modified = lastModified[str_link])	
	print("status " ,d.status)
	#print("last modified" + d.modified)
	if(d.status==200):
		l = [{}]
		#print(d.etag)
		#lastModified[str_link] = d.modified
		#print("check1")
		print(d.feed.link)
		#print("check2")
		print(d.feed.title)
		for entry in d.entries:
			l=[{}]
			index = index+1
			L={}
			l[0]["date"]= entry.published
			
			#print("date:" + entry.published)
			l[0]['title' ]= entry.title
			print("title: " + entry.title)
			print("check3")
			l[0]["url"]=entry.link
			print("url: "+ entry.link)
			article=Article(entry.link)
			article.download()
			article.parse()			
			#print("check4")
			##print entry.description.decode.encode('utf-8')						
			
			#text = html2text(entry.description.encode('utf-8'))
			
			##text = h.handle(entry.description.decode('utf-8'))
			#size = text.find("Image")
			#if size > 0:
				#text = text[:size]
			#text = text.strip()	
			#text = text.replace("\n"," ")	
			#l[0]["description"] = text
			
			#print "description is starting"
			#print("description: " + text)
			#print "description is ending"
		
			l[0]["articleId"] = articleId
			print("articleId: " + str(articleId))
			l[0]["text"]=article.text
			articleId = articleId+1	
			#json_data = json.dumps(l)
			f.write(unicode(json.dumps(l, ensure_ascii=False)))
			f.write(unicode("\n"))
			#capture.append(json_data)
			#print(l)						
	elif d.status == 304:
		print('not updated yet')
		print(str_link)
		print(d.status)
	else:
		print(str_link)
		print(d.status)
		
		
print(capture)



#d = fp.parse('http://www.business-standard.com/rss/beyond-business-104.rss')
#d.feed.link
#print(d.feed.description)
#print(d.entries[0].title)
#print(d.entries[0].description)
#print(d.entries[0].link)
#print(d.entries[0].published)
#print(d.entries[0].updated)
#print(d.entries[0].id)
#print(d.bozo)
## date title url text articleId
#yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')
