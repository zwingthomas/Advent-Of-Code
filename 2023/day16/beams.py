import copy
import sys

dirs = {"up": (0, 1), "down": (0, -1), "right": (1, 0), "left": (-1, 0)}

def recurse(r, c, dx, dy, seen, seen_twice):

    if r < 0 or r >= len(field) or c < 0 or c >= len(field[0]):
        return

    if (r, c) in seen_twice:
        return
    elif (r, c) in seen:
        seen_twice.add((r, c))
    else:
        seen.add((r, c))

    global set_energized
    set_energized.add((r, c))

    if field[r][c] == '/':
        dx, dy = -dy, -dx
        recurse(r + dy, c + dx, dx, dy, seen, seen_twice)
    elif field[r][c] == '\\':
        dx, dy = dy, dx
        recurse(r + dy, c + dx, dx, dy, seen, seen_twice)
    elif field[r][c] == '|' and abs(dx):
        recurse(r + 1, c, 0, 1, seen, copy.deepcopy(seen_twice))
        recurse(r - 1, c, 0, -1, seen, seen_twice)
    elif field[r][c] == '-' and abs(dy):
        recurse(r, c - 1, -1, 0, seen, copy.deepcopy(seen_twice))
        recurse(r, c + 1, 1, 0, seen, seen_twice)
    else:
        recurse(r + dy, c + dx, dx, dy, seen, seen_twice)

with open('./day16/input.txt', 'r') as fp:
    field = [list(line.strip()) for line in fp.readlines()]

new_recursion_limit =  len(field) * len(field[0])
sys.setrecursionlimit(new_recursion_limit)

count = 0
length_set_energized = 0
set_energized = set()
max_energized = 0

for r in range(len(field)):
    seen = set()
    seen_twice = set()
    recurse(r, 0, 1, 0, seen, seen_twice)
    max_energized = max(len(set_energized), max_energized)
    set_energized = set()
    print("r, 0: " + str(r))
for c in range(len(field[0])):
    recurse(0, c, 0, 1, set(), set())
    max_energized = max(len(set_energized), max_energized)
    set_energized = set()
    print("0, c: " + str(c))
for r in range(len(field)):
    recurse(r, len(field[0]) - 1, -1, 0, set(), set())
    max_energized = max(len(set_energized), max_energized)
    set_energized = set()
    print("r, len(field[0]) - 1: " + str(r))
for c in range(len(field[0])):
    recurse(len(field) - 1, c, 0, -1, set(), set())
    max_energized = max(len(set_energized), max_energized)
    set_energized = set()
    print("len(field) - 1, c: " + str(c))


print(max_energized)



        