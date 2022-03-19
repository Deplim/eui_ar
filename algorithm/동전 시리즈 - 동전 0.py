# 백준 | 동전 0 : (https://www.acmicpc.net/problem/11047)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(target, input_):
    Answer = 0
    input_.reverse()
    for v in input_:
        if target >= v:
            quotient = target//v
            target = target - v*(quotient)
            Answer += (quotient)
        if target == 0:
            return Answer


n, target = tuple(map(int, input().split(' ')))
input_ = []
for i in range(n):
    input_.append(int(input()))

Answer = solution(target, input_)
print(Answer)
