
file = open('./day2/input.txt')

lines = file.readlines()

working_sum = 0
for line in lines:
    possible = True
    game_number, draws = line.split(": ")
    hm = {"red": 0, "green": 0, "blue": 0}
    for draw in draws.split("; "):
        for item in draw.split(", "):
            count, match = item.split(" ")
            match = match.strip()
            hm[match] = max(hm[match], int(count))
    power = 1
    for key in hm:
        power *= hm[key] 
    working_sum += int(power)
print(working_sum)