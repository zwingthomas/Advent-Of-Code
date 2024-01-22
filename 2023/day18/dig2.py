import re

dirs = {"0": 'R', "1": 'D', "2": 'L', "3": 'U'}
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

with open('./day18/input.txt', 'r') as fp:
    lines = fp.readlines()
    steps = []
    for line in lines:
        line = re.search(r'\((.*?)\)', line).group(1)[1:]
        direction = directions[dirs[line[-1:]]]
        line = line[:-1]
        steps.append([direction, int(line, 16)])
    print(lines)

seen = set()
curr = [0, 0]
stack = [curr]
min_r = min_c = 0
for direction, repeat in steps:
    dy, dx = direction
    for _ in range(repeat):
        nr = curr[0] + dy
        nc = curr[1] + dx
        min_r = min(min_r, nr)
        min_c = min(min_c, nc)
        curr = [nr, nc]
        stack.append(curr)

max_r = 0
max_c = 0
for i in range(len(stack)):
    r, c = stack[i]
    r += abs(min_r)
    c += abs(min_c)
    max_r = max(max_r, r)
    max_c = max(max_c, c)
    stack[i] = [r, c]

print("Reorganized stack")

seen = set()
for r, c in stack:
    seen.add((r, c))

print(max_r)
print(max_c)
map_grid = {}
# grid = [['.' for _ in range(max_c + 1)] for _ in range(max_r + 1)]
for r, c in stack:
    seen.add((r,c))
    map_grid[str(r) + "x" + str(c)] = '#'

edges = len(seen)

print("Made Grid")
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def flood_fill(field, start_r, start_c, max_r, max_c):
    """ Perform flood-fill algorithm to mark areas outside the loop iteratively. """

    stack = [(start_r, start_c)]
    global seen
    while stack:
        print(len(stack))
        r, c = stack.pop()
        if r < 0 or r >= max_r or c < 0 or c >= max_c or (r, c) in seen:
            continue

        seen.add((r, c))

        
        for dy, dx in directions:
            new_r = r + dy
            new_c = c + dx
            if not (new_r, new_c) in seen and new_r >= 0 and new_r < max_r and new_c >= 0 and new_c < max_c:
                stack.append((new_c, new_r))
    
    return field


def mark_inside_outside(field, max_r, max_c):

    # Flood fill from the edges to mark the outside area
    for r in range(max_r):
        field = flood_fill(field, r, 0, max_r, max_c)
        field = flood_fill(field, r, max_c, max_r, max_c - 1)
        print(r)
    for c in range(max_c):
        field = flood_fill(field, 0, c, max_r, max_c)
        field = flood_fill(field, max_r - 1, c, max_r, max_c)
        print(c)
mark_inside_outside(map_grid, max_r, max_c)
print("Marked")



print(max_r * max_c - len(seen) + edges)
