
PHRASES=[[0]]
with open("Sans_titre.txt") as fileobj:
    for line in fileobj:
       for ch in line: 
           if (ch=='.' or '?' or '!'):
           	PHRASES.append([[]])
           if (ch==' '):
           	PHRASES[-1].append([])
           else :
           	if 	PHRASES[-1][-1]==[]:
           		PHRASES[-1][-1]=ch
           	else: PHRASES[-1][-1]=str(PHRASES[-1][-1])+str(ch)

for i in range(len(PHRASES)):
	print(PHRASES[i])