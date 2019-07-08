#by Eui Ryeong , wjddmflud@gmail.com
#랜덤한 정수 배열이 주어지면 중복된 원소의 값을 모두 프린트 하시오.
# 단, 공간복잡도 O(1)이여야 합니다.

def Duplicate_elements(ar):
    a=0
    for i in range(len(ar)):
        if(ar[i]==None): continue
        a=ar[i]
        for j in range(len(ar)):
            if(i==j): continue
            if(ar[i]==ar[j]):
                ar[j]=None
                if(ar[i]!=None):
                    print(ar[i])
                    ar[i]=None


a=input("배열을 입력하시오.(공백 없이) : ")
ar=[]
for i in range(len(a)):
    ar.append(a[i])
Duplicate_elements(ar)

#입력값을 배열로 받을 수 있다면 이렇게 안풀고 정렬만 하면 된다. 결과에 중복된 값이 나오지 않게 할 수 있다.
#숫자가 아닌 다른것을 입력값으로 받아도 같은 것끼리 뭉치게 전처리만 해주면 됨.
#문제의 포인트는 결과에 중복된 값이 나오지 않도록 하는것. 입력값 배열 공간을 이용해 그 작업을 함.