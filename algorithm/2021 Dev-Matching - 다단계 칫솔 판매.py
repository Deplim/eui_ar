#프로그래머스 | 다단계 칫솔 판매 : (https://programmers.co.kr/learn/courses/30/lessons/77486)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(enroll, referral, seller, amount):
    # 그래프, sell dict 만들기
    graph = {i:[] for i in set(referral)}
    graph_r = {}
    sell = {}
    for i, r in enumerate(referral) : 
        graph[r].append(enroll[i])
    for k in graph.keys():
        for e in graph[k]:
            graph_r[e] = k
    for i, s in enumerate(seller):
        if s in sell:          
            sell[s].append(amount[i]*100)
        else:
            sell[s] = [amount[i]*100]
    
    # bfs 트리 탐색으로
    stage = [["-"]]
    queue = ["-"]
    while queue:
        queue_t = []
        for r in queue:
            e_ = graph.get(r)
            if e_ is not None:
                queue_t.extend(e_)
        if len(queue_t) != 0:
            stage.append(queue_t)
        queue = queue_t
    
    # 밑에서부터 단계 별로 올라오면서 분배 계산
    stage.reverse()
    answer = {p:[] for p in enroll+["-"]}
    for st in stage:
        for p in st:
            if p in sell:
                for s_ in sell[p]:
                    answer[p].append(s_)
            if p in graph_r and answer[p]!=0:
                r_ = graph_r[p]
                for i, am in enumerate(answer[p]):
                    if (answer[p][i]//10)>0:
                        answer[r_].append(answer[p][i]//10)
                        answer[p][i] -= (answer[p][i]//10)
    answer = [int(sum(answer[p])) for p in enroll]
    return answer