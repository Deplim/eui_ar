#프로그래머스 | 디스크 컨트롤러 : (https://programmers.co.kr/learn/courses/30/lessons/42627)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import heapq
import math

def solution(jobs):
    target=[] # 대기중인 작업 대상
    time=0 # 현제 시간
    current=0 # 현제 작업중인 대상
    answer=0 
    job_length=len(jobs)
    
    #job 시간순대로 정렬
    jobs=sorted(jobs, key=lambda x: x[0])
    #job 입력시간과 걸리는시간 위치 바꿔주기. (heap 에 넣기 위해서)
    jobs=list(map(lambda x:(x[1], x[0]), jobs))
    
    while 1:
        while 1:
            if len(jobs)==0:
                break
                
            if jobs[0][1]<=time:
                heapq.heappush(target, jobs.pop(0))
            else:
                break
        
        if current!=0:
            answer=answer+(time-current[1])
            current=0
        
        if len(target)==0:
            if len(jobs)==0:
                break
            else:
                time=jobs[0][1]
                continue
        else:
            current=heapq.heappop(target)
            time=time+current[0]
        '''
        print("after:")
        print(jobs)
        print(target)
        print(current)
        print(answer)
        print("--------------------------\n")
        '''
    #print("\n\n\n\n\nanswer:", answer)    
    answer=math.trunc(answer/job_length)
    return answer