with open('./day6/input.txt', 'r') as fp:
    lines = fp.readlines()
    times = [int(value) for value in lines[0].split() if value.isdigit()]
    distances = [int(value) for value in lines[1].split() if value.isdigit()]
    races = list(zip(times, distances))

total = 1
for time, record in races:
    winning_range = 0
    for button_press in range(time):
        remaining = time - button_press
        speed = button_press
        if speed * remaining > record:
            winning_range += 1
    total *= winning_range
print(total)
