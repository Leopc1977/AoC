#https://stackoverflow.com/questions/489999/convert-list-of-ints-to-one-number
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    #s = int(s)              # 123
    return s

rateOxygen = 0
rateCarbon = 0

total = 0
lines = []
with open('AoC\day_3\input.txt') as file:
    for line in file:
        lstNumber = []
        for number in line:
            try:
                lstNumber.append(int(number))
            except:
                pass
        lines.append(lstNumber)        

def getMaxFromColumnANDFilter(lines, lstLineIndex,currentColumn):
    #getMax
    lstQteBit = [0,0]
    for line in lstLineIndex:
        lstQteBit[lines[line][currentColumn]]+=1

    maxi = int(lstQteBit[1]>=lstQteBit[0])
    lstGoodOnes=[]
    #filter good ones and return it
    for i in range(len(lstLineIndex)):
        indexLine = lstLineIndex[i]
        if lines[indexLine][currentColumn]==maxi:
            lstGoodOnes.append(indexLine)
    return lstGoodOnes

lstLineIndex = [i for i in range(len(lines))]
currentColumn = 0
while len(lstLineIndex)>1:
    lstLineIndex = getMaxFromColumnANDFilter(lines, lstLineIndex, currentColumn)
    currentColumn+=1   

rateOxygen= int(magic(lines[lstLineIndex[0]]),2)

def getMinFromColumnANDFilter(lines, lstLineIndex,currentColumn):
    #getMax
    lstQteBit = [0,0]
    for line in lstLineIndex:
        lstQteBit[lines[line][currentColumn]]+=1

    mini = int(lstQteBit[1]<lstQteBit[0])
    lstGoodOnes=[]
    #filter good ones and return it
    for i in range(len(lstLineIndex)):
        indexLine = lstLineIndex[i]
        if lines[indexLine][currentColumn]==mini:
            lstGoodOnes.append(indexLine)
    return lstGoodOnes

lstLineIndex = [i for i in range(len(lines))]
currentColumn = 0
while len(lstLineIndex)>1:
    lstLineIndex = getMinFromColumnANDFilter(lines, lstLineIndex, currentColumn)
    currentColumn+=1   

rateCarbon= int(magic(lines[lstLineIndex[0]]),2)

print(rateOxygen*rateCarbon)