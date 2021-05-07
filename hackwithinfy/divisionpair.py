#10 9 4 5 7 2 8 20 21
#15
l=list(map(int,input().split()))
m=int(input())
d=dict()
for i in l:
    if(i%m in d):
        d[i%m]+=1
    else:
        d[i%m]=1
print(d)
res=0
visited=[]
for i in d:
    if(m-i in d and (m-i not in visited and i not in visited)):
        res+=d[i]*d[m-i]
        visited.append(m-i)
        visited.append(i)
        print(i," ",m-i)
        #print(res)
print(visited)
print(res)