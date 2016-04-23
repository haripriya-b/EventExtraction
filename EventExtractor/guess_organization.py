
def getOrganization(entites_in_article):
    #print(entites_in_article)
    maxOrg= " "
    maxOcc = 0
    maxOccTitle = 0
    minDis = 999
    for articleId in entites_in_article.keys():
        for entity in entites_in_article[articleId].keys():
            if entites_in_article[articleId][entity][3] == 'ORGANIZATION' and int(entites_in_article[articleId][entity][0]) > maxOcc and int(entites_in_article[articleId][entity][1]) > maxOcc:
                maxOcc= int(entites_in_article[articleId][entity][0])
                maxOccTitle= int(entites_in_article[articleId][entity][1])
                maxOrg = entity
                minDis =  entites_in_article[articleId][entity][2]
            elif entites_in_article[articleId][entity][3] == 'ORGANIZATION' and int(entites_in_article[articleId][entity][0]) == maxOcc and entites_in_article[articleId][entity][1] == maxOccTitle: 
                if  entites_in_article[articleId][entity][2] < minDis:
                    maxOcc= int(entites_in_article[articleId][entity][0])
                    maxOrg = entity
                    minDis =  entites_in_article[articleId][entity][2]     
    return maxOrg
    
