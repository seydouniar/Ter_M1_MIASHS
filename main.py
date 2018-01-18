import itemSet_TreeTag as itm
import fonctions as fct
import codecs
with codecs.open("Sans_titre.txt",'r',encoding='utf8') as f:
    text = f.read()
    corpus = itm.extract_etq(str(text))
    print(fct.pattern_research(corpus,"g:PRO:PER,g:VER:pres,g:ADV"))
