#프로그래머스 | 자물쇠와 열쇠 : (https://programmers.co.kr/learn/courses/30/lessons/60059)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import copy

def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)

    zero_count = 0
    for i in range(lock_len):
        zero_count += lock[i].count(0)

    start = (1-key_len, 1-key_len)

    for rotate_key in range(4):
        for y_ in range(key_len + lock_len - 1):
            for x_ in range(key_len + lock_len -1):
                coord_matching = (start[0] + y_, start[1] + x_)
                target = [(y, x) for x in range(key_len) for y in range(key_len)]
                count = 0

                for y, x in target:
                    if (coord_matching[0]+y)<0 or (coord_matching[0]+y)>= lock_len:
                        continue
                    if (coord_matching[1]+x)<0 or (coord_matching[1]+x)>= lock_len:
                        continue
                    if (key[y][x] + lock[coord_matching[0] + y][coord_matching[1] + x]) != 1:
                        break
                    if key[y][x] == 1:
                        count += 1
                
                if count == zero_count:
                    return True
        
        rotate=[[0]*key_len for _ in range(key_len)]

        for i in range(key_len):
            for j in range(key_len):
                rotate[j][(key_len-1)-i] = key[i][j]
        key = copy.deepcopy(rotate)
    
    return False

#import numpy as np
#key_ = np.around(np.random.rand(3, 3))
#lock_ = np.around(np.random.rand(5, 5))
#print(key_)
#print(lock_)
#print(solution(key_.tolist(), lock_.tolist()))
