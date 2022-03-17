# 백준 | 키로거 : (https://www.acmicpc.net/problem/5397)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        left = self.left.value if self.left is not None else "None"
        value = self.value
        right = self.right.value if self.right is not None else "None"
        return left + " " + value + " " + right


def solution(inputs):
    Answer = []
    for input in inputs:
        Answer.append(solve(input))
    return Answer


def solve(input):
    password = ""
    pointer = None
    first_flag = False

    for i in input:
        if i == "<":
            if pointer is not None:
                if pointer.left is not None:
                    pointer = pointer.left
                elif first_flag is False:
                    first_flag = True
        elif i == ">":
            if pointer is not None:
                if pointer.right is not None:
                    pointer = pointer.right
                elif first_flag is True:
                    first_flag = False
        elif i == "-":
            if pointer is None or first_flag:
                pass
            elif pointer.left is None and pointer.right is None:
                pointer = None
            elif pointer.left is None:
                pointer = pointer.right
                pointer.left = None
                first_flag = True
            else:
                pointer.left.right = pointer.right
                if pointer.right is not None:
                    pointer.right.left = pointer.left
                pointer = pointer.left
        else:
            new_node = Node(i)
            if pointer == None:
                pointer = new_node
            elif first_flag:
                new_node.right = pointer
                pointer.left = new_node
                first_flag = False
                pointer = new_node
            else:
                new_node.left = pointer
                if pointer.right is not None:
                    pointer.right.left = new_node
                    new_node.right = pointer.right
                pointer.right = new_node
                pointer = new_node
        #print("("+i+")", pointer, first_flag)

    if pointer is not None:
        while pointer.left is not None:
            pointer = pointer.left
        password += pointer.value
        while pointer.right is not None:
            pointer = pointer.right
            password += pointer.value
    return password


n = int(input())
inputs = []
for i in range(n):
    inputs.append(input())

Answer = solution(inputs)
for i in Answer:
    print(i)
