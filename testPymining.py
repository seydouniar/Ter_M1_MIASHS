from pymining import itemmining
txt = open("/Users/Eloan/Desktop/Ter_M1_MIASHS/Sans_titre.txt").read()
list_phrase=txt.split(".")
print(list_phrase)
transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
relim_input = itemmining.get_relim_input(transactions)
report = itemmining.relim(relim_input, min_support=2)
report
