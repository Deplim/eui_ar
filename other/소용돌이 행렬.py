import numpy


def solution(n):
    output = [[0 for _ in range(n)] for _ in range(n)]

    go = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    c_point = [0, 0]
    c_num = 1

    while n >= 1:
        if n == 1:
            output[c_point[0]][c_point[1]] = c_num
            break

        for dir in go:
            for i in range(n-1):
                output[c_point[0]][c_point[1]] = c_num+i
                c_point = [c_point[0]+dir[0], c_point[1]+dir[1]]
        c_num += (n-1)
        c_point = [c_point[0]+1, c_point[1]+1]
        n = n-2

    return output


ans = solution(8)
num_ans = numpy.array(ans)
print(num_ans)
