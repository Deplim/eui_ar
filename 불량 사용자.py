# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 프로그래머스 : 불량 사용자 (https://programmers.co.kr/learn/courses/30/lessons/64064)
import ref.순열_조합

def check(a, b):
    for i in b:
        check = 1
        for j in range(len(i)):
            if check2(a[j], i[j]) == 0:
                check = 0
                break;
        if check == 1:
            return 1

    return 0


def check2(a, b):
    if len(a) != len(b):
        return 0

    for i in range(len(b)):
        if b[i] == '*':
            continue
        if a[i] != b[i]:
            return 0
    return 1


def solution(user_id, banned_id):
    banned_size = len(banned_id)
    comb_user = comb(user_id, banned_size)
    perm_banned = perm(banned_id, banned_size)
    count = 0

    for i in comb_user:
        count = count + check(i, perm_banned)

    return count
