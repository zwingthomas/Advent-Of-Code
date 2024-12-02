with open('./day9/input.txt', 'r') as fp:
    lines = [[int(item) for item in line.strip().split(" ")] for line in fp.readlines()]
total = 0
for data in lines:
    build = [data]
    not_all_zeros = True
    while not_all_zeros:
        not_all_zeros = False
        build.append([])
        print("Casacde")
        print(build)
        for i in range(len(build[-2]) - 1):
            next = build[-2][i] - build[-2][i + 1]
            if next != 0:
                not_all_zeros = True
            build[-1].append(build[-2][i + 1] - build[-2][i])
    for i in reversed(range(len(build) - 1)):
        build[i].append(build[i][0] - build[i + 1][-1])
    total += build[0][-1]
    print(build)
print(total)