

#print(s.find(who))
def getWhat(whoAll,title):
	who_n_what = []
	
	originalWho = whoAll[:]
	
	for i in whoAll:
	   if i.find(" ") > 0:
			 whoAll.remove(i)
			 whoAll = whoAll + i.split(" ")
	
	#print whoAll
	for who in whoAll:
		p = title.split('),')
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
				
			
#st = st.split(['ParentedTree','NN'])
#print st			
#s = "{'../data/articles/title/315.txt': [ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga']), ParentedTree('NNP', ['Founder']), ParentedTree('NNP', ['Mark']), ParentedTree('NNP', ['Pincus'])]), ParentedTree('VP', [ParentedTree('VBZ', ['Steps']), ParentedTree('NP', [ParentedTree('NN', ['Down'])]), ParentedTree('PP', [ParentedTree('IN', ['From']), ParentedTree('NP', [ParentedTree('NNP', ['Chief']), ParentedTree('NNP', ['Product']), ParentedTree('NNP', ['Officer']), ParentedTree('NN', ['Role'])])])])])])]}"
#who = 'Zynga'
text = """
{'../data/articles/text/313.txt': [ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('VP', [ParentedTree('VBZ', ['is']), ParentedTree('VP', [ParentedTree('VBG', ['announcing']), ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('JJ', ['new']), ParentedTree('NN', ['addition'])]), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('PRP$', ['its']), ParentedTree('NN', ['board'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NNS', ['directors'])])])]), ParentedTree(':', ['--']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Regina']), ParentedTree('NNP', ['E.']), ParentedTree('NNP', ['Dugan'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['vice']), ParentedTree('NN', ['president'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NN', ['engineering']), ParentedTree('CC', ['and']), ParentedTree('NN', ['head'])])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NNP', ['Advanced']), ParentedTree('NNP', ['Technology']), ParentedTree('CC', ['and']), ParentedTree('NNPS', ['Projects']), ParentedTree('NN', ['group'])]), ParentedTree('PP', [ParentedTree('IN', ['at']), ParentedTree('NP', [ParentedTree('NNP', ['Google'])])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['In']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NN', ['memo'])]), ParentedTree('VP', [ParentedTree('VBN', ['sent']), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['company']), ParentedTree('POS', ["'s"])]), ParentedTree('NNS', ['employees'])])])])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['CEO']), ParentedTree('NNP', ['Don']), ParentedTree('NNP', ['Mattrick'])]), ParentedTree('VP', [ParentedTree('VBD', ['said']), ParentedTree('SBAR', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan'])]), ParentedTree('VP', [ParentedTree('MD', ['will']), ParentedTree('VP', [ParentedTree('VB', ['be']), ParentedTree('``', ['``']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('JJ', ['true']), ParentedTree('NN', ['catalyst'])]), ParentedTree('PP', [ParentedTree('IN', ['for']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('JJ', ['creative']), ParentedTree('NN', ['thinking'])]), ParentedTree('PP', [ParentedTree('IN', ['at']), ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])])])])])])])])])])]), ParentedTree('.', ['.']), ParentedTree("''", ["''"])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('SBAR', [ParentedTree('IN', ['As']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBN', ['highlighted']), ParentedTree('PP', [ParentedTree('IN', ['at']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('JJ', ['recent']), ParentedTree('NNP', ['Google']), ParentedTree('NNP', ['I/O']), ParentedTree('NN', ['developer']), ParentedTree('NN', ['conference'])])])])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan']), ParentedTree('POS', ["'s"])]), ParentedTree('NN', ['team'])]), ParentedTree('VP', [ParentedTree('VBZ', ['is']), ParentedTree('VP', [ParentedTree('VBG', ['working']), ParentedTree('PP', [ParentedTree('IN', ['on']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNS', ['projects'])]), ParentedTree('PP', [ParentedTree('IN', ['like']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('JJ', ['temporary']), ParentedTree('JJ', ['electronic']), ParentedTree('NN', ['tattoo'])]), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WDT', ['that'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('MD', ['can']), ParentedTree('VP', [ParentedTree('VB', ['unlock']), ParentedTree('NP', [ParentedTree('PRP$', ['your']), ParentedTree('NN', ['smartphone'])])])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('-LRB-', ['-LRB-']), ParentedTree('NP', [ParentedTree('PRP', ['She'])]), ParentedTree('VP', [ParentedTree('VBD', ['described']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['group'])]), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('``', ['``']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNS', ['pirates'])]), ParentedTree('VP', [ParentedTree('VBG', ['trying']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('TO', ['to']), ParentedTree('VP', [ParentedTree('VB', ['do']), ParentedTree('NP', [ParentedTree('NN', ['epic']), ParentedTree('NN', ['shit'])])])])])])])])]), ParentedTree('.', ['.']), ParentedTree("''", ["''"]), ParentedTree('-RRB-', ['-RRB-'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['Before']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBG', ['joining']), ParentedTree('NP', [ParentedTree('NNP', ['Google/Motorola']), ParentedTree('NN', ['Mobility'])])])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['Dugan'])]), ParentedTree('VP', [ParentedTree('VBD', ['served']), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['director'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NNP', ['Defense']), ParentedTree('NNP', ['Advanced']), ParentedTree('NNP', ['Research']), ParentedTree('NNP', ['Projects']), ParentedTree('NNP', ['Agency'])])]), ParentedTree(',', [',']), ParentedTree('VP', [ParentedTree('ADVP', [ParentedTree('RB', ['better'])]), ParentedTree('VBN', ['known']), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('NP', [ParentedTree('NNP', ['DARPA'])])])])])])])]), ParentedTree(':', ['--']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['she'])]), ParentedTree('VP', [ParentedTree('VBD', ['was']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['agency']), ParentedTree('POS', ["'s"])]), ParentedTree('JJ', ['first']), ParentedTree('JJ', ['female']), ParentedTree('NN', ['leader'])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('S', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga']), ParentedTree('POS', ["'s"])]), ParentedTree('NN', ['press']), ParentedTree('NN', ['release'])]), ParentedTree('VP', [ParentedTree('VBZ', ['highlights']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NN', ['bunch'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('JJ', ['media-related']), ParentedTree('NNS', ['honors'])])])]), ParentedTree('ADVP', [ParentedTree('RB', ['as']), ParentedTree('RB', ['well'])])])]), ParentedTree(',', [',']), ParentedTree('CC', ['but']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['I'])]), ParentedTree('VP', [ParentedTree('VBP', ["'m"]), ParentedTree('ADJP', [ParentedTree('JJ', ['partial']), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['reporter']), ParentedTree('NNP', ['Liz']), ParentedTree('NNP', ['Gannes']), ParentedTree('POS', ["'"])]), ParentedTree('JJ', ['complimentary']), ParentedTree('NN', ['description'])])])])])])]), ParentedTree(':', [':']), ParentedTree('``', ['``']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Google']), ParentedTree('POS', ["'s"])]), ParentedTree('NNP', ['Regina']), ParentedTree('NNP', ['Dugan'])]), ParentedTree('VP', [ParentedTree('VBZ', ['Is']), ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NNP', ['Badass'])])])]), ParentedTree('.', ['.']), ParentedTree("''", ["''"])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('DT', ['The']), ParentedTree('NN', ['appointment'])]), ParentedTree('VP', [ParentedTree('VBZ', ['follows']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['departure'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NNP', ['LinkedIn']), ParentedTree('NN', ['co-founder']), ParentedTree('NNP', ['Reid']), ParentedTree('NNP', ['Hoffman'])])])]), ParentedTree('CC', ['and']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['DreamWorks']), ParentedTree('NNP', ['Animation']), ParentedTree('NNP', ['CEO']), ParentedTree('NNP', ['Jeffrey']), ParentedTree('NNP', ['Katzenberg'])]), ParentedTree('PP', [ParentedTree('IN', ['from']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga']), ParentedTree('POS', ["'s"])]), ParentedTree('NN', ['board'])])])])]), ParentedTree('NP-TMP', [ParentedTree('JJ', ['last']), ParentedTree('NN', ['month'])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('DT', ['Those']), ParentedTree('NNS', ['departures'])]), ParentedTree('VP', [ParentedTree('VBD', ['meant']), ParentedTree('SBAR', [ParentedTree('IN', ['that']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('VP', [ParentedTree('VBD', ['was']), ParentedTree('ADVP', [ParentedTree('ADVP', [ParentedTree('RB', ['no']), ParentedTree('RBR', ['longer'])]), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('NN', ['compliance'])])])]), ParentedTree('PP', [ParentedTree('IN', ['with']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NNP', ['NASDAQ']), ParentedTree('NN', ['listing']), ParentedTree('NN', ['rule'])]), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WDT', ['that'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBD', ['required']), ParentedTree('NP', [ParentedTree('NNS', ['boards'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('TO', ['to']), ParentedTree('VP', [ParentedTree('VB', ['have']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NN', ['majority'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('JJ', ['independent']), ParentedTree('NNS', ['directors'])])])])])])])])])])])]), ParentedTree(',', [',']), ParentedTree('SBAR', [ParentedTree('IN', ['as']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBN', ['noted']), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('JJ', ['regulatory']), ParentedTree('NN', ['filing'])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['With']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan']), ParentedTree('POS', ["'s"])]), ParentedTree('NN', ['appointment'])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('VP', [ParentedTree('MD', ['should']), ParentedTree('VP', [ParentedTree('VB', ['be']), ParentedTree('ADJP', [ParentedTree('JJ', ['compliant'])]), ParentedTree('ADVP', [ParentedTree('RB', ['again'])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('EX', ['There'])]), ParentedTree('VP', [ParentedTree('VBP', ['are']), ParentedTree('ADVP', [ParentedTree('RB', ['now'])]), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('CD', ['five']), ParentedTree('JJ', ['independent']), ParentedTree('NNS', ['directors'])]), ParentedTree('PRN', [ParentedTree('-LRB-', ['-LRB-']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Stanley']), ParentedTree('NNP', ['J.']), ParentedTree('NNP', ['Meresman'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['Sunil']), ParentedTree('NNP', ['Paul'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['Ellen']), ParentedTree('NNP', ['F.']), ParentedTree('NNP', ['Smirnoff'])]), ParentedTree(',', [',']), ParentedTree('CC', ['and']), ParentedTree('NP', [ParentedTree('NNP', ['John']), ParentedTree('NNP', ['Doerr'])])]), ParentedTree(',', [',']), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WP', ['who'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBZ', ['is']), ParentedTree('ADVP', [ParentedTree('RB', ['now'])]), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['lead']), ParentedTree('JJ', ['independent']), ParentedTree('NN', ['director'])])])])])])]), ParentedTree('-RRB-', ['-RRB-'])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('DT', ['The']), ParentedTree('JJ', ['other']), ParentedTree('NN', ['board']), ParentedTree('NNS', ['members'])]), ParentedTree('VP', [ParentedTree('VBP', ['are']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['founder']), ParentedTree('CC', ['and']), ParentedTree('NN', ['chairman'])]), ParentedTree('NNP', ['Mark']), ParentedTree('NNP', ['Pincus']), ParentedTree(',', [',']), ParentedTree('NNP', ['Bing']), ParentedTree('NNP', ['Gordon']), ParentedTree('CC', ['and']), ParentedTree('NNP', ['Mattrick'])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan'])]), ParentedTree('VP', [ParentedTree('MD', ['will']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VP', [ParentedTree('NN', ['chair']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['board']), ParentedTree('POS', ["'s"])]), ParentedTree('ADJP', [ParentedTree('JJ', ['nominating']), ParentedTree('CC', ['and']), ParentedTree('NN', ['governance'])]), ParentedTree('NN', ['committee'])])]), ParentedTree('CC', ['and']), ParentedTree('VP', [ParentedTree('MD', ['will']), ParentedTree('ADVP', [ParentedTree('RB', ['also'])]), ParentedTree('VP', [ParentedTree('VB', ['be']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NN', ['member'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['product']), ParentedTree('NN', ['committee'])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['In']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['release'])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('PRP', ['she'])]), ParentedTree('VP', [ParentedTree('VBD', ['said'])])]), ParentedTree(':', [':']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['I'])]), ParentedTree('VP', [ParentedTree('VBP', ['believe']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['we'])]), ParentedTree('VP', [ParentedTree('VB', ['need']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('TO', ['to']), ParentedTree('VP', [ParentedTree('VB', ['play'])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('VP', [ParentedTree('VBZ', ['is']), ParentedTree('ADJP', [ParentedTree('JJ', ['full']), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('JJ', ['creative']), ParentedTree('NNS', ['thinkers'])]), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WP', ['who'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBP', ['embrace']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['power'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NN', ['play'])])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Einstein'])]), ParentedTree('ADVP', [ParentedTree('RB', ['famously'])]), ParentedTree('VP', [ParentedTree('VBD', ['stated']), ParentedTree('SBAR', [ParentedTree('IN', ['that']), ParentedTree('S', [ParentedTree('S', [ParentedTree('``', ['`']), ParentedTree('NP', [ParentedTree('JJ', ['combinatory']), ParentedTree('NN', ['play'])]), ParentedTree('VP', [ParentedTree('VBZ', ['seems']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('TO', ['to']), ParentedTree('VP', [ParentedTree('VB', ['be']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('JJ', ['essential']), ParentedTree('NN', ['feature'])]), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('JJ', ['productive']), ParentedTree('NN', ['thought'])])])])])])])]), ParentedTree(',', [',']), ParentedTree("''", ["'"])]), ParentedTree('CC', ['and']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('DT', ['this']), ParentedTree('NN', ['spirit'])]), ParentedTree('VP', [ParentedTree('VBZ', ['is']), ParentedTree('VP', [ParentedTree('VBN', ['embodied']), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Zynga']), ParentedTree('POS', ["'s"])]), ParentedTree('NNS', ['products'])]), ParentedTree(',', [',']), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WDT', ['which'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBP', ['have']), ParentedTree('VP', [ParentedTree('VBN', ['brought']), ParentedTree('NP', [ParentedTree('JJ', ['new']), ParentedTree('NN', ['technology'])]), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('NP', [ParentedTree('NNS', ['games'])])])])])])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNPS', ['Games'])]), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WDT', ['that'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBP', ['help']), ParentedTree('NP', [ParentedTree('NNS', ['people'])])])])])]), ParentedTree('VP', [ParentedTree('VP', [ParentedTree('VP', [ParentedTree('VB', ['connect'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['share'])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NN', ['rest'])])])]), ParentedTree('CC', ['and']), ParentedTree('VP', [ParentedTree('VB', ['energize']), ParentedTree('PP', [ParentedTree('IN', ['through']), ParentedTree('NP', [ParentedTree('NN', ['play'])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['I'])]), ParentedTree('VP', [ParentedTree('VBP', ['look']), ParentedTree('ADVP', [ParentedTree('RB', ['forward'])]), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBG', ['working']), ParentedTree('PP', [ParentedTree('IN', ['with']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Don'])]), ParentedTree('CC', ['and']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['board'])])])]), ParentedTree('PP', [ParentedTree('IN', ['on']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['company']), ParentedTree('POS', ["'s"])]), ParentedTree('JJ', ['next']), ParentedTree('NN', ['chapter'])]), ParentedTree('SBAR', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['Despite']), ParentedTree('NP', [ParentedTree('DT', ['some']), ParentedTree('JJ', ['high-profile']), ParentedTree('NNS', ['struggles']), ParentedTree('CC', ['and']), ParentedTree('NNS', ['layoffs'])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('NNP', ['Zynga'])]), ParentedTree('ADVP', [ParentedTree('RB', ['actually'])]), ParentedTree('VP', [ParentedTree('VBD', ['came']), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('RB', ['slightly']), ParentedTree('RB', ['ahead'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NN', ['analyst']), ParentedTree('NNS', ['estimates'])])])])]), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('PRP$', ['its']), ParentedTree('ADJP', [ParentedTree('RBS', ['most']), ParentedTree('JJ', ['recent'])]), ParentedTree('NNS', ['earnings']), ParentedTree('NN', ['report'])])])])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('PP', [ParentedTree('IN', ['At']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['time'])])]), ParentedTree(',', [',']), ParentedTree('NP', [ParentedTree('PRP', ['it'])]), ParentedTree('ADVP', [ParentedTree('RB', ['also'])]), ParentedTree('VP', [ParentedTree('VBD', ['announced']), ParentedTree('SBAR', [ParentedTree('IN', ['that']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Pincus'])]), ParentedTree('PRN', [ParentedTree('-LRB-', ['-LRB-']), ParentedTree('SBAR', [ParentedTree('WHNP', [ParentedTree('WP', ['who'])]), ParentedTree('S', [ParentedTree('VP', [ParentedTree('VBD', ['was']), ParentedTree('VP', [ParentedTree('VBN', ['replaced']), ParentedTree('PP', [ParentedTree('IN', ['by']), ParentedTree('NP', [ParentedTree('NNP', ['Mattrick'])])]), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('NP', [ParentedTree('NNP', ['CEO'])])]), ParentedTree('NP-TMP', [ParentedTree('JJ', ['last']), ParentedTree('NN', ['year'])])])])])]), ParentedTree('-RRB-', ['-RRB-'])])]), ParentedTree('VP', [ParentedTree('MD', ['would']), ParentedTree('VP', [ParentedTree('VB', ['be']), ParentedTree('VP', [ParentedTree('VBG', ['stepping']), ParentedTree('ADVP', [ParentedTree('RB', ['down']), ParentedTree('PP', [ParentedTree('IN', ['from']), ParentedTree('NP', [ParentedTree('DT', ['an']), ParentedTree('JJ', ['operational']), ParentedTree('NN', ['role'])])])]), ParentedTree('PP', [ParentedTree('IN', ['at']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['company'])])])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('FRAG', [ParentedTree('NP', [ParentedTree('NNP', ['Update'])]), ParentedTree(':', [':']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('PRP', ['You'])]), ParentedTree('VP', [ParentedTree('MD', ['can']), ParentedTree('VP', [ParentedTree('VB', ['see']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('JJ', ['regulatory']), ParentedTree('NN', ['filing'])]), ParentedTree('VP', [ParentedTree('VBN', ['related']), ParentedTree('PP', [ParentedTree('TO', ['to']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NNP', ['Dugan']), ParentedTree('POS', ["'s"])]), ParentedTree('NN', ['appointment'])])]), ParentedTree('ADVP', [ParentedTree('RB', ['here'])])])])])])]), ParentedTree('.', ['.'])])]), ParentedTree('ROOT', [ParentedTree('S', [ParentedTree('NP', [ParentedTree('DT', ['The']), ParentedTree('NN', ['filing'])]), ParentedTree('ADVP', [ParentedTree('RB', ['also'])]), ParentedTree('VP', [ParentedTree('VBZ', ['mentions']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('NNP', ['Mattrick'])]), ParentedTree('VP', [ParentedTree('VBG', ['vesting']), ParentedTree('S', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NN', ['stock'])]), ParentedTree('PP', [ParentedTree('IN', ['as']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('NN', ['result'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('NP', [ParentedTree('PRP$', ['his']), ParentedTree('JJ', ['first']), ParentedTree('NN', ['anniversary'])]), ParentedTree('PP', [ParentedTree('IN', ['at']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['company'])])])]), ParentedTree(',', [',']), ParentedTree('CC', ['and']), ParentedTree('NP', [ParentedTree('DT', ['a']), ParentedTree('JJ', ['related']), ParentedTree('NN', ['stock']), ParentedTree('NN', ['sale'])])])])])])]), ParentedTree('``', ['``']), ParentedTree('VP', [ParentedTree('TO', ['to']), ParentedTree('VP', [ParentedTree('VB', ['satisfy']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['Company']), ParentedTree('POS', ["'s"])]), ParentedTree('JJ', ['statutory']), ParentedTree('NN', ['tax']), ParentedTree('NN', ['withholding']), ParentedTree('NNS', ['obligations'])]), ParentedTree('PP', [ParentedTree('IN', ['in']), ParentedTree('NP', [ParentedTree('NN', ['connection'])])]), ParentedTree('PP', [ParentedTree('IN', ['with']), ParentedTree('NP', [ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('NN', ['vesting'])]), ParentedTree('PP', [ParentedTree('IN', ['of']), ParentedTree('NP', [ParentedTree('DT', ['the']), ParentedTree('-LRB-', ['-LSB-']), ParentedTree('JJ', ['restricted']), ParentedTree('NN', ['stock']), ParentedTree('NNS', ['units'])])])])])])]), ParentedTree('-RRB-', ['-RSB-'])])])])]), ParentedTree('.', ['.']), ParentedTree("''", ["''"])])])]}
"""
#who="Zynga"
title="""
{'../data/articles/title/313.txt': '[ParentedTree(\'ROOT\', [ParentedTree(\'S\', [ParentedTree(\'NP\', [ParentedTree(\'NNP\', [\'Googler\'])]), ParentedTree(\',\', [\',\']), ParentedTree(\'NP\', [ParentedTree(\'CC\', [\'And\']), ParentedTree(\'NP\', [ParentedTree(\'NP\', [ParentedTree(\'NNP\', [\'Former\']), ParentedTree(\'NNP\', [\'DARPA\']), ParentedTree(\'NNP\', [\'Director\'])]), ParentedTree(\',\', [\',\']), ParentedTree(\'NP\', [ParentedTree(\'NNP\', [\'Regina\']), ParentedTree(\'NNP\', [\'Dugan\'])])])]), ParentedTree(\'VP\', [ParentedTree(\'VBZ\', [\'Joins\']), ParentedTree(\'NP\', [ParentedTree(\'NP\', [ParentedTree(\'NP\', [ParentedTree(\'NNP\', [\'Zynga\']), ParentedTree(\'POS\', ["\'s"])]), ParentedTree(\'NNP\', [\'Board\'])]), ParentedTree(\'PP\', [ParentedTree(\'IN\', [\'Of\']), ParentedTree(\'NP\', [ParentedTree(\'NNS\', [\'Directors\'])])])])])])])]'}
"""
who = ["Regina Dugan","Zynga","Don Mattrick","Advanced Technology and Projects","DARPA ","Google"]

who_n_what_title = getWhat(who,title)
who_n_what_text = getWhat(who,text)
who_n_what = who_n_what_text + who_n_what_title
print(who_n_what)
