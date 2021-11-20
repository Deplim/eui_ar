#백준 | 카드 정렬하기 : (https://www.acmicpc.net/problem/1715)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# 사실상 "_Heap - 더 맵게" 랑 똑같은 문제임

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

'''
배열을 한번만 정렬하고 작은거부터 꺼내면서 계속 더하면 되는 것이 아닌가 생각했으나,
그렇게 하면 가장 최근에 더한것이 최소값이라는 보장이 없음.
=> 값을 다시 삽입할 수 있는 heap 자료구조가 필요
'''