def fun(n):
    if(n==1):
        return n
    s=1+n
    for i in range(2,n):
        if(n%i==0):
            s+=i
    return s

a = list(map(int,input().split(',')))
print(a)
res=[]
for i in a:
    n=fun(i)
    print(i," ",n)
    if n in a:
        res.append(i)
if(len(res)!=0):
    print(res)
else:
    print(-1)