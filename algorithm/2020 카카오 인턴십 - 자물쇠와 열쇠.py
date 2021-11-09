#프로그래머스 | 자물쇠와 열쇠 : (https://programmers.co.kr/learn/courses/30/lessons/60059)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import copy




def solution2(a, b):
    # 열쇠
    key = a
    key_90 = rotate(key)
    key_180 = rotate(key_90)
    key_270 = rotate(key_180)

    # 자물쇠
    lock = b

    # 자물쇠 '0'의 갯수
    lock_0 = 0
    for i in range(len(lock)):
        lock_0 = lock_0 + lock[i].count(0)

    padding(key, lock)
    answer = False
    for x_start in range(len(lock)-len(key)+1):
        for y_start in range(len(lock)-len(key)+1):
            # 해당 위치에 자물쇠의 0이 모두 존재하는가?
            cnt = 0
            for i in range(len(key)):
                for j in range(len(key)):
                    if lock[x_start+i][y_start+j] == 0:
                        cnt = cnt + 1
            if cnt == lock_0: # lock_0 = 자물쇠의 총 0의 갯수
                for fit_key in [key, key_90, key_180, key_270]:
                    new_lock_0 = lock_0
                    key1_and_lock1 = 0
                    for i in range(len(key)):
                        for j in range(len(key)):
                            # 열쇠의 1과 자물소의 1이 만난다 = i,j for문을 빠져나가라
                            # 열쇠의 1과 자물쇠의 0이 만난다 = new_lock_0을 1씩 감소시켜라
                            # 그 외에는 아무일도 일어나지 않는다
                            if fit_key[i][j]==1 and lock[x_start+i][y_start+j]==1:
                                key1_and_lock1 = 1
                                break
                            elif fit_key[i][j]==1 and lock[x_start+i][y_start+j]==0:
                                new_lock_0 = new_lock_0 - 1
                        if key1_and_lock1==1:
                            break
                    # 열쇠가 맞아 떨어진다.
                    if new_lock_0 == 0:
                        answer = True
                        return answer     
            else:
                continue
    return answer

# key를 90도 회전시키기
def rotate(key):
    rotate_key = copy.deepcopy(key)
    
    y = len(key) - 1
    for i in range(len(key)):
        x = 0
        for j in range(len(key)):
            rotate_key[x][y]= key[i][j]
            x = x + 1
        y = y-1
    return rotate_key

def padding(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    
    #왼쪽 오른쪽 padding
    for i in range(len_lock):
        lock[i] = [2]*(len_key-1) + lock[i] + [2]*(len_key-1)
    # 윗부분 padding
    for _ in range(len_key-1):
        lock.insert(0, [2]*((len_key-1)*2 + len_lock))
    # 아래부분 padding
    for _ in range(len_key-1):
        lock.append([2]*((len_key-1)*2 + len_lock))
    # lock을 padding시켜주는 것이 목적이므로, return값이 없어도 무관하다.
