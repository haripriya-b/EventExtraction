from event import Event
import corefResolution
from guess_who import getWho
from guess_what import get_who_and_what
from FeatureExtractor import generate_entity_features
from guess_where import getWhere
from guess_when import getWhen

		

def Extractor(inputFile):
	
    articles = corefResolution.create_title_input(inputFile)
    entities_in_article = generate_entity_features()
    who_and_prob = getWho(inputFile, entities_in_article)
    print(who_and_prob)
    who = []
    for (ent, prb) in who_and_prob:
        who.append(ent)
    who_n_what = get_who_and_what(who)
    print("who_n_what: ", who_n_what)
    when = getWhen(entities_in_article,articles,who_n_what[0])
    print("when: ",when)
    where = getWhere(inputFile, entities_in_article)
    print('where: ', where)
    for articleID in articles.keys():
    	publicationDate = articles[articleID].date
    	link = articles[articleID].url
    event1 = Event(who_n_what[0], who_n_what[1], where[0], when, "", "", publicationDate,link)
    return event1
   
   
Extractor("../data/test.txt")