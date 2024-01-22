directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

with open('./day18/input.txt', 'r') as fp:
    lines = fp.readlines()
    steps = []
    for line in lines:
        line = line.split(' ')
        steps.append((directions[line[0]], int(line[1])))

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

seen = set()
for r, c in stack:
    seen.add((r, c))

grid = [['.' for _ in range(max_c + 1)] for _ in range(max_r + 1)]
for r, c in stack:
    grid[r][c] = '#'

def flood_fill(field, start_r, start_c):
    """ Perform flood-fill algorithm to mark areas outside the loop iteratively. """
    global seen
    stack = [(start_r, start_c)]

    while stack:
        r, c = stack.pop()
        if r < 0 or r >= len(field) or c < 0 or c >= len(field[0]) or (r, c) in seen:
            continue

        seen.add((r, c))
        field[r][c] = "O"

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dy, dx in directions:
            stack.append((r + dy, c + dx))
    
    return field


def mark_inside_outside(field, loop_coords):

    # Flood fill from the edges to mark the outside area
    for r in range(len(field)):
        field = flood_fill(field, r, 0)
        field = flood_fill(field, r, len(field[0]) - 1)
    for c in range(len(field[0])):
        field = flood_fill(field, 0, c)
        field = flood_fill(field, len(field) - 1, c)

    # Mark the inside area
    for r in range(len(field)):
        for c in range(len(field[0])):
            if (r, c) not in loop_coords and field[r][c] != "O":
                field[r][c] = 'I'

mark_inside_outside(grid, seen)


count = 0
for j, row in enumerate(grid):
    for i, c in enumerate(row):
        if c == "I" or c == "#":
            count += 1
    print(''.join(row))
print(count)


