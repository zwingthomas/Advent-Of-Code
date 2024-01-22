import re
with open('./day19/input.txt', 'r') as fp:
    lines = fp.readlines()
    workflows = {}
    parts = []
    in_parts = False
    for line in lines:
        if line == '\n':
            in_parts = True
            continue
        if in_parts:
            hm = {}
            line = re.split("[,}{]", line.strip())
            for spec in line:
                if '=' in spec:
                    spec = spec.split('=')
                    hm[spec[0]] = spec[1]
            parts.append(hm)
            continue
        line = re.split("[,}{]", line.strip())
        workflows[line[0]] = [_ for _ in line[1:-1]]
    for key in workflows:
        for i, path in enumerate(workflows[key]):
            if ':' in path:
                flow = workflows[key][i].split(':')
                workflows[key][i] = {flow[0]: flow[1]}

total = 0
for part in parts:
    curr = 'in'
    while curr in workflows:
        for i, steps in enumerate(workflows[curr]):
            b = False
            for step in steps:
                print(i)
                print(workflows[curr])
                if i == len(workflows[curr]) - 1:
                    curr = workflows[curr][i]
                    b = True
                    break
                elif '>' in step:
                    if int(part[step[:1]]) > int(step.split('>')[1]):
                        curr = workflows[curr][i][step]
                        b = True
                        break
                elif '<' in step:
                    if int(part[step[:1]]) < int(step.split('<')[1]):
                        curr = workflows[curr][i][step]
                        b = True
                        break
            if curr == 'A' or curr == 'R' or b:
                break
    if curr == 'A':
        print("Accepted")
        for key in part:
            total += int(part[key])
    else:
        print(curr)

print(total)


