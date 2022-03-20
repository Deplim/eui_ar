# 프로그래머스 | 01 타일 : (https://www.acmicpc.net/problem/1904)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(n):
    DP = [1, 1] + [0]*(n-1)
    for i in range(2, n+1):
        DP[i] = (DP[i-1] + DP[i-2]) % 15746
    return DP[n]


input = int(input())
Answer = solution(input)
print(Answer)
