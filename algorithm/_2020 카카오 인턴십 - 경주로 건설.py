# 프로그래머스 | 경주로 건설 : (https://programmers.co.kr/learn/courses/30/lessons/67259)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# 이 문제는 코드를 깔끔하게 짤 방법이 떠오르지 않아 다른 사람의 풀이를 참고함
# https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B2%BD%EC%A3%BC%EB%A1%9C-%EA%B1%B4%EC%84%A4-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-BFS

# 위의 코드를 그대로 쓰면 마지막 테스트 케이스에서 오류 발생.
# 단순히 기존의 cost 보다 작을때만 visit 한다고 하면 방향이 같을때 얻을 수 있는 이득을 계산하지 못하기 때문
# ->> 따라서 기존의 cost+500 보다 작을 때 queue 에 넣을 수 있도록 변경함
# (단, 각 노드의 최소 cost를 바꾸는 것은 기존 cost 보다 작을 때만)

import math
from collections import deque
import heapq


def solution(board):
    n = len(board)

    visit = [[[math.inf for _ in range(4)]
              for _ in range(n)] for _ in range(n)]
    queue = []
    heapq.heappush(queue, (0, 0, 0, -1))  # cost, y, x, direciton

    for i in range(4):
        visit[0][0][i] = 0

    while queue:
        cost, y, x, d = heapq.heappop(queue)

        neighbors = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        for nd, (ny, nx) in enumerate(neighbors):
            n_cost = cost + (100 if d == nd or d == -1 else 600)

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if board[ny][nx]:
                continue

            if visit[ny][nx][nd] > n_cost:
                visit[ny][nx][nd] = n_cost
                heapq.heappush(queue, (n_cost, ny, nx, nd))

    return min(visit[n-1][n-1])


def solution2(board):
    n = len(board)

    visit = [[math.inf for _ in range(n)] for _ in range(n)]
    queue = deque([(0, 0, -1, 0)])  # y, x, direction, cost
    visit[0][0] = 0

    while queue:
        y, x, d, cost = queue.popleft()

        neighbors = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        for nd, (ny, nx) in enumerate(neighbors):
            n_cost = cost + (100 if d == nd or d == -1 else 600)

            if (nd+2) % 4 == d:
                continue

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if board[ny][nx]:
                continue

            if visit[ny][nx]+500 <= n_cost:
                continue

            if visit[ny][nx] > n_cost:
                visit[ny][nx] = n_cost
            queue.append((ny, nx, nd, n_cost))

    return visit[n-1][n-1]
