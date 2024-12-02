with open('./day15/input.txt', 'r') as fp:
    lines = [list(line.strip()) for line in fp.readlines()]
    input = []
    for line in lines:
        input += line[:]

total = 0
current = 0
for c in input:
    if c == ',':
        total += current
        current = 0
        continue
    current += ord(c)
    current *= 17
    current %= 256
total += current

print(total)
