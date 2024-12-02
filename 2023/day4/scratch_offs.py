from collections import deque

with open('./day4/input.txt', 'r') as fp:
    lines = [line.strip() for line in fp.readlines()]

total = 0
number_of_copies = deque([])
number_of_copies.append(0)
total_cards = 0
for line in lines:
    if number_of_copies:
        curr_copies = number_of_copies.popleft() + 1
    else:
        curr_copies = 1
    total_cards += curr_copies
    line = line.split(": ")[1]
    winning_nums, nums = line.split(" | ")
    winning_nums = set(winning_nums.split(" "))
    winning_nums = [num for num in winning_nums if num != ""]
    nums = nums.split(" ")
    nums = [num for num in nums if num != ""]
    i = 0
    for num in nums:
        if num in winning_nums:
            if i < len(number_of_copies):
                number_of_copies[i] += curr_copies
            else:
                number_of_copies.append(curr_copies)
            i += 1
for num in number_of_copies:
    total_cards += num
print(total_cards)
    