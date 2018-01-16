import resultImport

def quel_type(mot):
    l=mot[0]
    if (l=='m'):
        return 0
    elif (l=='l'):
        return 1
    elif (l=='g'):
        return 2
    else :
        print ("error :",mot)
        return -1

def research():
	print("Écrire le pattern voulu en suivant la syntaxe suivante :")
	print("Exemple 1 : g:PRO:PER,g:VER:pres,g:ADV")
	print("Exemple 2 : m:infini,l:et,g:ADJ")
	print("Avec : 'm' pour mot, 'l' pour lemme et 'g' pour groupe nominal ")
	entree=input()
	ListeResult=[]
	Corpus = resultImport.result_item_set
	ListeSearch = entree.split(',')
	#print(ListeSearch)
	Enddrap=len(ListeSearch)-1
	drap=0
	typ=0
	len(Corpus)
	#parcour le corpus
	for i in range(len(Corpus)):
		#parcour les phrase
		print("phrase=",Corpus[i])
		for j in range(len(Corpus[i])):
			print("mot=",Corpus[i][j])
	        #print("MOT:",Corpus[i][j])
			l=quel_type(ListeSearch[drap])
			drap=0
			baton=False
	        #tant que les mots dans le corpus sont en commun avec le ListeSearch : on continue !
			while (baton==False) and (ListeSearch[drap][2:] in Corpus[i][j+drap][l]):
				print("mot bon=",ListeSearch[drap][2:]," and ",Corpus[i][j+drap][l])
				drap+=1
	            #si le compte est bon
				if drap ==Enddrap:
					Res=[]
					for a in range(drap+1):
						Res+=[Corpus[i][j+a]]
						print("ajout ListeResult",[Corpus[i][j+a]])
						ListeResult+=["sentence n",i,Res]
					baton=True
				l=quel_type(ListeSearch[drap])
	            #si on est arrivé en fin de phrase avant
				if (j+drap)>=len(Corpus[i]):
					print("fin de phrase trop tot")
					baton=True
	            #print (drap,i,j,k,l)
	            #print(Corpus[i])
			drap=0
	return ListeResult


            
def research_pat(lis):
	ListeResult=[]
	Corpus = resultImport.result_item_set
	ListeSearch = lis
	Enddrap=len(ListeSearch)-1
	drap=0
	typ=0
	len(Corpus)
	for i in range(len(Corpus)):

	    for j in range(len(Corpus[i])):
	        #print("MOT:",Corpus[i][j])
	        l=quel_type(ListeSearch[drap])
	        drap=0
	        baton=False       
	        while (baton==False) and (ListeSearch[drap][2:] in Corpus[i][j+drap][l]):
	            drap+=1
	            if drap ==Enddrap:

	                
	                Res=[]
	                for a in range(drap+1):
	                    Res+=[Corpus[i][j+a]]

	                ListeResult.append([Res])
	                baton=True

	            l=quel_type(ListeSearch[drap])
	            
	            if (j+drap)>=len(Corpus[i]):
	                baton=True
	            #print (drap,i,j,k,l)
	            #print(Corpus[i])
	        drap=0
	return ListeResult           

##def most_patern_frequence(n):
##	tabhash={}
##	corpus = resultImport.result_item_set
##	for i in range (len(corpus)):
##		print(i,"/",len(corpus))
##		ListResult=[]
##		for j in range(len(corpus[i])):
##			if ((len(corpus[i])-j)<n):
##					m=n-len(corpus[i])-j
##			else:
##					m=n
##			for k in range(m):
##				for l in range(3):
##					if ((l)==0):
##						ListResult.append("m:"+corpus[i][j+k][0])
##					elif (l==1):
##						ListResult.append("l:"+corpus[i][j+k][1])
##					elif (l==2):
##						ListResult.append("g:"+corpus[i][j+k][2])
##				hashed=hash((str(ListResult)))
##				if not(hashed in tabhash):
##					tabhash[hashed]=["origin",str(ListResult)]
##					L=research_pat(ListResult)
##				    for i in range(len(L)):
##                        tabhash[hashed].append([L[i]])
##    for (key in tabhash.keys()):
##        print(key)
##    return tabhash





