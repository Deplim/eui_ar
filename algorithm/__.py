
def solution(target, input_):
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

        queue = next_queue

    return queue[target]


n, target = tuple(map(int, input().split(' ')))
input_ = []
for i in range(n):
    input_.append(int(input()))

Answer = solution(target, input_)
print(Answer)
