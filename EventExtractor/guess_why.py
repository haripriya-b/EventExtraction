import re

str = "stepped down to make way for Mr. Y"

def guess(article, event):
    candidateWhy = []
    title_sent = article.sent_in_title()
    sentences = article.sentences()
    for sent in sent_in_title:
        why = findWhy(sent)
        if why != "NONE":
            candidateWhy.append(why)
    for sentence in sentences:
        why = findWhy(sentence)
        if why != "NONE":
            candidateWhy.append(why)

def findWhy(sent, event):
    causalLinks = ['since', 'cause', "because", "hence", "therefore", "why", "result", "reason", "provide", "Due to", "s behind"]
    for link in causalLinks:
        str1 = r'(.*) (' + link + ') (.*)'
        str2 = r'(' + link + ') (.*)' 
        match = re.match( str1 + '|' + str2  , sent , re.I )
        if match:
            print(match.group())
            #return (match.group(2) + " " + match.group(3))
        else:
            print("NONE")
            #return "NONE"
            
findWhy("Because she was wearing heels, she fell.", "")
findWhy("She fell down because she was wearing heels. ", "")