import pickle
import numpy
import corefResolution
import csv
#import sklearn
def getWho(inputFile):
    file = open("../data/my_who_classifier.pkl", "rb")
    gnb_classifier = pickle.load(file)
    inputFile = "../data/test.txt"
    articles = corefResolution.generate_entities(inputFile, "/home/prerit/ai/project/stanford-corenlp-full-2015-12-09", "text")
    csv_reader = csv.DictReader(open('who_train.csv','r'))
    entities_in_article_text = {}
    for row in csv_reader:
        if row["articleId"] not in entities_in_article_text.keys():
            entities_in_article_text[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
        else:
            entities_in_article_text[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
    print (entities_in_article_text)
        
    dummy = open("who_train.csv","w")
    dummy.close()
        
        
    articles = corefResolution.generate_entities(inputFile, "/home/prerit/ai/project/stanford-corenlp-full-2015-12-09", "title") 
    csv_reader = csv.DictReader(open('who_train.csv','r'))
    entities_in_article_title = {}
    for row in csv_reader:
        if row["articleId"] not in entities_in_article_title.keys():
            entities_in_article_title[row["articleId"]] = {row["who"]: [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]]}
        else:
            entities_in_article_title[row["articleId"]][row["who"]] = [row["num_occur_text"], row["num_occur_title"], row["distribution"], row["entity_type"]] 
    print (entities_in_article_title)
        
    dummy = open("who_train.csv","w")
    dummy.close()
        
        
    '''
    Merge text and title entities
    '''
        
    writer = csv.DictWriter(open('who_train.csv','a'), fieldnames = ["articleId","who", "num_occur_text", "num_occur_title","distribution","entity_type"])
    writer.writeheader()
    
    for id in entities_in_article_title.keys():
        for who in entities_in_article_title[id].keys():
            if who in entities_in_article_text[id].keys():
                    entities_in_article_text[id][who][1] =int(entities_in_article_title[id][who][1]) + 1
            else:
                 entities_in_article_text[id][who] = entities_in_article_title[id][who]
    whoList = []
    del entities_in_article_text["articleId"]
    for id in entities_in_article_text.keys():
        for who in entities_in_article_text[id].keys():
            l = entities_in_article_text[id][who]
            type = l[3]
            l = l[:3]
            if type == 'PERSON':
                l = l + [0,1,0]
            elif type == 'ORGANISATION':
                l = l + [0,0,1]
            elif type == 'LOCATION':
                l = l + [1,0,0]
            else:
                l = l + [0,0,0]    
            
            print("list: " , l)
            
            for i in range(0,len(l)):
                l[i] = float(l[i])
                
            print ("new l: " , l)
            feature = numpy.array(l)
            feature = numpy.reshape(feature,(1,6)) 
            #feature = numpy.asarray(l,dtype = numpy.float(32))
    
            print("feature", feature)
            ans = gnb_classifier.predict(feature)
            prob_ans= gnb_classifier.predict_proba(feature)
            
            print(who,ans[0])
            print("probability")
            print(who,prob_ans[0][1])
            if ans[0]== float(1):
                whoList.append((who,prob_ans[0][1]))
    whoList = sorted(whoList, key = lambda x:x[1],reverse  = True)
    #print(whoList) 
    return whoList                        
'''            
for id in entities_in_article_text.keys():
    for who in entities_in_article_text[id].keys():        
        row = {"articleId":id, "who":who, "num_occur_text": entities_in_article_text[id][who][0], "num_occur_title": entities_in_article_text[id][who][1], "distribution": entities_in_article_text[id][who][2], "entity_type": entities_in_article_text[id][who][3]}
        writer.writerow(row)
'''