total = 0
lines = []
with open('input.txt') as file:
    for line in file:
        lines.append(int(line))

"""currentNumber = lines[0]
for i in range(1, len(lines)-1):
    nextNumber = lines[i]
    if currentNumber < nextNumber:
        total = total + 1
    currentNumber = nextNumber"""

nbLine = len(lines)#366 #3*366 = 1998
lstLetter=[]
for i in range(nbLine):
    currentNumber = lines[i]
    lstLetter.append([currentNumber])
    for k in range(len(lstLetter)):
        if len(lstLetter[k])<3:
            lstLetter[k].append(currentNumber)
print(lstLetter[0])
for k in range(len(lstLetter)):
    if len(lstLetter[k])<3:
        lstLetter.pop(k)

for k in range(8):
    lstLetter[k] = sum(lstLetter[k])
    print(lstLetter[k])

currentNumber = lstLetter[0]
"""for i in range(1, len(lstLetter)-1):
    nextNumber = lstLetter[i]
    if currentNumber < nextNumber:
        total = total + 1
    currentNumber = nextNumber"""

print(total)