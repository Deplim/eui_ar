#구름 | Happy Number : (https://level.goorm.io/exam/43084/happy-number/quiz/1)
# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)

# 숫자를 문자 단위로 끊어줘야하기 때문에, while 문을 끝낼때마다 target 을 str 변환하도록 함.

user_input=input()
target = user_input
storage={}
result=""

while 1:
	aaa=list(target)
	temp=0
	for i in aaa:
		temp=temp+int(i)**2
	target=temp
	
	if target==1:
		result="Happy"
		break
	if target in storage:
		result="Unhappy"
		break
	else:
		storage[target]=1
		
	target=str(target)

print(user_input+" is "+result+" Number.")
	