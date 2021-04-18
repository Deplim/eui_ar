#백준 | 카드 정렬하기 : (https://www.acmicpc.net/problem/1715)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

import heapq

target=[]
k=int(input())
for i in range(k):
    target.append(int(input()))

heapq.heapify(target)

answer = 0
while 1:
    if len(target)==1:
        break
    target1=heapq.heappop(target)
    target2=heapq.heappop(target)
    answer=answer+target1+target2
    heapq.heappush(target, target1+target2)
print(answer)