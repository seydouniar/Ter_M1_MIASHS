#!/usr/bin/env python
from pymining import itemmining
from pymining import seqmining
from pymining import perftesting

txt = open("Sans_titre.txt".encode("utf-8")).read()
print(txt)
txt=str(txt)
list_phrase=txt.split(".")
List_phrases=[]
key_word=[]

for i in range(len(list_phrase)-1):
    List_phrases.append(list_phrase[i].split(" "))
    key_word.append(i)


relim_input = itemmining.get_relim_input(List_phrases)
print("Entrer la frequence minimal des mots")
report = itemmining.relim(relim_input, min_support=int(input()))
    

print(len(report))
print(report)


#feq_sorte=itemmining._sort_transactions_by_freq(List_phrases,itemmining.key_func())
print("Utilisation de sequences frequents")
List_Sequences = []
for i in range(len(list_phrase)-1):
	List_Sequences.append(list_phrase[i].split(" "))
print("Entrer la frequence minimale:")
freq_seqs = seqmining.freq_seq_enum(List_Sequences,int(input()))
result=sorted(freq_seqs)
print(result)

#perftesting.test_itemset_perf()