# 백준 | 나무 자르기 : (https://www.acmicpc.net/problem/2805)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import math


def solution(n, m, input_):
    input_.sort()
    total_sum = sum(input_)
    c_sum = 0
    end = 0
    for i, v in enumerate(input_):
        c_sum += v
        tree_under = c_sum + (n - (i+1)) * v
        if (total_sum - tree_under) < m:
            end = v
            break
    target = m-(total_sum - tree_under)
    Answer = end - math.ceil(target / (n-i))
    return Answer


n, m = tuple(map(int, input().split(' ')))
inputs = []
input_ = list(map(int, input().split(' ')))

Answer = solution(n, m, input_)
print(Answer)
