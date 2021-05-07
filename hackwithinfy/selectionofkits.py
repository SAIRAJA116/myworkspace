l=list(map(int,input().split()))
s=sum(l)/2
l.sort()
sum=0
c=0
for i in range(len(l)-1,-1,-1):
    sum+=l[i]
    c+=1
    if(sum>=s):
        print(c)
        break

# a=10**21
# print(a)