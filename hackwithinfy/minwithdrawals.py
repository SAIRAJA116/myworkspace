#1 7 15 2 3 6
#1 6 3 2 1 5 12 8 4 8 3
l=list(map(int,input().split()))
m=int(input())
max=0
n=sum(l)-m
i,j=0,1
while(i<=j and j<=len(l)):
    curr=sum(l[i:j])
    if(curr>n):
        i+=1
    elif(curr<n):
        j+=1
    elif(curr==n):
        if(j-i>max):
            max=j-i
        j+=1
if(max==0):
    print(-1)
else:
    print(len(l)-max)