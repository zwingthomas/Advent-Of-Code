import math
class Checksum():

    def __init__(self, input):
        with open(input, 'r') as fp:
            self.input = [list(line.strip()) for line in fp.readlines()]
        self.modified_input = [[] for _ in range(len(self.input))]
        self.mutate_lines()
        self.checksum = 0
        self.calculate_checksum()

    def mutate_lines(self):

        for i, s in enumerate(self.input):
            ret = []
            front_ptr, back_ptr = 0, len(s) - 1
            while front_ptr <= back_ptr:
                s[back_ptr] = int(s[back_ptr])
                s[front_ptr] = int(s[front_ptr])
                # Write the values dictated by the front
                if front_ptr % 2 == 0:
                    ret += [(front_ptr // 2) for _ in range(s[front_ptr])]
                    front_ptr += 1
                # Free space in the front, write from the back
                else:
                    # Empty space doesn't matter on the back, so just skip over it
                    if back_ptr % 2 == 1:
                        back_ptr -= 1
                        s[back_ptr] = int(s[back_ptr])
                    # Add as many from the back as will fit
                    ret += [(back_ptr // 2) for _ in range(min(s[back_ptr], s[front_ptr]))]
                    # They take up space in the front, and similarily there will be fewer indexes to write from the back
                    s[back_ptr], s[front_ptr] = s[back_ptr] - s[front_ptr], s[front_ptr] - s[back_ptr]
                    if s[back_ptr] == 0:
                        back_ptr -= 1
                        front_ptr += 1
                    elif s[back_ptr] > 0:
                        front_ptr += 1
                    elif s[back_ptr] < 0:
                        back_ptr -= 1
            self.modified_input[i] = ret
        
    def calculate_checksum(self):
        for s in self.modified_input:
            for i, num in enumerate(s):
                self.checksum += num * i

if __name__ == "__main__":
    print(Checksum('./2024/9/input.txt').checksum)

