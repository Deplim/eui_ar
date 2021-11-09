#프로그래머스 | 디스크 컨트롤러 : (https://programmers.co.kr/learn/courses/30/lessons/42627)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# solution2 -> solution : jobs 에서 아이템을 가져올 때, pop(0) 이 아닌 pop() 을 가져오도록 변경 (대신 sort reverse)
# 다만 실행시간에 그렇게 영향은 없음. 애초에 최적화가 필요한 문제가 아님.

import heapq
import math

def solution(jobs):
    target=[] # 대기중인 작업 대상
    time=0 # 현제 시간
    current=0 # 현제 작업중인 대상
    answer=0 # 작업의 요청부터 종료까지 시간의 합
    job_length=len(jobs) # jobs 에서 pop 할 것이므로, length 따로 저장.
    
    jobs.sort(key=lambda x: x[0], reverse = True)
    jobs=list(map(lambda x:(x[1], x[0]), jobs)) #job 입력시간과 걸리는시간 위치 바꿔주기. (heap 에 넣기 위해서)
    
    while 1:
        while 1:
            if len(jobs)!=0 and jobs[-1][1]<=time: # 들어온 작업이 있는 경우
                heapq.heappush(target, jobs.pop())
            else:
                break
        
        if current!=0: # 작업한 대상이 있는 경우
            answer=answer+(time-current[1])
            current=0
        
        if len(target)==0: # 대기중인 작업이 없는경우
            if len(jobs)==0: # 끝
                break 
            else: # 다음 작업이 들어오는 시간으로 점프
                time=jobs[-1][1]
                continue
        else: # 대기중인 작업이 있는경우
            current=heapq.heappop(target)
            time=time+current[0] # time 을 1씩 늘리는게 아니라 current 단위로 더하고 그 사이에 들어온 작업이 있는지 본다.
            
    answer=math.floor(answer/job_length)
    return answer


'''
def solution2(jobs):
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
'''