#https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    #s = int(s)              # 123
    return s

rateGamma = []
rateEpsilon = []

total = 0
lines = []
with open('input.txt') as file:

    for line in file:
        lstNumber = []
        for number in line:
            try:
                lstNumber.append(int(number))
            except:
                pass
        lines.append(lstNumber)        

lstBitByColumn = []
for c in range(len(lines[0])):
    currentColumn = []
    for l in range(len(lines)):
        currentBit = lines[l][c]
        currentColumn.append(currentBit)
    lstBitByColumn.append(currentColumn)

lstQteBitByColumn = []
for column in lstBitByColumn: #[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    lstQteBit = [0,0]
    for number in column:
        lstQteBit[number]+=1
    lstQteBitByColumn.append(lstQteBit)

for qte in lstQteBitByColumn:
    rateGamma.append(int(qte[1]>qte[0]))
    rateEpsilon.append(int(qte[1]<qte[0]))

rateGamma = int(magic(rateGamma),2)
rateEpsilon = int(magic(rateEpsilon),2)

res = rateEpsilon*rateGamma
print(res)