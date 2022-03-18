# 프로그래머스 | 소수 찾기 : (https://programmers.co.kr/learn/courses/30/lessons/42839)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)


from itertools import permutations


def solution(numbers):
    Answer = 0
    permut = []
    for i in range(len(numbers)):
        permut += list(permutations(list(numbers), i+1))
    permut_set = set([int(''.join(item)) for item in permut])
    permut_set.discard(0)
    permut_set.discard(1)
    # print(permut_set)

    for item in permut_set:
        if if_prime(item):
            # print(item)
            Answer += 1
    return Answer


def if_prime(n):
    root_n = n**(1/2)
    c_num = 2
    while c_num <= root_n:
        if n % c_num == 0:
            return False
        c_num += 1
    return True
