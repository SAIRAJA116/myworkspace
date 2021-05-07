#distribute weights
#1 2 3 4 5
def ispossible(l,m,k):
    curr=l[0]
    pair=1
    flag=True
    for i in range(1,len(l)):
        if(curr+l[i]<=k):
            curr+=l[i]
        else:
            curr=l[i]
            pair+=1
            if(pair>m):
                flag=False
                break
    print(k," ",flag)
    return flag



l=list(map(int,input().split()))
m=int(input())
low=max(l)
h=sum(l)
min=99999
while(low<=h):
    mid=(low+h)//2
    if(ispossible(l,m,mid)):
        if(mid<min):
            min=mid
        h=mid-1
    else:
        low=mid+1
print(min)
    
        