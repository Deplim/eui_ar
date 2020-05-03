# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 2020 Dev-Matching 웹 백엔드 개발자(상반기) 3번.py
# 8자리 숫자 배열이 주어졌을 때 각 옆자리의 차가 k 이하가 되게 하는 최소한의 교환횟수를 찾아라.

def check(target, k):
    result=0
    for i in range(len(target)-1):
        temp=max(target[i], target[i+1])-min(target[i], target[i+1])
        if temp>k:
            result=result+(temp//k+(temp%k>0))-1
    return result

def solution(target, k):
    result=check(target, k)
    count=0
    print(target)

    # 방법이 없을때 k 반환
    temp_target=target[:]
    temp_target.sort()
    if check(temp_target, k)!=0:
        print("방법 없음")
        return -1

    while 1:
        if result==0:
            break

        for i in range(len(target)):
            for j in range(i+1, len(target)):
                temp_target=target[:]
                temp_target[i] , temp_target[j] = temp_target[j] , temp_target[i]
                temp_result=check(temp_target, k)

                if result>temp_result:
                    result=temp_result
                    next_target=temp_target

        count=count+1
        target=next_target
        print(target)

    return count

solution([3,7,2,8,6,4,5,1], 3)