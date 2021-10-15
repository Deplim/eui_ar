#프로그래머스 | 더 맵게 : (https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import heapq

print("k")
def solution(scoville, K):
    current=[]
    
    for i in scoville:
        heapq.heappush(current, i)
    
    answer = 0
    while 1:
        if current[0]>=K:
            return answer
        if len(current)==1:
            return -1
        target1=heapq.heappop(current)
        target2=heapq.heappop(current)
        heapq.heappush(current, target1+2*target2)
        answer=answer+1  
           
    return answer