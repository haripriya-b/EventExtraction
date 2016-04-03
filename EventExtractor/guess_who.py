import pickle
import numpy
import corefResolution
import csv

def get_entities_in_articles():
    inputFile = "../data/test.txt"
    articles = corefResolution.generate_entities(inputFile, "/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09", "text")
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
        
        
    articles = corefResolution.generate_entities(inputFile, "/home/haripriya/AI/eventExtraction/stanford-corenlp-full-2015-12-09", "title") 
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
    
    del entities_in_article_text["articleId"]
    return entities_in_article_text
        
    
def get_candidate_whos():
    candidate_whos = []
    file = open("../data/my_who_classifier.pkl", "rb")
    gnb_classifier = pickle.load(file)
    entities_in_article = get_entities_in_articles()    
    for id in entities_in_article.keys():
        for who in entities_in_article[id].keys():
            l = entities_in_article[id][who]
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
            
            #print("list: " , l)
            
            for i in range(0,len(l)):
                l[i] = float(l[i])
                
           # print ("new l: " , l)
            feature = numpy.array(l)
            feature = numpy.reshape(feature,(1,6))
            #feature = numpy.ScalarType.transform(feature)
            #feature = numpy.asarray(l,dtype = numpy.float(32))
    
            #print("feature", feature)
            ans = gnb_classifier.predict(feature)
            print(who,ans)
            if ans[0] == 1.:
                candidate_whos.append(who)
              #  print(who)
                
    return (candidate_whos)

get_candidate_whos()

'''            
for id in entities_in_article_text.keys():
    for who in entities_in_article_text[id].keys():        
        row = {"articleId":id, "who":who, "num_occur_text": entities_in_article_text[id][who][0], "num_occur_title": entities_in_article_text[id][who][1], "distribution": entities_in_article_text[id][who][2], "entity_type": entities_in_article_text[id][who][3]}
        writer.writerow(row)
'''