import sys
from collections import deque


def insert_markers(array, row_marker, col_marker):
    # Insert horizontal markers
    with_horizontal_markers = []
    for row in array:
        with_horizontal_markers.append(row)
        with_horizontal_markers.append(row_marker * len(row))  # Row of horizontal markers

    # Insert vertical markers
    with_vertical_markers = []
    for row in with_horizontal_markers:
        new_row = col_marker.join(row)
        with_vertical_markers.append(list(new_row))

    return with_vertical_markers


with open('./day10/input.txt', 'r') as fp:
    field = [list(line.strip()) for line in fp.readlines()]


directions = {"S": [(0, 1), (1, 0), (0, -1), (-1, 0)], '.': [], 'F': [(0, 1), (1, 0)], '7': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)], 'L': [(-1, 0), (0, 1)], '-': [(0, 1), (0, -1)], '|': [(1, 0), (-1, 0)]}


field = insert_markers(field, "|", "-")

for r in range(len(field)):
    for c in range(len(field[0])):
        if field[r][c] == "S":
            break
    if field[r][c] == "S":
        break

field[r][c] = '|'

q = deque()
seen = set()
seen.add((r, c))
q.append((r, c, 0))

max_depth = 0
while q:
    r, c, curr_depth = q.popleft()
    # temp = field[r][c]
    # field[r][c] = '#'
    # for row in field:
    #     print(row)
    # print('\n')
    # field[r][c] = temp
    max_depth = max(curr_depth, max_depth)
    for dy, dx in directions[field[r][c]]:
        r += dy
        c += dx
        if r >= 0 and c >= 0 and r < len(field) and c < len(field[0]) and field[r][c] != '.' and (r, c) not in seen:
            q.append((r, c, curr_depth + 1))
            seen.add((r, c))
        r -= dy
        c -= dx

print(max_depth)


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
                field[r][c] = 'I'  # Mark inside areas

new_recursion_limit =  len(field) * len(field[0])
sys.setrecursionlimit(new_recursion_limit)

loop_coords = seen
mark_inside_outside(field, loop_coords)

# Print the marked field
count = 0
for j, row in enumerate(field):
    for i, c in enumerate(row):
        if c == "I" and i % 2 == 0 and j % 2 == 0:
            count += 1
    # print(''.join(row))
print(count)