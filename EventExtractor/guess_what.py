from guess_who import getWho
from nltk.tree import *
import json
from DistUpgrade.DistUpgradeViewText import readline


'''
def getWhat(whoAll,sentenceTree):
	
	
	
	who_n_what = []
	
	originalWho = whoAll[:]
	#print("who_all", whoAll)
	for i in whoAll:
	   if i.find(" ") > 0:
	   		whoAll.remove(i)
	   		whoAll = whoAll + i.split(" ")
	
	#print whoAll
	for who in whoAll:
		p = parseTree.split('),')
		#for i in p:
		#	print i
			
		#print "hello"	
		who_in_title = False
		for i in range(0,len(p)):
			if p[i].find(who) > 0:
				who_in_title = True
				p = p[i+1:]
				break
		if who_in_title:					
			#for i in p:
				#print i						
			#for i in range(0,len(p)):
			index = p[0].find('VP')
			if index > 0:
				p[0] = p[0][index:]
				st = p[0][p[0].find('['):]
				count = 0

				if p[0].find('[')>0:
					count =1
					
					for i in range(p[0].find('[')+1,len(p[0])):
						if p[0][i] == ']':
							count = count-1
						elif p[0][i] =='[':
							count = count + 1
					#print count		
							
					if count >0:
						p = p[1:]			
				#print "hi"
				flag = "f"
				for i in p:
					for j in range(0,len(i)):
						if i[j] == ']':
							count = count-1
							#print count,i[j]
							if count == 0:
								flag = "t"
								break 
						elif i[j] =='[':
							count = count + 1
							#print count,i[j]
						st = st + i[j]	
					if flag =="t":
						break			
				#print("st:  ",	st)											
							
				semiFinal = ""
				i = 0
				while True:
					k = st.find('[\'')
					if k == -1:break
					index = k+2
					while st[index] != "\'":
						semiFinal = semiFinal + st[index]
						index = index + 1
					st = st[k+1:]
					semiFinal = semiFinal + " "
				#print semiFinal
				#print originalWho
				for a_who in originalWho:
					#print(a_who,who)
					if a_who.find(who) > 0:
						who = a_who
				#print("whoNsemi",who,semiFinal)		
				who_n_what.append((who,semiFinal))	
					#p = p[i:]
			#else:
			#	print(who," does not have a what, move to the next who")		
			#continue
	return who_n_what				
			#for i in p:
			#	print i
'''		
'''		

def traverse(tree, first_who, what):
	
	try:
		tree.label()
	except AttributeError:
		return what
	print("Trav_what_out: ", what)
	if what != "":
		print("Trav_what: ", what)
		return what
    
	if tree.label() == "NP" and (first_who in tree.leaves()):
		print("is NP")
		tree.draw()
		right = tree.right_sibling()
		
		if right != None and right.label() == "VP":
			print("VP: ", ' '.join(right.leaves()))
			print(right.label())
			right.draw()
			vp = ' '.join(right.leaves())
			what += vp
	
	for child in tree:
		traverse(child, first_who, what)
'''

    	

def getWhat(who,tree):
	a = 1
	who=who.strip()
	print(who)
	a+=1
	#print(tree)
	leaf_values = tree.leaves()
	what = ""
	finalWhat = ""
	if who in leaf_values:
		leaf_index = leaf_values.index(who)
		tree_location = tree.leaf_treeposition(leaf_index)
		#print("hwer",tree[tree_location[:-1]].label())
		#tree_location = (0,3,0)
		tree_location=tree_location[:-1]
		print ("tree for:", who)
		tree.draw()
		nounList = ['NN','NNP','NNS','NP']
		temp=tree_location
		while tree[tree_location].label() in nounList :
			temp = tree_location
			tree_location = tree_location[:-1]
			
			if tree[tree_location].label() == 'NP':
				if tree[tree_location].right_sibling() is not None and tree[tree_location].right_sibling().label() == "VP":
					what = tree[tree_location].right_sibling().leaves()
					finalWhat = (finalWhat + ' ' + ' '.join(what)).strip()
					print(' '.join(what))
			
				elif tree[tree_location].right_sibling() is not None and tree[tree_location].right_sibling().leaves()[0] == ',' and tree[tree_location].right_sibling().right_sibling().label() == "VP":
					what = tree[tree_location].right_sibling().right_sibling().leaves()
					finalWhat = (finalWhat + ', ' + ' '.join(what)).strip()
					
				elif tree[tree_location].right_sibling() is not None and tree[tree_location].right_sibling().label() == 'NP-TMP' and tree[tree_location].right_sibling().right_sibling().label() == "VP":
					what = tree[tree_location].right_sibling().right_sibling().leaves()
					finalWhat = (finalWhat + ', ' + ' '.join(what)).strip()
				
	return finalWhat		
			
		#print("here",tree[tree_location].label())
		#tree_location = tree_location[:-1]
		#tree_location = temp
'''
		if tree[tree_location].right_sibling() is not None and tree[tree_location].right_sibling().label() == "VP":
			what = tree[tree_location].right_sibling().leaves()
			print(' '.join(what))
			
		elif tree[tree_location].right_sibling() is not None and tree[tree_location].right_sibling().leaves()[0] == ',' and tree[tree_location].right_sibling().right_sibling().label() == "VP":
			what = tree[tree_location].right_sibling().right_sibling().leaves()
	
	return ' '.join(what)
'''
	
	
'''	
	print("Inside getWhat")
	
	
	print("Leaf Vals: ", leaf_values)
	who_words = who.strip().split(' ')
	first_who = who_words[0]
	what = traverse(sentenceTree, first_who, "")
	
	print("What: ", what)
	

	print("last who: ", last_who)
	if last_who in leaf_values:
		print("inside if")
		leaf_index = leaf_values.index(who.strip())
		print("Leaf Index: ", leaf_index)
		tree_location = sentenceTree.leaf_treeposition(leaf_index)
		print("Tree Location: ", tree_location)
		print("Value: ", sentenceTree[tree_location])
		
		parent = 
		
'''
def get_who_and_what(whoAll):
	
	what = ""
	
	with open("../data/articles/title/parseTrees.dat","r") as titleFile:
		titleTree_with_id = json.load(titleFile)
	for i in range(0,len(titleTree_with_id.keys())):
		titleTree = titleTree_with_id[str(i)]
		for sent in titleTree.keys():
			tree = ParentedTree.fromstring(titleTree[sent])
			#print("tree in get who and what", tree," who",who[0])
			for who in whoAll: 
				for part_who in who.split():
					#print("who going in:", who)
					#print("Part who going in:", part_who)
					what = getWhat(part_who, tree)
					#print("what coming out:", what)
					if what != "": return (who, what)
					tree.draw()
		 
	if what == "":
		with open("../data/articles/text/parseTrees.dat","r") as textFile:
			textTree_with_id = json.load(textFile)
		for i in range(0,len(textTree_with_id.keys())):
			textTree = textTree_with_id[str(i)]
			for sent in textTree.keys():
				for who in whoAll:
					for part_who in who.split():
						if sent.find(part_who):
							tree = ParentedTree.fromstring(textTree[sent])
							#print("b. who going in:", who)
							#print("b. Part who going in:", part_who)
							what = getWhat(part_who, tree)
							#print("what coming out:", what)
							#tree.draw()
							if what != "":
								return (who,what)

	return (whoAll[0], "")			 
	
'''
	#print("tree", textTree)
	who_n_what_title = getWhat(who,titleTree)
	who_n_what_text = getWhat(who, textTree)
	#print("title", who_n_what_title)
	if len(who_n_what_title) == 0:
		who_n_what_text = getWhat(who,textTree)
		#print ("text: ", who_n_what_text)
		if len(who_n_what_text) > 0:
			return who_n_what_text[0]
		else: return "  "
	else:
	#	print("title: ", who_n_what_title)
		return who_n_what_title[0]
		
'''