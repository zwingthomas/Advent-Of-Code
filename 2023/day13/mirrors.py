
def difference(a, b):
    ret = 0
    if len(a) == len(b):
        for i, c in enumerate(a):
            if a[i] != b[i]:
                ret += 1
    else:
        ret = float('inf')
    return ret

def findHorizontalMirrorScore(matrix):
    # options = set([i + 1 for i in range(len(matrix[0]))])
    violations = [0] * len(matrix[0])
    for r in range(len(matrix)):
        stack = []
        curr = matrix[r][:]
        i = len(matrix[r]) - 1
        while curr:
            stack.append(curr.pop())
            if violations[i] <= 1:
                if len(stack) < len(curr):
                    if stack != curr[-len(stack):]:
                        # options.remove(i)
                        violations[i] += difference(stack, curr[-len(stack):])
                elif len(stack) >= len(curr):
                    if stack[-len(curr):] != curr:
                        # options.remove(i)
                        violations[i] += difference(stack[-len(curr):], curr)
            i -= 1
    for i, x in enumerate(violations):
        if x == 1:
            return i

def transposed(matrix):
    new_matrix = []
    for c in range(len(matrix[0])):
        new_matrix.append([])
        for r in range(len(matrix)):
            new_matrix[-1].append(matrix[r][c])
    return new_matrix


with open('./day13/input.txt', 'r') as fp:
    inputs = fp.readlines()
    matrixes = [[]]
    for line in inputs:
        if line != '\n':
            matrixes[-1].append(list(line.strip()))
        else:
            matrixes.append([])
    print(matrixes)

score = 0
for matrix in matrixes:
    horizontal = findHorizontalMirrorScore(matrix)
    if horizontal:
        score += horizontal
    matrix = transposed(matrix)
    vertical = findHorizontalMirrorScore(matrix)
    if vertical:
        score += 100 * vertical
print(score)