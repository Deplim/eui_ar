#프로그래머스 문제 : 도둑질 (https://programmers.co.kr/learn/courses/30/lessons/42897?language=python3)
# >> 풀이 by DepLim , wjddmflud@gmail.com
def solution(money):
    hlen = len(money)
    print(hlen)
    if (hlen == 3):
        return max(money);
    else :
        # 첫번째 집을 털기로 했을 때
        money_stack=[-1 for _ in range(hlen)]
        money_stack[hlen-1]=0
        money_stack[hlen-2]=money[hlen-2]
        money_stack[hlen-3]=money[hlen-3]
        i=hlen-4
        while (i > -1):
            money_stack[i]=money[i]+max([money_stack[i+2], money_stack[i+3]])
            i=i-1
        a = money_stack[0];


        # 첫번째 집을 털지 않기로 했을 때
        money_stack = [-1 for _ in range(hlen)]
        money_stack[hlen - 1] = money[hlen - 1]
        money_stack[hlen - 2] = money[hlen - 2]
        money_stack[hlen - 3] = money[hlen - 3] + money[hlen - 1]
        i = hlen - 4
        while (i > 0):
            money_stack[i]=money[i]+max([money_stack[i+2], money_stack[i+3]])
            i=i-1
        money_stack[0] = max([money_stack[1], money_stack[2]])
        b = money_stack[0];

    answer=max([a, b])
    return answer





