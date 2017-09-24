from pymining import itemmining
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
