# 백준 | 덩치 : (https://www.acmicpc.net/problem/7568)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

def solution(inputs):
    rank_dict = {i: 0 for i, _ in enumerate(inputs)}
    Answer = []

    # 자신보다 더 "큰 덩치"의 사람의 수
    for i, (w, h) in enumerate(inputs):
        score = 0
        for i_, (w_, h_) in enumerate(inputs):
            if w < w_ and h < h_:
                score += 1
        Answer.append(score+1)
    return Answer


n = int(input())
inputs = []
for i in range(n):
    inputs.append(tuple(map(int, input().split(' '))))

Answer = list(map(str, solution(inputs)))
print(' '.join(Answer))
