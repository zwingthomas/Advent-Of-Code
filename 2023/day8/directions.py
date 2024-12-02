from collections import deque
import math


with open("./day8/input.txt", "r") as fp:
    lines = fp.readlines()
    directions = list(lines[0].strip())
    lines = lines[2:]
    hm = {}
    for line in lines:
        node, _, left, right = line.split(" ")
        left = left[1:-1]
        right = right.strip()
        right = right[:-1]
        hm[node] = [left, right]

i = 0
n = len(directions)
q = deque([])
for key in hm:
    if key[-1] == "A":
        q.append((key, key, 0))

numZs = 0
print(q)
visitedZs = set()
found = []
while len(q) != numZs:
    curr, key, steps = q.popleft()
    if curr[-1] == "Z":
        numZs -= 1
    if directions[steps % n] == 'L':
        curr = hm[curr][0]
    elif directions[steps % n] == 'R':
        curr = hm[curr][1]
    else:
        print("Broken")
    if curr[-1] == "Z" and curr not in visitedZs:
        visitedZs.add(curr)
        found.append((curr, key, steps + 1))
        if len(visitedZs) == len(q) + 1:
            print(found)
            break
    q.append((curr, key, steps + 1))
    print(q)

steps = [item[2] for item in found]
def lcm_of_two_numbers(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_of_six_numbers(nums):
    lcm = lcm_of_two_numbers(nums[0], nums[1])
    for i in range(2, len(nums)):
        lcm = lcm_of_two_numbers(lcm, nums[i])
    return lcm

print(lcm_of_six_numbers(steps))

# total = 0
# while q:
#     _, steps = q.popleft()
#     total += steps
#print(total - 1)
