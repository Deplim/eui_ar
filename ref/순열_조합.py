# https://medium.com/@dltkddud4403/python-순열-조합-구현-5e496e74621c 참조

def comb(lst, n):
    ret = []

    if n > len(lst): return ret
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


def perm(lst, n):
    ret = []

    if n > len(lst): return ret
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret