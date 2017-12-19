import treetaggerwrapper
import codecs
import pprint

txt =codecs.open("Sans_titre.txt",'r','utf-8')
a=txt.read()
list_phrase=a.split(".")

# Ajout des etuquette
def add_etiquette(key,etiquette):
	key=etiquette

# Verifie l'existance de l'etiquette
def iskif_kif(etq,etqs):
    if etq in etqs:
         return False
    return True
#etiquette dict
motEtiqs = []
motEtiq_enrichi= {}

tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')
cpt=0

tous_mots=[]
mots_encrichis=[]
for phrase in list_phrase:
    #print(phrase)
    tag_phrase_tmp = tagger.tag_text(phrase)
    tag_phrase = treetaggerwrapper.make_tags(tag_phrase_tmp)
    #   print(len(tag_phrase))
    # tag contains
    mots =[]
    print(phrase)
    for tag in tag_phrase:
        etq=()
        etq += (tag.word,tag.lemma,tag.pos)
        mots.append(etq)
    tous_mots.append(mots)
    pprint.pprint(mots)
   # cpt+=len(mots)

#enrichissement de l'etiquette
"""for ph in tous_mots:
    for tup in ph:
        mot={}
        if not iskif_kif(tup[0],mot.keys()) and not iskif_kif(tup[2],mot.values):
            add_etiquette(mot[tup[0]],(tup[1],tup[2]))
        else:
            l = list(mot.items())
            l.append(tup[2])
            print(tuple(l))
            add_etiquette(mot[tup[0]],tuple(l))

        motEtiq_enrichi.append(mot)
pprint.pprint(motEtiq_enrichi)
"""






