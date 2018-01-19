import itemSet_TreeTag as itm
import fonctions as fct


f=open("Sans_titre.txt",'r')
text = f.read()
f.close()
corpus = itm.extract_etq(text)
val=fct.pattern_research(corpus,"m:infini,l:et,g:ADJ")
print(val)
