from functools import cache

def fitsHere(i, j):
    global spring_map
    global guide

    counter = 0
    while i < len(spring_map) and (spring_map[i] == "?" or spring_map[i] == "#") and counter < guide[j]:
        counter += 1
        i += 1
    if counter == guide[j] and (i == len(spring_map) or spring_map[i] != "#"):
        return True
    else:
        return False

@cache
def dp(i, j, placed, run):
    global spring_map
    global guide
    # completed a good run together
    if i >= len(spring_map) and j >= len(guide):
        return 1
    # completed one before the other, bad arrangement
    elif (i >= len(spring_map) and j < len(guide)) or (spring_map[i] == '#' and j >= len(guide)):
        return 0

    if spring_map[i] == '?':
        if placed or j >= len(guide):
            return dp(i + 1, j, False, run)
        else:
            if fitsHere(i, j):
                return dp(i + guide[j], j + 1, True, run) + dp(i + 1, j, False, run)
            return dp(i + 1, j, False, run)
    elif spring_map[i] == '.':
        return dp(i + 1, j, False, run)
    elif spring_map[i] == "#":
        if fitsHere(i, j):
            return dp(i + guide[j], j + 1, True, run)
        return 0


with open('./day12/input.txt', 'r') as fp:
    springs = [[item.strip().split(',') for item in line.split(" ")] for line in fp.readlines()]

total = 0
run = 0
for spring_map, guide in springs:
    spring_map = [str(x) for x in spring_map[0]]
    spring_map = [item for i in range(5) for item in (spring_map + ["?"] if i < 5 - 1 else spring_map)]
    guide = [int(x) for x in guide] * 5
    arrangements = dp(0, 0, False, run)
    print(arrangements)
    total += arrangements
    run += 1
print(total)