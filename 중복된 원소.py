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
