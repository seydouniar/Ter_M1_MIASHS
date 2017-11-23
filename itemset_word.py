#!/usr/bin/env python3
import codecs
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/seydou/Bureau/TER_DOC/stanford-corenlp-full-2017-06-09/',lang='fr')
#fileout = open("SHORTER.txt","w")
txt =codecs.open("Sans_titre.txt",'r','utf-8')
a= txt.read()
phrases = a.split('.')
#add etiquette function
"""def add_etiquette(motEtiqs,etiquette):
	for etiq in motEtiqs:
		if etiquette==etiq:
			break;
		else:
			motEtiqs.append(etiquette)
	return motEtiqs"""

#append word etiquette function
def iskif_kif(etq1,etq2):
    lis_etqs = etq1.split('|')
    for e in lis_etqs:
    	if e==etq2:
    		return False
    return True

motEtiqs = {}
mot_listes=nlp.pos_tag("")

for ph in phrases:
	words=nlp.pos_tag(ph)
	mot_listes+=words
#print(len(mot_listes))
for word_etq in mot_listes:
	motEtiqs[word_etq[0]]=word_etq[1]
#print(len(motEtiqs))

for we in mot_listes:
	print(we)
	for key in motEtiqs.keys():
		if we[0]==key and iskif_kif(motEtiqs[key],we[1]):
			motEtiqs[key] = motEtiqs[key] + "|"+we[1]
print(motEtiqs)

		#print(motEtiqs[w[0]])
"""etqEnrichis=motEtiqs
for ph in phrases:
	words=nlp.pos_tag(ph)
	for w in words:
		for x in xrange(1,10):
			pass
		if 
		motEtiqs[w[0]]=w[1]

"""
#1 itération




#props={'annotators': 'pos','pipelineLanguage':'fr','outputFormat':'text'}
#fileout.write(nlp.annotate(phrases[0],properties=props.ner))
#print (nlp.annotate(phrases[0],properties=props))

#fileout.close() 