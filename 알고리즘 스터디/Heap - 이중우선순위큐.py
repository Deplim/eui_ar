#프로그래머스 | 이중우선순위큐 : (\https://programmers.co.kr/learn/courses/30/lessons/42628)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import heapq

def solution(operations):
    result=[]
    split_o=list(map(lambda x:x.split(" "), operations))
    
    for i in split_o:
        if i[0]=='I':
            result.append(int(i[1]))
        elif i[1]=='1' and len(result)!=0:
            result.remove(max(result))
        elif i[1]=='-1' and len(result)!=0:
            result.remove(min(result))
    
    
    if len(result)==0:
        answer=[0, 0]
    else:
        answer=[max(result), min(result)]
    
    return answer