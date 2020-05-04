# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 프로그래머스 : 크레인 인형뽑기 게임 (https://programmers.co.kr/learn/courses/30/lessons/64061)

def solution(board, moves):
    answer = 0

    size = len(board)
    basket = []
    board2 = []
    count = 0

    for i in range(size):
        board2.append([k[i] for k in board])

    for i in moves:
        i = i - 1

        if board2[i] == [0] * size:
            continue

        res = get_doll(board2[i])
        board2[i] = res[1][:]
        temp_doll = res[0]

        if len(basket) != 0 and basket[len(basket) - 1] == temp_doll:
            basket.pop()
            count = count + 2
        else:
            basket.append(temp_doll)

    return count


def get_doll(target):
    for k in range(len(target)):
        if target[k] != 0:
            temp = target[k]
            target[k] = 0
            return [temp, target]