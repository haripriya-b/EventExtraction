from guess_who import getWho

def getWhat(whoAll,parseTree):
	who_n_what = []
	
	originalWho = whoAll[:]
	
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
				who_n_what.append((who,semiFinal))	
					#p = p[i:]
			#else:
			#	print(who," does not have a what, move to the next who")		
			#continue
	return who_n_what				
			#for i in p:
			#	print i
				
def get_who_and_what(who):

	with open("../data/articles/title/parseTrees.dat","r") as titleFile:
		titleTree = titleFile.readline() 

	with open("../data/articles/text/parseTrees.dat","r") as textFile:
		textTree = textFile.readline()
	#print(textTree)
	who_n_what_title = getWhat(who,titleTree)
	who_n_what_text = getWhat(who, textTree)
	#print(who_n_what_text)
	if len(who_n_what_title) == 0:
		who_n_what_text = getWhat(who,textTree)
	#	print ("text: ", who_n_what_text)
		return who_n_what_text[0]
	else:
	#	print("title: ", who_n_what_title)
		return who_n_what_title[0]