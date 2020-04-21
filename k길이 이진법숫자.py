# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
#Given an integer K, print all binary strings of length K without consecutive 1s.

class Stack(list):
    push = list.append    # Insert
                          # Delete - 내장 pop 메소드 활용
    def is_empty(self):   # 데이터가 없는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self):        # 최상단 데이터 확인
        return self[-1]

    def show(self):
        print(self)

def binary_number(k):
    total=0
    s=Stack()
    s.push([1])
    s.push([0])
    while not s.is_empty():
        pop_list=s.pop()
        if len(pop_list)==k:
            total=total+1
            print(pop_list)
        else:
            pop_list.append(0)
            if(pop_list[-2]==1):
                s.push(pop_list[:])
            else:
                s.push(pop_list[:])
                pop_list[-1]=1
                s.push(pop_list[:])
    print("total : ",total)

#main
k=input("input length of binary number : ")
k=int(k)
binary_number(k)
