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
        print ("errrrrrroooooor")
        return -1

print("Ecrire le patern voulu en suivant cette forme")
print("Exemple 1 : g:PRO:PER,g:VER:pres,g:ADV")
print("Exemple 2 : l:'20e','g:NOM','m:,'")
print("selon la charte m pour mot l pour lemme et g pour groupe nominal ")
entree=input()
ListeResult=[]
Corpus = resultImport.result_item_set
ListeSearch = entree.split(',')
print(ListeSearch)
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
                    Res+=Corpus[i][j+a]

                ListeResult+=["sentence n",i,Res]
                baton=True

            l=quel_type(ListeSearch[drap])
            
            if (j+drap)>=len(Corpus[i]):
                baton=True
            #print (drap,i,j,k,l)
            #print(Corpus[i])
        drap=0
print(ListeResult)
            
            

