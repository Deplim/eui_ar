#프로그래머스 | 가장 먼 노드 : (https://programmers.co.kr/learn/courses/30/lessons/49189)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# solution2 -> solution : list 대신 deque 사용, visit 를 set 으로 구현
# visit 처리를 queue 에서 값을 꺼낼 때 할지, 연결된 노드를 찾을 때 할지에 따라 구현이 달라지는데, 어느쪽으로 풀어도 됨.

from collections import deque

def solution(n, edge):
    answer = [-1]*(n+1)
    G = {i+1:[] for i in range(n)}
    for a,b in edge:
        G[a].append(b)
        G[b].append(a)
    
    visit = set([1])
    queue = deque([(1, 0)])

    while queue:
        node, path=queue.popleft()

        answer[node]=path

        temp=[(i, path+1) for i in G[node] if i not in visit]
        for j in temp:
            visit.add(j[0])
        queue += temp
            
    answer = answer.count(max(answer))
    return answer

def solution_(n, edge):
    answer = [-1]*(n+1)
    G = {i+1:[] for i in range(n)}
    for a,b in edge:
        G[a].append(b)
        G[b].append(a)
    
    visit = set([])
    queue = deque([(1, 0)])

    while queue:
        node, path=queue.popleft()
        if node not in visit:  
            visit.add(node)
            answer[node]=path

            temp=[(i, path+1) for i in G[node]]
            queue += temp
            
    answer = answer.count(max(answer))
    return answer

'''
def solution2(n, edge):
    answer = [-1]*(n+1)
    G={i+1:[] for i in range(n)}
    for a,b in edge:
        G[a].append(b)
        G[b].append(a)
    
    visit=[]
    queue=[]
    queue.append((1,0))
    visit.append(1)
    while queue:
        node, path=queue.pop(0)
        answer[node]=path
        temp=[(i, path+1) for i in G[node] if i not in visit]
        for j in temp:
            visit.append(j[0])
        queue=queue+temp
            
    answer = answer.count(max(answer))
    return answer
'''