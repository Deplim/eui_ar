# 백준 | 동전 1 : (https://www.acmicpc.net/problem/2293)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# 시관초과를 해결하지 못해 다른 사람의 코드를 참고함
# https://yabmoons.tistory.com/491
# solution2 : 시간 초과 해결 못한 코드  |  solution : 참고한 코드

def solution(target, input_):
    DP = [1] + [0] * (target)
    for coin in input_:
        for i in range(coin, target+1):
            DP[i] = DP[i] + DP[i-coin]
    return DP[target]


def solution2(target, input_):
    input_.sort(reverse=True)
    print(input_)
    Answer = 0

    max_of_first_value = target//input_[0]
    queue = {input_[0]*i: 1 for i in range(max_of_first_value+1)}
    for c_num in range(1, len(input_)):
        next_queue = {}
        for key in queue:
            max_of_target_value = (target-key)//input_[c_num]
            for coin_num in range(max_of_target_value+1):
                next_key = key + input_[c_num]*coin_num
                if next_key in next_queue:
                    next_queue[next_key] += queue[key]
                else:
                    next_queue[next_key] = queue[key]

        print(queue)
        queue = next_queue
        input()
    return queue[target]


n, target = tuple(map(int, input().split(' ')))
input_ = []
for i in range(n):
    input_.append(int(input()))

Answer = solution(target, input_)
print(Answer)
