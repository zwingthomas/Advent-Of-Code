class ListNode():
    def __init__(self, val = None, label = None, next = None, prev = None):
        self.val = val
        self.label = label
        self.next = next
        self.prev = prev


def determine_box(sequence):
    current = 0
    chars = ""
    for c in sequence:
        if c == '=' or c == '-':
            break
        current += ord(c)
        current *= 17
        current %= 256
        chars += c
    return current, chars

def remove_node(box, label):
    node = box
    while node.next != None:
        print("HERE")
        print(node.label)
        print(label)
        if node.label == label:
            node.prev.next = node.next
            node.next.prev = node.prev
        node = node.next
    return box

def replace_node(box, label):
    replaced = False
    node = box
    while node and node.next != None:
        if node.label == label:
            node.val = lens[-1]
            replaced = True
            break
        node = node.next
    return box, replaced

def add_node(box, label):
    node = box
    while node.next and node.next.val != None:
        node = node.next
    new_node = ListNode(int(lens[-1]), label, node.next, node)
    node.next = new_node
    return box
    

def print_linked_list(head):
    current = head
    elements = []
    score = 0
    i = 1
    while current:
        if current.val:
            score += i * int(current.val)
            i += 1
        elements.append(str(current.val) + " " + str(current.label))
        current = current.next
    print(" -> ".join(elements))
    return score


with open('./day15/input.txt', 'r') as fp:
    lines = [list(line.strip().split(',')) for line in fp.readlines()]
    input = []
    for line in lines:
        input += line[:]

box_set = set()
boxes = []
for _ in range(256):
    head = ListNode()
    tail = ListNode(None, None, None, head)
    head.next = tail
    boxes.append(head)

total = 0
for lens in input:
    box_num, label = determine_box(lens)
    print(box_num)
    print(lens)
    if '-' in lens:
        # remove node
        boxes[box_num] = remove_node(boxes[box_num], label)
    else:
        # replace node
        boxes[box_num], replaced = replace_node(boxes[box_num], label)
        if not replaced:
            boxes[box_num] = add_node(boxes[box_num], label)
            box_set.add(box_num)

    # for i, box in enumerate(boxes):
    #     if i in box_set:
    #         print(i)
    #         print_linked_list(box)
    #         print("___")
    # print('New Lens\n')

total = 0
for i, box in enumerate(boxes):
    if i in box_set:
        print(i)
        score = print_linked_list(box)
        print("___")
        total += (i + 1) * score
print(total)

