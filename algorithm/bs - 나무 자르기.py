# 백준 | 나무 자르기 : (https://www.acmicpc.net/problem/2805)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import math


def solution(n, m, input_):
    input_.sort()
    total_sum = sum(input_)
    c_sum = 0  # i번 index 까지의 나무들의 길이의 합
    end = 0
    for i, v in enumerate(input_):
        c_sum += v
        # tree_remain 는 v에서 잘랐을때 남는 나무의 길이
        tree_remain = c_sum + (n - (i+1)) * v
        if (total_sum - tree_remain) < m:
            end = v
            break
    target = m-(total_sum - tree_remain)  # end 에서 자를경우 부족한 나무의 길이
    Answer = end - math.ceil(target / (n-i))
    return Answer


n, m = tuple(map(int, input().split(' ')))
inputs = []
input_ = list(map(int, input().split(' ')))

Answer = solution(n, m, input_)
print(Answer)
