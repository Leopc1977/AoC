rateOxygen = []
rateCarbon = []

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

def getMaxFromColumnANDFilter(lines, lstLineIndex,currentColumn):
    #getMax
    lstQteBit = [0,0]
    for line in lstLineIndex:
        lstQteBit[lines[line][currentColumn]]+=1

    maxi = int(lstQteBit[1]>lstQteBit[0])

    #filter good ones and return it
    for i in range(len(lstLineIndex)-1,0,-1):
        indexLine = lstLineIndex[i]
        if lines[indexLine][currentColumn]!=maxi:
            lstLineIndex.remove(indexLine)

    return lstLineIndex

lstLineIndex = [i for i in range(len(lines))]

currentColumn = 0
while len(lstLineIndex)>1:
    lstLineIndex = getMaxFromColumnANDFilter(lines, lstLineIndex, currentColumn)
    currentColumn+=1
    
print(lines[lstLineIndex[0]])