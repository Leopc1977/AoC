total = 0
lines = []
with open('input.txt') as file:
    for line in file:
        lines.append(int(line))

#first star
"""currentNumber = lines[0]
for i in range(1, len(lines)-1):
    nextNumber = lines[i]
    if currentNumber < nextNumber:
        total = total + 1
    currentNumber = nextNumber"""

#second star
nbLine = len(lines)
lstLetter=[]
for i in range(nbLine):
    currentNumber = lines[i]
    for k in range(len(lstLetter)):
        if len(lstLetter[k])<3:
            lstLetter[k].append(currentNumber)
    lstLetter.append([currentNumber])

for k in range(len(lstLetter)-1):
    if len(lstLetter[k])<3:
        lstLetter.pop(k)
        
#sum each letter
for k in range(len(lstLetter)):
    print(lstLetter[k])
    lstLetter[k] = sum(lstLetter[k])

currentNumber = lstLetter[0]
for i in range(1, len(lstLetter)-1):
    nextNumber = lstLetter[i]
    if currentNumber < nextNumber:
        total = total + 1
    currentNumber = nextNumber

print(total)