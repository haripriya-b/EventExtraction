import ast
import nltk

from nltk.tree import *



def traverse(t):
    try:
        t.label()
        print("label: ", t.label)
    except AttributeError:
        return

    if t.label() == "'VBZ',":
        current = t
        while current.parent() is not None:

            while current.left_sibling() is not None:

                if current.left_sibling().label() == "NP":
                    np_trees.append(current.left_sibling())

                current = current.left_sibling()

            current = current.parent()

    for child in t:
        traverse(child)

'''
def traverse(list_of_lists):
    try:
        print("here1")
        for i in iter(list_of_lists):
            for j in traverse(i):
                yield j
                print (j)
    except TypeError:
        yield list_of_lists
        print (list_of_lists)
'''
textParse = {}
titleParse = {}

titlePath = "../data/articles/title/requiredData.dat"
textPath = "../data/articles/text/requiredData.dat"

with open(textPath,'r') as dataFile: 
    textParse = eval(dataFile.read())
    
with open(titlePath, 'r') as dataFile:
    titleParse = eval(dataFile.read())       
    
for articleID in textParse.keys():
    np_trees = []
    tree = nltk.tree.Tree.fromstring("(" + str(textParse[articleID]).replace("[", "").replace("]", "") + ")")
    #print(tree)
    traverse(tree)
    print (np_trees) # [ParentedTree('NP', [ParentedTree('NNP', [])])]
    
    
