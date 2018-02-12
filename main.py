import itemSet_TreeTag as itm
import fonctions as fct
from corpus_stanford import get_seqence


f=open("Sans_titre.txt",'r')
text = f.read()
f.close()
corpus = itm.extract_etq(text)
val=fct.pattern_research(corpus,"g:PRO:PER,g:VER:pres,g:ADV,g:ADV")
repoprt=get_seqence(corpus)
#print(val)
print(repoprt)
