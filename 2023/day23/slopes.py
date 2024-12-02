import copy

with open('./day23/input.txt', 'r') as fp:
    slopes = [list(line) for line in fp.readlines()]


directions = {".": [(0, 1), (1, 0), (0, -1), (-1, 0)], ">": [(0, 1)], "<": [(0, -1)], "v": [(1, 0)], "^": [(-1, 0)], "#": []}
stack = [(0, 1, 0, {(0, 1)})]
step_count = 0
while stack:
    r, c, steps, seen = stack.pop()
    step_count = max(steps, step_count)
    for dx, dy in directions[slopes[r][c]]:
        nr, nc = r + dx, c + dy
        if 0 <= nr < len(slopes) and 0 <= nc < len(slopes[0]) and (nr, nc) not in seen and slopes[nr][nc] != "#":
            seen.add((nr, nc))
            stack.append((nr, nc, steps + 1, copy.deepcopy(seen)))
print(step_count)

