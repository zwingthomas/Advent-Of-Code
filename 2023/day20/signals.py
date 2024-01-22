import math
from collections import defaultdict, deque

with open('./day20/input.txt', 'r') as fp:
    lines = fp.readlines()
    types = {}
    mappings = defaultdict(list)
    for line in lines:
        line = line.strip()
        first, second = line.split(' -> ')
        if first != 'broadcaster':
            name = first[1:]
            types[name] = first[:1]
        else:
            name = first
        for next_signal in second.split(', '):
            mappings[name].append(next_signal)
    
    flipflops = {}
    conjunctions = defaultdict(dict)
    for module in types:
        if types[module] == '&':
            for input in mappings:
                print(input)
                for output in mappings[input]:
                    print(output)
                    if output == module:
                        conjunctions[module][input] = 0
        if types[module] == '%':
            flipflops[module] = 0
    
    print(conjunctions)
    print(flipflops)

high_count = 0
low_count = 0
for i in range(1000):
    q = deque()
    low_count += 1
    for broadcast in mappings['broadcaster']:
        q.append((broadcast, "broadcaster", 0))
    
    while q:
        curr, prev, signal = q.popleft()
        # print(f"Curr: {curr} Prev: {prev}, Signal: {signal}")
        if signal == 1:
            high_count += 1
        else:
            low_count += 1
        if curr in conjunctions:
            conjunctions[curr][prev] = signal
            if curr == "hj" and signal == 1:
                print(f"Button Presses: {i + 1}   hj: {conjunctions[curr]}")
            all_high = 0
            for s in conjunctions[curr]:
                if conjunctions[curr][s] == 0:
                    all_high = 1
                    break
            for nxt in mappings[curr]:
                q.append((nxt, curr, all_high))
        if curr in flipflops:
            if signal == 1:
                continue
            if flipflops[curr] == 1:
                flipflops[curr] = 0
                for nxt in mappings[curr]:
                    q.append((nxt, curr, 0))
            else:
                flipflops[curr] = 1
                for nxt in mappings[curr]:
                    q.append((nxt, curr, 1))
        if curr == 'broadcaster':
            for nxt in mappings[curr]:
                q.append((nxt, curr, signal))

print(low_count)
print(high_count)
print(high_count * low_count)
print(math.lcm(3889, 3911, 3947, 4013))
