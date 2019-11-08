#프로그래머스 문제: 지형 편집 (https://programmers.co.kr/learn/courses/30/lessons/12984
# >> 풀이 by DepLim , wjddmflud@gmail.com

def solution(land, P, Q):
    n = len(land)
    answer = 0
    land_line=[]
    land_max = land[0][0]
    for i in range(len(land)):
        land_line.extend(land[i])
    land_max=max(land_line)
    land_min = min(land_line)

    block_range = [land_min, land_max+1]

    hight = (block_range[1] - block_range[0]) // 2 + block_range[0]
    while 1:
        a = 0
        a=sum(i > hight for i in land_line)
        temp = (n ** 2 - a) * P - a * Q

        a2 = 0
        a2=sum(i > hight-1 for i in land_line)
        temp2 = (n ** 2 - a2) * P - a2 * Q

        if (temp > 0) and (temp2 > 0):
            block_range[1] = hight
        elif (temp < 0) and (temp2 < 0):
            block_range[0] = hight
        else:
            for i in range(n):
                for j in range(n):
                    if land[i][j] > hight:
                        answer = answer + Q * (land[i][j] - hight)
                    elif land[i][j] < hight:
                        answer = answer + P * (hight - land[i][j])
            break;
        hight = (block_range[1] - block_range[0]) // 2 + block_range[0]

    return answer

print("result : ",solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]],5,3))



