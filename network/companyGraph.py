import os
import sys
import csv

from py2neo import Graph
from neo4jrestclient.client import GraphDatabase

sys.path.insert(0, '../EventExtractor')
from event import Event


gdb = GraphDatabase("http://localhost:7474/db/data/",username="neo4j",password="thanks123")

def createNetwork():
    path = "file://" + os.getcwd() + "/data"
    companyListPath = path + "/companiesNew.csv"
    companyTypePath = path + "/companyType.csv"
    relationshipPath = path + "/edges.csv"
    compAsso = path + "/competitors.csv"
    print(companyListPath)
    
    
    createCompanies="LOAD CSV WITH HEADERS FROM \"" + companyListPath + """\" AS csvLine
    CREATE (c:Company { id: toInt(csvLine.ID), name: csvLine.Company})
    """
    
    
    createCompanyTypes = "LOAD CSV WITH HEADERS FROM \"" + companyTypePath + """\" AS csvLine
    CREATE (c:Field { id: csvLine.FieldID, sector: csvLine.Field })
    """
    createRelations = "LOAD CSV WITH HEADERS FROM \"" + relationshipPath + """\" AS csvLine
    MATCH (company:Company { name: csvLine.Company}),(field:Field { sector: csvLine.Field})
    CREATE (company)-[:WORKS_IN]->(field)
    """
    
    createCompanyRels = "USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM \"" + compAsso + """\" AS csvLine 
    FIELDTERMINATOR ','
    MERGE ( company1:Company { name: csvLine.Company1 } )
    MERGE ( company2:Company { name: csvLine.Company2 } )
    FOREACH(ignoreMe IN CASE WHEN csvLine.Relation='COMPETITOR' THEN [1] ELSE [] END | 
        MERGE (company1)-[:COMPETITOR]->(company2) )
    FOREACH(ignoreMe IN CASE WHEN csvLine.Relation='ASSOCIATE' THEN [1] ELSE [] END | 
        MERGE (company1)-[:ASSOCIATE]->(company2) )
        """
        
    print(createCompanies)
    print(createCompanyTypes)
    print(createRelations)
    print(createCompanyRels)
    #results = gdb.query(createCompanies)
    #print(results)
    resultOfTypes = gdb.query(createCompanyTypes)
    print(resultOfTypes)
    resultOfCompanies = gdb.query(createCompanies)
    print(resultOfCompanies)
    resultOfRelations = gdb.query(createRelations)
    print(resultOfRelations)
    resultOfCompRels = gdb.query(createCompanyRels)
    print(resultOfCompRels)



def addEvents(events):
    for event in events:
        addToOrg = "MATCH (e:Event),(c:Company) WHERE e.id = " + str(event.id) + " AND c.name = '" + event.org + "' CREATE (e)-[r:ABOUT]->(c) RETURN r"
        
        
        eventLabel = gdb.labels.create("Event")
        eventNode = gdb.node.create(id=event.id, who=event.who, what=event.what, when=event.when, where=event.where, pubData=event.articleDate, url=event.link)
        eventLabel.add(eventNode)
        
        
       # result_add_event = gdb.query(createEvent)
        #print(result_add_event)
        
        result_add_event_rel = gdb.query(addToOrg)
        print(result_add_event_rel)

events = []
createNetwork()
link = """http://feedproxy.google.com/~r/TechCrunch/Zynga/~3/KxqBxfQKC10/"""
link1 = """http://feedproxy.google.com/~r/TechCrunch/Zynga/~3/bB_4k26LpBI/"""
event = Event(1, "Mark Pincus", 'joined as CEO', 'Mountain View', 'today', '', 'Zynga', 'Sun 12 Apr 2015', link)
event1 = Event(2, "Regina E. Dugan", "joins zynga 's board of directors", '', '', '', 'Zynga', 'Sun 12 Apr 2015', link1)

events.append(event)
events.append(event1)
addEvents(events)
