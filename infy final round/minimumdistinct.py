n=int(input())
l=input().split()
distinct=list(set(l))
count=[]
for i in distinct:
    count.append(l.count(i))
print(l)
print(distinct)
print(count)
count.sort()
print(count)
i=0
length=len(count)
if(count[i]>n):
    print(len(count))
else:
    while(n!=0):
        if(count[i]<=n):
            n-=count[i]
            count[i]=0
            length-=1
        else:
            count[i]-=n
            n=0
        i+=1
print(length)
