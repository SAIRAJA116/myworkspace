# 5
# 1 2 3 4 5
# 7
# 1 3
# 2 3
# 1 2
# 6 8
# 5 4
# 5 7
# 8 9

n=int(input())
l=list(map(int,input().split()))
m=int(input())
p=[]
for _ in range(m):
    p.append(list(map(int,input().split())))
visited=[0]*m
visited[0]=1
g=[]
g.append(p[0])
i=0
for _ in range(m):
    for _ in range(2):
        for j in range(1,len(p)):
            if((p[j][0] in g[i]) or (p[j][1] in g[i])):
                g[i].append(p[j][0])
                g[i].append(p[j][1])
                g[i]=list(set(g[i]))
                visited[j]=1
    for k in range(len(visited)):
        if(visited[k]==0):
            i+=1
            g.append(p[k])
            break
min=999999
for i in g:
    if(sum(i)<min):
        min=sum(i)
print(min)