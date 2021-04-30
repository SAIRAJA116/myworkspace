s=input()
l=set()
for i in s:
    if(i.isdigit()):
        l.add(i)
l=list(l)
l=list(map(int,l))
leasteven=10
for i in l:
    if(i<leasteven and i%2==0):
        leasteven=i
if(leasteven==-1):
    print(-1)
else:
    l.remove(leasteven)
    res=''
    l=sorted(l,reverse=True)
    for i in l:
        res+=str(i)
    res+=str(leasteven)
print(res)

