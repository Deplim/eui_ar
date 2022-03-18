# 백준 | 숨바꼭질 2 : (https://www.acmicpc.net/problem/12851)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(a, b):
    queue = {a: 1}
    visit = set()

    cost = 0
    while queue:
        next_queue = {}

        flag = False
        for key in queue:
            if key == b:
                flag = True

            if key in visit:
                continue

            temp = []
            if key >= 0:
                temp.append(key-1)
            if key < b:
                temp.extend([key+1, key*2])

            for next_key in temp:
                if next_key in next_queue:
                    next_queue[next_key] += queue[key]
                else:
                    next_queue[next_key] = queue[key]
        if flag:
            break

        for key in queue:
            visit.add(key)
        cost += 1
        queue = next_queue

    return cost, queue[b]


a, b = tuple(map(int, input().split(' ')))
Answer = list(map(str, solution(a, b)))
print(' '.join(Answer))
