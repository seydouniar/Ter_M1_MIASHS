#!/usr/bin/env python
from pymining import itemmining
from pymining import seqmining
from pymining import perftesting
txt = open("Sans_titre.txt".encode("utf-8")).read()
print(txt)
txt=str(txt)
list_phrase=txt.split(".")
List_phrases=[]
for i in range(len(list_phrase)-1):
    List_phrases.append(list_phrase[i].split(" "))
    List_phrases[i]
relim_input = itemmining.get_relim_input(List_phrases)
print("Entrer la longueur minimal des mots")
report = itemmining.relim(relim_input, min_support=int(input()))
    

print(len(report))
print(report)
print("Utilisation de sequences frequents")
List_Sequences = []
for i in range(len(list_phrase)-1):
	List_Sequences.append(list_phrase[i].split(" "))
print("Entrer la longueur minimale:")
freq_seqs = seqmining.freq_seq_enum(List_Sequences,int(input()))
result=sorted(freq_seqs)
print(result)

#perftesting.test_itemset_perf()