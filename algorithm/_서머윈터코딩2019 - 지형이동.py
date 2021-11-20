#프로그래머스 | 지형 이동 : (https://programmers.co.kr/learn/courses/30/lessons/62050)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

from math import inf

def solution(land, height):
    land_l = len(land)
    
    land_group = []
    processed = []
    for i in range(land_l):
        for j in range(land_l):
            if (i, j) in processed:
                continue
            visit = [(i, j)]
            stack = [(i, j)]
            while stack:
                y, x = stack.pop()
                target = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
                for ny, nx in target:
                    if ny < 0 or ny >= land_l or nx < 0 or nx >= land_l:
                        continue    
                    if abs(land[y][x]-land[ny][nx]) <= height and (ny, nx) not in visit and (ny, nx) not in processed:
                        visit.append((ny, nx))
                        stack.append((ny, nx))
            land_group.append(visit)
            processed.extend(visit)
    
    node_label = {}
    for g_num, g in enumerate(land_group):
        for n in g:
            node_label[n] = g_num
    
    
    g_graph = {}
    for g_num, g in enumerate(land_group):
        for y, x in g:
            target = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
            for ty, tx in target:
                if ty < 0 or ty >= land_l or tx < 0 or tx >= land_l:
                    continue  
                t_label = node_label[(ty, tx)]
                if g_num < t_label:
                    if (g_num, t_label) not in g_graph:
                        g_graph[(g_num, t_label)] = abs(land[ty][tx] - land[y][x])
                    elif g_graph[(g_num, t_label)] > abs(land[ty][tx] - land[y][x]):
                        g_graph[(g_num, t_label)] = abs(land[ty][tx] - land[y][x])
    #print(land_group)
    #print(g_graph)
    
    
    

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))


'''
    DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    answer = 0
    queue = [land_group.pop(0)] # key가 1인 그룹을 queue에 넣음 

    while queue:
        min_height, key = inf, -1  
        g_one = queue.pop(0)
        inp = input()
        for g_two_num, g_two in enumerate(land_group): # g_one과 비교할 그룹들 
            for y1, x1 in g_one: # g_one의 y, x 좌표 
                for y2, x2 in g_two: # g_two의 y, x 좌표 
                    if (y1-y2, x1-x2) in DIR: # 둘의 차이가 DIR 안에 있으면 
                        candi = abs(land[y1][x1] - land[y2][x2]) # 후보값 candi
                        if candi < min_height: # candi가 min_height보다 작다면 
                            min_height = candi # 후보값이 min_height를 대신함 
                            key = g_two_num # min_height가 있는 그룹의 key 값 
        if key!=-1: # key가 0이 아니면 
            answer += min_height
            queue.append(g_one + land_group.pop(key))
    print(answer)
    return answer
'''

'''
    graph_items = list(g_graph.items())
    graph_items.sort(key = lambda x:x[1])
    
    count = 0
    connect = {}
    result = []
    for g in graph_items: 
        a, b = g[0]
        if a not in connect and b not in connect:
            connect[a] = count
            connect[b] = count
            result.append(g[1])
            count += 1
        elif a in connect and b not in connect:
            connect[b] = connect[a]
            result.append(g[1])
        elif b in connect and a not in connect:
            connect[a] = connect[b]
            result.append(g[1])
        else:
            continue
        if count == (len(land_group)-1):
            break

    return sum(result)
'''