# f = open('day9input.txt', 'r')
f = open('day9ex.txt', 'r')
lines = f.readlines()

instr = []
for line in lines:
    dir = line.strip().split(' ')[0]
    amt = int(line.strip().split(' ')[1])
    instr.append((dir, amt))

# Part 1

currHx = 0
currHy = 0
currTx = 0
currTy = 0

headvisited = set()
headvisited.add((0,0))
tailvisited = set()
tailvisited.add((0,0))

for item in instr:
    # Head moves
    if item[0] == 'U':
        for i in range(item[1]):
            currHy -= 1
            headvisited.add((currHx, currHy))
    if item[0] == 'L':
        for i in range(item[1]):
            currHx -= 1
            headvisited.add((currHx, currHy))
    if item[0] == 'D':
        for i in range(item[1]):
            currHy += 1
            headvisited.add((currHx, currHy))
    if item[0] == 'R':
        for i in range(item[1]):
            currHx += 1
            headvisited.add((currHx, currHy))
    # Tail moves
    diffx = currHx - currTx
    diffy = currHy - currTy
    # Diagonal Cases
    if abs(diffx) > 1 or abs(diffy) > 1:
        print(diffx, diffy)
        while diffx >= 2:
            currTx += 1
            diffx = currHx - currTx
            visited.add((currTx, currTy))
        while diffx <= -2:
            currTx -= 1
            diffx = currHx - currTx
            visited.add((currTx, currTy))
        while diffy >= 2:
            currTy += 1
            diffy = currHy - currTy
            visited.add((currTx, currTy))
        while diffy <= -2:
            currTy -= 1
            diffy = currHy - currTy
            visited.add((currTx, currTy))

print(headvisited)
print(len(headvisited))