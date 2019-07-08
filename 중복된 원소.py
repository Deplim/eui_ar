#by Eui Ryeong , wjddmflud@gmail.com
#랜덤한 정수 배열이 주어지면 중복된 원소의 값을 모두 프린트 하시오.
# 단, 공간복잡도 O(1)이여야 합니다.

def Duplicate_elements(ar):
    a=[]
    for i in range(len(ar)):
        for j in range(len(ar)):
            if(i==j): continue
            if(ar[i]==ar[j]):
                if ar[i] not in a:
                    a.append(ar[i])
    print(a)

ar=input("배열을 입력하시오.(공백 없이) : ")
Duplicate_elements(ar)
