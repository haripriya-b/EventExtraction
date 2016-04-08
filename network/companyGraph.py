import os
from py2neo import Graph
from neo4jrestclient.client import GraphDatabase
path = "file://" + os.getcwd() + "/data"
companyListPath = path + "/companiesNew.csv"
companyTypePath = path + "/companyType.csv"
relationshipPath = path + "/edges.csv"
print(companyListPath)
gdb = GraphDatabase("http://localhost:7474/db/data/",username="neo4j",password="thanks123")

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

print(createCompanies)
print(createCompanyTypes)
print(createRelations)


#results = gdb.query(createCompanies)
#print(results)
resultOfTypes = gdb.query(createCompanyTypes)
print(resultOfTypes)
resultOfRelations = gdb.query(createRelations)
print(resultOfRelations)


