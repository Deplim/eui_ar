#프로그래머스 | N으로 표현 : (https://programmers.co.kr/learn/courses/30/lessons/42895)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import numpy as np

def solution(N, number):
    storage = {}
    storage[1] = [N]
    if number == N: 
        return 1
    
    for i in range(2, 9):
        cont = int(str(N)*i)   

        cases = []
        for j in range(1, i):
            temp = np.array([[[a+b, a-b, a*b, a//b if b!=0 else None] for b in storage[i-j]] for a in storage[j]])
            cases += temp.reshape(-1,).tolist()
        cases = list(set(cases)) + [cont]
        
        if None in cases:
            cases.remove(None)

        if number in cases:
            return i

        storage[i] = cases
        if number in cases:
            return i
    return -1
