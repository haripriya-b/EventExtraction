import corefResolution
from guess_who import getWho
from guess_what import get_who_and_what
from FeatureExtractor import generate_entity_features

def Extractor(inputFile):
    articles = corefResolution.create_title_input(inputFile)
    entities_in_article = generate_entity_features()
    who_and_prob = getWho(inputFile, entities_in_article)
    who = []
    for (ent, prb) in who_and_prob:
        who.append(ent)
    who_n_what = get_who_and_what(who)
    print("who_n_what: ", who_n_what)
    
Extractor("../data/test.txt")