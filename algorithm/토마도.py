# 백준 | 토마토 : (https://www.acmicpc.net/problem/7576)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

from collections import deque


def solution(h, w, input):
    queue = deque()
    for i, input_row in enumerate(input):
        for j, val in enumerate(input_row):
            if val == 1:
                queue.append((i, j, -1, 0))

    max_day = 0
    while queue:
        y, x, d, day = queue.popleft()

        neighbors = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        for nd, (ny, nx) in enumerate(neighbors):
            if d != -1 and (nd+2) % 4 == d:
                continue

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if input[ny][nx] in [-1, 1]:
                continue

            max_day = max(max_day, day+1)

            input[ny][nx] = 1
            queue.append((ny, nx, nd, day+1))

    for input_row in input:
        for val in input_row:
            if val == 0:
                return -1
    return max_day


w, h = tuple(map(int, input().split(' ')))
inputs = []
for i in range(h):
    inputs.append(list(map(int, input().split(' '))))

Answer = solution(h, w, inputs)
print(Answer)
