#프로그래머스 | 지형 이동 : (https://programmers.co.kr/learn/courses/30/lessons/62050)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

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
    
    graph_items = list(g_graph.items())
    graph_items.sort(key = lambda x:x[1])
    print(graph_items)
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

import numpy as np
    

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))