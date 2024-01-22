from collections import defaultdict

def tilt_platform_up(platform):
    for c in range(len(platform[0])):
        for r in range(len(platform)):
            if platform[r][c] == 'O':
                r -= 1
                while platform[r][c] == '.':
                    platform[r][c] = 'O'
                    platform[r + 1][c] = '.'
                    r -= 1
    return platform

def tilt_platform_left(platform):
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == 'O':
                c -= 1
                while platform[r][c] == '.':
                    platform[r][c] = 'O'
                    platform[r][c + 1] = '.'
                    c -= 1
    return platform

def tilt_platform_down(platform):
    for c in range(len(platform[0])):
        for r in reversed(range(len(platform))):
            if platform[r][c] == 'O':
                r += 1
                while platform[r][c] == '.':
                    platform[r][c] = 'O'
                    platform[r - 1][c] = '.'
                    r += 1
    return platform

def tilt_platform_right(platform):
    for r in range(len(platform)):
        for c in reversed(range(len(platform[0]))):
            if platform[r][c] == 'O':
                c += 1
                while platform[r][c] == '.':
                    platform[r][c] = 'O'
                    platform[r][c - 1] = '.'
                    c += 1
    return platform


with open('./day14/input.txt', 'r') as fp:
    platform = [['#'] + list(line.strip()) + ['#'] for line in fp.readlines()]
    blockers = ['#' for _ in range(len(platform[0]))]
    platform = [blockers] + platform + [blockers]
for row in platform:
        print(row)
print("____________________")
hm = defaultdict(list)

for x in range(155):
    platform = tilt_platform_up(platform)
    platform = tilt_platform_left(platform)
    platform = tilt_platform_down(platform)
    platform = tilt_platform_right(platform)
    h = ""
    for row in platform:
        h += str(row)
    hm[h].append(x)
    for key in hm:
        print(hm[key])
    print(len(hm))
for row in platform:
        print(row)
print("Different")
difference = (1000000000 - 94) % 65 + 94
print(difference)
for i in range(94, 159):
    print(str(i) + "   " + str((1000000000 - i) % 65))
score = 0
for r in range(len(platform)):
     for c in range(len(platform[0])):
          if platform[r][c] == "O":
               score += len(platform) - r - 1
print(score)