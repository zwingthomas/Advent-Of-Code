from collections import deque

with open('./day21/input.txt', 'r') as fp:
    field = [list(line) for line in fp.readlines()]


for r, row in enumerate(field):
    for c, item in enumerate(row):
        if item == 'S':
            break
    if item == 'S':
        break

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
reachable = set()

for j in range(1, 26501365 + 1, 2):
    q = deque()
    q.append((r, c))
    seen = set((r, c))

    for i in range(j):
        l = len(q)
        for _ in range(l):
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if field[nr % (len(field) - 1)][nc % (len(field[0]) - 1)] != '#' and (nr, nc) not in seen:
                    q.append((nr, nc))
                    seen.add((nr, nc))
    print(j)

    while q:
        cr, cc = q.popleft()
        reachable.add((cr, cc))
    print(len(reachable))
