# 백준 | 영화감독 솜 : (https://www.acmicpc.net/problem/1436)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(input):
    count = 0
    num = 666
    while 1:
        if '666' in str(num):
            count += 1
            if count == input:
                return num
        num += 1


input = int(input())
Answer = solution(input)
print(Answer)
