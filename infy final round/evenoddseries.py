s=input()
l=[]
for i in s:
    if(i.isdigit()):
        l.append(i)
l=sorted(list(set(l)))
l=list(map(int,l))

leasteven =10
for i in l:
    if(i<leasteven and i%2==0):
        leasteven=i
if(leasteven==10):
    print(-1)
else:
    res=""
    l.remove(leasteven)
    for i in range(len(l)-1,-1,-1):
        res+=str(l[i])
    res+=str(leasteven)
    print(res)
