k=int(input())
l=list(map(int,input().split()))
d=dict()
for i in l:
    a=i%k
    if(a not in d):
        d[a]=1
    else:
        d[a]+=1
print(d)
c=0
for i in d:
    if(i==0 or i==(k//2)):
        c=c+(d[i]*(d[i]-1)//2)
        d[i]=0

    if(i!=0):
        j=k-i
        if(j in d):
            c+=d[i]*d[j]
            d[i]=d[j]=0
            # print(c)
print(c)
print(d)