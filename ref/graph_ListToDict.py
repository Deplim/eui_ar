# EuiRyeong Jeong (wjddmflud@gmail.com, https://github.com/Deplim)
# Graph : List to Dict

N=3
paths = [[1,2],[2,3],[3,1]]
G={i:[] for i in range(N)}
for a,b in paths:
  G[a-1].append(b-1)
  G[b-1].append(a-1)

print(G)



