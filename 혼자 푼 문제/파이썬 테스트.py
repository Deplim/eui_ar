# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# 파이썬 테스트

'''
import tensorflow as tf

with tf.compat.v1.Session() as sess:
  h = tf.constant("Hello")
  w = tf.constant("World!")
  hw = h + w
  ans = sess.run(hw)
  print(ans)
'''
'''
a=""
try:
  a="k"
  raise Exception('test exception raise')
except:
  print(a)
'''

#import sys
#sys.setrecursionlimit(10 ** 9)

N,T=list(map(lambda x:int(x),input().split()))
I=[]
for i in range(int(N)):
  I.append(list(map(lambda x:int(x),input().split())))

i_dict={}
for i in range(N):
  for j in range(N):
    i_dict[(j,i)]=I[i][j]
i_dict[(0,0)]=0

go=[(1,0),(0,1),(-1,0),(0,-1)]
result={}
def solve(c, t):
  if (c+(t,)) in result:
    return result[c+(t,)]
  if c==(N-1, N-1):
    return (i_dict[c] if t==0 else 0)
  result[c+(t,)]=-1
  temp=[]
  temp2=[]
  for i in go:
    target=(c[0]+i[0], c[1]+i[1])
    if target in i_dict and not(result[target+((t+1)%3,)]==-1 if (target+((t+1)%3,)) in result else False):
      e=solve(target, (t + 1) % 3)
      temp.append(e)
      temp2.append((target+(t,), e))
  temp=list(filter(lambda x:x!=-1, temp))
  if len(temp)==0:
    del result[c+(t,)]
    return -1
  print(c, t, temp, temp2)
  res=(T+i_dict[c] if t==0 else T)+min(temp)
  result[c+(t,)]=res
  return res

print(solve((0,0), 0))
print(result)
