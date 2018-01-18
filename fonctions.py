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
    resultat=[]
    for i in range(len(phrase)) :
        e=pattern[0]

        indent=quel_type(e[0])

        if (phrase[i][indent]==e[2:]):
            boolean,res=possiblement_correct(phrase[i:],pattern)
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
        if len(res)>0:
            
            resultat+=[i,res]
    return resultat

#"Écrire le pattern voulu en suivant la syntaxe suivante :"
# pattern_research(corpus,"g:PRO:PER,g:VER:pres,g:ADV")
#[0, [('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')], 1, [('On', 'on', 'PRO:PER'), ('a', 'avoir', 'VER:pres'), ('déjà', 'déjà', 'ADV'), ('il', 'il', 'PRO:PER'), ('est', 'être', 'VER:pres'), ('assez', 'assez', 'ADV')], 4, [('on', 'on', 'PRO:PER'), ('aime', 'aimer', 'VER:pres'), ('trop', 'trop', 'ADV')], 43, [('on', 'on', 'PRO:PER'), ('retrouve', 'retrouver', 'VER:pres'), ('souvent', 'souvent', 'ADV')], 52, [('se', 'se', 'PRO:PER'), ('prête', 'prêter', 'VER:pres'), ('fort', 'fort', 'ADV')], 63, [('le', 'le', 'PRO:PER'), ('montre', 'montrer', 'VER:pres'), ('très', 'très', 'ADV')], 66, [('y', 'y', 'PRO:PER'), ('a', 'avoir', 'VER:pres'), ('ainsi', 'ainsi', 'ADV')], 78, [('on', 'on', 'PRO:PER'), ('peut', 'pouvoir', 'VER:pres'), ('bien', 'bien', 'ADV')], 82, [('il', 'il', 'PRO:PER'), ('parle', 'parler', 'VER:pres'), ('directement', 'directement', 'ADV')]]
#"Exemple 2 : m:infini,l:et,g:ADJ"
#Avec : 'm' pour mot, 'l' pour lemme et 'g' pour groupe nominal "
def pattern_research(corpus,pattern):

    resultat=[]
    #note : on ne peut pas chercher une virgule ça peut poser probleme!
    liste_pattern = pattern.split(',')
    resultat = recherche_corpus(corpus,liste_pattern)
    return resultat
