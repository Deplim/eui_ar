# 프로그래머스 | 동굴 탐험 : (https://programmers.co.kr/learn/courses/30/lessons/67260)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# 처음 풀었던 방식(solution2) 은 핵심 아이디어는 맞았으나 효율성 테스트 통과를 못함.
# 알고리즘 최적화를 위해 cylce 확인 부분에서 탐색 시간복잡도가 적게 들어가는 자료형을 사용.
# + 그리고 현제 경로에 속한 노드를 stack 에 같이 넣어주는게 아니라, 외부에서 정의한 변수에 저장되게 끔 함.
# 알고리즘을 잘 풀기 위해서는 사용하는 언어의 주요 자료형들 시간 복잡도를 알고있어야 한다.
# https://wiki.python.org/moin/TimeComplexity

def solution(n, path, order):
    # 그래프가 tree 라고 가정한 풀이
    G = {i: [] for i in range(n)}
    for a, b in path:
        G[a].append(b)
        G[b].append(a)

    check = {i[1]: i[0] for i in order}

    # queue 에서 pop(0) 에 의한 시간복잡도를 줄이려면 deque 를 사용하거나, 아래처럼 큐에 들어있는 아이템을 한번에 다 처리해야함.
    prerequisites = {}
    queue = []
    queue.append((0, -1))
    while queue:
        queue2 = []
        for i in queue:
            node, visit = i[0], i[1]
            prerequisites[node] = [visit]
            queue2.extend([(j, node) for j in G[node] if j != visit])
        queue = queue2

    for i in range(n):
        if i in check:
            prerequisites[i].append(check[i])
        else:
            prerequisites[i].append(-1)

    # 노드 i 에서 시작하여 check,res 를 계속 다시 탐색했을때 i 로 돌아오는지 (cycle) 확인
    # (i번 방을 가기 위해 i 가 필요하다는 의미이므로)

    ok = {i: 0 for i in range(n)}
    bb = 0
    for i in check:
        if ok[i]:
            continue

        visit_list = {}  # 재귀함수를 쓰지 않아도 현제 경로에 속한 노드를 계산하게끔 구현할 수 있다.
        on_visit = []
        global_visit_list = set()
        stack = []
        stack.append(i)

        while stack:
            node = stack.pop()
            while len(on_visit) != 0 and len(stack) < on_visit[-1][0]:
                del visit_list[on_visit[-1][1]]
                on_visit.pop()

            bb += 1
            if node in visit_list:
                return False
            if node == -1 or ok[node] or node in global_visit_list:
                continue

            global_visit_list.add(node)
            visit_list[node] = 1
            on_visit.append((len(stack), node))

            previous_node = prerequisites[node]
            stack.extend([previous_node[0], previous_node[1]])

            bb += 1
        for i in global_visit_list:
            ok[i] = 1

    return True

# 풀긴 했지만 깔끔하게 짜지 못한 것 같아서 다른 사람의 코드를 서칭해봄
# https://cocook.tistory.com/132
