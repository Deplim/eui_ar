#프로그래머스 | 타겟 넘버 : (https://programmers.co.kr/learn/courses/30/lessons/43165)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# solution2 -> solution : 재귀함수 실행시 배열이 아니라 index 를 넘기도록 구현

def solution(numbers, target):
    global numbers_, numbers_len
    numbers_ = numbers[:]
    numbers_len = len(numbers)

    return full_search(0, target)

def full_search(number, target):
    plus = target - numbers_[number]
    minus = target + numbers_[number]

    if number == (numbers_len-1):
        return (plus == 0) or (minus == 0)
    else:
        return full_search(number+1, plus)+full_search(number+1, minus)
        

'''
def solution2(numbers, target):
    answer = full_search2(numbers, target)
    return answer

def full_search2(numbers,target):
    if len(numbers)==1:
        return (target-numbers[0]==0) or (target+numbers[0]==0)
    else:
        return full_search2(numbers[1:], target-numbers[0])+full_search2(numbers[1:], target+numbers[0])
'''