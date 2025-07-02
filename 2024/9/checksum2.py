from bisect import bisect_left

class NoFragmentation():

    def __init__(self, input):
        with open(input, 'r') as fp:
            self.input = ''.join([int(_) for _ in fp.readline()])
        self.modified_input = []
        self.mutate_input()
    

    def mutate_input(self):

        gaps = []
        data = []
        for i, num in enumerate(self.input):
            if num % 2 == 0: # contiguous data
                data.append((i // 2, num))
            else: # free space
                gaps.append((num, i))
        
        gaps = sorted(gaps)

        while data:
            i = len(gaps)
            while gaps[i][0] 
            gaps[i] = (gaps[i][0] - data[1], )











if __name__ == "__main__":
    print(NoFragmentation('./2024/9/test_input.txt'))
