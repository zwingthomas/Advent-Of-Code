
with open('./day11/input.txt', 'r') as fp:
    matrix = [list(line.strip()) for line in fp.readlines()]

expanded_rows = set()
for i, row in enumerate(matrix):
    if '#' not in row:
        expanded_rows.add(i)
galaxies = []
expanded_cols = set()
for i, c in enumerate(range(len(matrix[0]))):
    galaxy_found = False
    for r in range(len(matrix)):
        if matrix[r][c] == '#':
            galaxy_found = True
            galaxies.append([r, c])
    if not galaxy_found:
        expanded_cols.add(c)

for galaxy in galaxies:
    print(galaxy)

print("__________")

i = 0
offset = 0
for c in range(len(matrix[0])):
    if c in expanded_cols:
        offset += 999999
    while i < len(galaxies) and galaxies[i][1] == c:
        galaxies[i][1] += offset
        i += 1

galaxies.sort()
i = 0
offset = 0
for r in range(len(matrix)):
    if r in expanded_rows:
        offset += 999999
    while i < len(galaxies) and galaxies[i][0] == r:
        galaxies[i][0] += offset
        i += 1

# get pairs
total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        distance = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        total += distance
print(total)