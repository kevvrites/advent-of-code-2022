f = open('day1input.txt', 'r')
lines = f.readlines()

elf = 0
for line in lines:
    if line == '\n':
        elf += 1

# Part 1
elves = [0 for i in range(elf + 1)]

idx = 0
for item in lines:
    if item == '\n':
        idx += 1
    else:
        elves[idx] += int(item)

print(max(elves))

# Part 2
cal1 = max(elves)
elves.remove(max(elves))
cal2 = max(elves)
elves.remove(max(elves))
cal3 = max(elves)

print(cal1 + cal2 + cal3)