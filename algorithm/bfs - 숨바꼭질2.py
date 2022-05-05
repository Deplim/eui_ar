# 백준 | 숨바꼭질 2 : (https://www.acmicpc.net/problem/12851)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(a, b):
    queue = {a: 1}
    visit = set()

    cost = 0
    while queue:
        for key in queue:
            visit.add(key)

        next_queue = {}
        for key in queue:
            target = []
            if key >= 0:
                target.append(key-1)
            if key < b:
                target.extend([key+1, key*2])

            for next_key in target:
                if next_key in visit:
                    continue
                if next_key in next_queue:
                    next_queue[next_key] += queue[key]
                else:
                    next_queue[next_key] = queue[key]
        if b in queue:
            break

        cost += 1
        queue = next_queue

    return cost, queue[b]


a, b = tuple(map(int, input().split(' ')))
Answer = list(map(str, solution(a, b)))
print(' '.join(Answer))
