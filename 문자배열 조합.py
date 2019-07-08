#by Eui Ryeong , wjddmflud@gmail.com

def factorial(n):
    sum = 1
    for i in range(n-1):
        sum=sum*n
        n=n-1
    return sum

def text_combiner(t):
    length=len(t)
    result=[]
    interval=[]
    total=factorial(length)
    print("total : ", total)
    for i in range(length-1):
        interval.append(factorial(length-1-i))

    for i in range(total):
        result=[]
        value=i
        t_cp = t[:]
        for j in range(length-1):
            target=value//interval[j]
            result.append(t_cp[target])
            value=value-target*interval[j]
            temp=t_cp[length-1-j]
            t_cp[length-1-j]=t_cp[target]
            t_cp[target]=temp

        result.append(t_cp[0])
        print(result)

text=input("input your string : ")
t_input=[]
for i in range(len(text)):
    t_input.append(text[i])
print(t_input)
text_combiner(t_input)