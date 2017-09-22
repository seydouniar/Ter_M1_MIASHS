from pymining import itemmining
<<<<<<< HEAD
txt = open("Sans_titre.txt".encode("utf-8")).read()
print(txt)
txt=str(txt)
list_phrase=txt.split(".")
List_phrases=[]
for i in range(len(list_phrase)-2):
    List_phrases.append(list_phrase[i].split(" "))
    List_phrases[i]
relim_input = itemmining.get_relim_input(List_phrases)

report = itemmining.relim(relim_input, min_support=12)
    

print(len(report))
print(report)
=======
txt = open("/Users/Eloan/Desktop/Ter_M1_MIASHS/Sans_titre.txt").read()
list_phrase=txt.split(".")
print(list_phrase)
transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)
report
>>>>>>> 0a8458650e91173df5ade9335162726559ab443e
