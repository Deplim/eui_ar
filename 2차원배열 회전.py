# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 2차원 배열 회전

def rotate_90(target):
    size=len(target)
    result=[[0]*size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            result[j][(size-1)-i]=target[i][j]
    return result

temp=[[1, 0, 8],
      [9, 3, 1],
      [12, -1, 4]]

print(rotate_90(temp))