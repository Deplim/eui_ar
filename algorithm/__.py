import math
import heapq


def solution(board):
    n = len(board)

    visit = [[[math.inf for _ in range(4)]
              for _ in range(n)] for _ in range(n)]
    queue = []
    heapq.heappush(queue, (0, 0, 0, -1))

    for i in range(4):
        visit[i][0][0] = 0

    while queue:
        cost, y, x, d = heapq.heappop(queue)

        neighbors = [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]
        for nd, (ny, nx) in enumerate(neighbors):
            n_cost = cost + (100 if d == nd or d == -1 else 600)

            if (nd+2) % 4 == d:
                continue

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if board[ny][nx]:
                continue

            if visit[nd][ny][nx] > n_cost:
                visit[nd][ny][nx] = n_cost
                heapq.heappush(queue, (n_cost, ny, nx, nd))

    return visit[n-1][n-1]
