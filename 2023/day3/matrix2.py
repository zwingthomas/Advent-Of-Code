from collections import defaultdict

def search_around(r, c, matrix):
    directions = [(1, 1), (-1, -1), (-1, 1), (1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    number = 0
    if matrix[r][c].isdigit():
        for dx, dy in directions:
            if r + dx < len(matrix) and r + dx >= 0 and c + dy < len(matrix[r]) and c + dy >= 0 and matrix[r + dx][c + dy] != "." and not matrix[r + dx][c + dy].isdigit():
                # found a part, now find the number of that part
                temp = c
                while c >= 0 and matrix[r][c].isdigit():
                    c -= 1
                number = ""
                c += 1
                while c < len(matrix[r]) and matrix[r][c].isdigit():
                    number += matrix[r][c]
                    c += 1
                c -= 1
                number = int(number)
                return c, number, matrix[r + dx][temp + dy], r + dx, temp + dy
    # return end of number (to not double count), and part number
    return c, 0, "?", 0, 0
            

with open('./day3/input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file.readlines()]

r = c = 0
sum_part_number = 0
ratios = defaultdict(list)
while r < len(matrix):
    while c < len(matrix[r]):
        next_c, part_number, symbol, symbol_r, symbol_c = search_around(r, c, matrix)
        print(symbol)
        if symbol == "*":
            print("found")
            ratios[str((symbol_r, symbol_c))].append(part_number)
        c = next_c + 1
    c = 0
    r += 1
total = 0
print(ratios)
for key in ratios:
    if len(ratios[key]) == 2:
        total += ratios[key][0] * ratios[key][1]

print(total)
