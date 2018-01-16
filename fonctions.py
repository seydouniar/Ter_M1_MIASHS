import resultImport
corpus = resultImport.result_item_set
#cette fonction retourne quoi prendre dans le triplet => en 0 le mot en 1 le lemme ou en 2 le groupe nominal
def quel_type(l):
    if (l=='m'):
        return 0
    elif (l=='l'):
        return 1
    elif (l=='g'):
        return 2
    else :
        print ("error :",mot)
        return -1

#cette fonction appelé par recherche_phrase regarde si le morceau de phrase ayant le meme debut que pattern contient le pattern
def possiblement_correct(morceau,pattern):
    print("possiblement_correct")
    if (len(pattern)>len(morceau)):
        return (False,[])
    else:
        for  i in range(len(pattern)):
            indent=quel_type(pattern[i][0])
            if pattern[i][2:]!=morceau[i][indent]:
                return (False,[])
        return (True,morceau[0:len(pattern)])


#cette fonction de doit etre appeler que par recherche_corpus!
#elle permet de chercher le pattern dans une phrase
def recherche_phrase(phrase,pattern):
    print("recherche_phrase")
    print("pattern")
    resultat=[]
    for i in range(len(phrase)) :
        e=pattern[0]
        print("e=",e)
        indent=quel_type(e[0])
        print("==",phrase[i][indent],e)
        if (phrase[i][indent]==e[2:]):
            boolean,res=possiblement_correct(phrase[i:],pattern)
            print(boolean)
            if boolean==True:
                resultat+=res
    return resultat
            





#cette fonction de doit etre appeler que par pattern_research! 
#elle permet de chercher par phrase dans le corpus
def recherche_corpus(corpus,pattern):
    print("recherche_corpus")
    resultat=[]
    for i in range(len(corpus)) :
        res=recherche_phrase(corpus[i],pattern)
        print(res)
        if len(res)>0:
            resultat+=[]
    return resultat

#"Écrire le pattern voulu en suivant la syntaxe suivante :"
#"Exemple 1 : g:PRO:PER,g:VER:pres,g:ADV"
#"Exemple 2 : m:infini,l:et,g:ADJ"
#Avec : 'm' pour mot, 'l' pour lemme et 'g' pour groupe nominal "
def pattern_research(corpus,pattern):
    print("pattern_research")
    resultat=[]
    #note : on ne peut pas chercher une virgule ça peut poser probleme!
    liste_pattern = pattern.split(',')
    resultat = recherche_corpus(corpus,pattern)
    return resultat
