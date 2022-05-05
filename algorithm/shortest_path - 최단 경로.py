# 백준 | 덩치 : (https://www.acmicpc.net/problem/7568)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import heapq
import math
import sys


def solution(v, e, k, inputs):
    G = [{} for i in range(v+1)]
    for a, b, c in inputs:
        if b not in G[a]:
            G[a][b] = c
        if b in G[a] and G[a][b] > c:
            G[a][b] = c

    queue = []
    visit = [math.inf]*(v+1)
    visit[k] = 0
    heapq.heappush(queue, (0, k))

    while queue:
        cost, point = heapq.heappop(queue)

        if visit[point] < cost:
            continue

        for next_point in G[point]:
            if (cost+G[point][next_point]) < visit[next_point]:
                visit[next_point] = cost+G[point][next_point]
                heapq.heappush(queue, (cost+G[point][next_point], next_point))

    return visit[1:]


v, e = tuple(map(int, input().split(' ')))
k = int(input())
inputs = []
for i in range(e):
    inputs.append(tuple(map(int, sys.stdin.readline().split(' '))))

Answer = list(map(str, solution(v, e, k, inputs)))
for i, v in enumerate(Answer):
    if v == 'inf':
        Answer[i] = 'INF'
print('\n'.join(Answer))
