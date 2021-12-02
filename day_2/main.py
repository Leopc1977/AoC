def forward(a,b):
    return a+b
def down(a,b):
    return a+b
def up(a,b):
    return a-b

lines = []
with open('input.txt') as file:
    for line in file:
        values = line.split() #ex : forward 5
        move = values[0] #forward
        dist = int(values[1]) #5
        lines.append([move, dist])

horizontalPos, depth, aim = 0,0,0
for move in lines:
    dist = move[1]
    func = move[0]
    print(dist)
    if func == "forward":
        depth = depth+aim*dist
        horizontalPos = forward(horizontalPos,dist)
    elif func == "up":
        aim=aim-dist
    elif func == "down":
        aim=aim+dist

print(depth*horizontalPos)