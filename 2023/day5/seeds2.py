

def navigate(key, map):
    range = bs(key, map)
    if range == -1:
        return key
    range = map[range]
    return (key - range[1]) + range[0]

def bs(target, array):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_range = array[mid]
        if mid_range[1] <= target < mid_range[1] + mid_range[2]:
            return mid
        elif target < mid_range[1]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


with open('./day5/seeds.txt', 'r') as fp:
    seeds = [int(item.strip()) for item in fp.read().split(" ")]
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
with open('./day5/seeds2soil.txt', 'r') as fp:
    seed2soil = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    seed2soil.sort(key=lambda x: x[1])
with open('./day5/soil2fertilizer.txt', 'r') as fp:
    soil2fert = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    soil2fert.sort(key=lambda x: x[1])
with open('./day5/fertilizer2water.txt', 'r') as fp:
    fert2water = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    fert2water.sort(key=lambda x: x[1])
with open('./day5/water2light.txt', 'r') as fp:
    water2light = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    water2light.sort(key=lambda x: x[1])
with open('./day5/light2tempurature.txt', 'r') as fp:
    light2temp = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    light2temp.sort(key=lambda x: x[1])
with open('./day5/temp2humidity.txt', 'r') as fp:
    temp2humid = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    temp2humid.sort(key=lambda x: x[1])
with open('./day5/humidity2location.txt', 'r') as fp:
    humid2loc = [[int(item.strip()) for item in line.split(" ")] for line in fp.readlines()]
    humid2loc.sort(key=lambda x: x[1])

min_loc = float('inf')
print(len(seeds))
counter = 1
for seedStart, seedLen in seeds:
    for x in range(seedStart, seedStart + seedLen):
        soil = navigate(x, seed2soil)
        fert = navigate(soil, soil2fert)
        water = navigate(fert, fert2water)
        light = navigate(water, water2light)
        temp = navigate(light, light2temp)
        humid = navigate(temp, temp2humid)
        loc = navigate(humid, humid2loc)
        min_loc = min(loc, min_loc)
        print(str(counter) + " Loading: " + str(x))
    counter += 1
print(min_loc)




