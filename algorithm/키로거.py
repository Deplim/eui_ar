# 백준 | 키로거 : (https://www.acmicpc.net/problem/5397)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(inputs):
    Answer = []
    for input in inputs:
        Answer.append(solve(input))
    return Answer


def solve(input):
    left = []
    right = []

    for i in input:
        if i == "<":
            if len(left) != 0:
                right.append(left.pop())
        elif i == ">":
            if len(right) != 0:
                left.append(right.pop())
        elif i == "-":
            if len(left) != 0:
                left.pop()
        else:
            left.append(i)

    return "".join(left + list(reversed(right)))


n = int(input())
inputs = []
for i in range(n):
    inputs.append(input())

Answer = solution(inputs)
for i in Answer:
    print(i)
