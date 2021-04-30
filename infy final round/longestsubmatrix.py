r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
temp=l
length=len(l[0])
longest=0
for i in range(1,r):
    for j in range(1,length):
        if(temp[i][j]!=0):
            l=[temp[i-1][j],temp[i-1][j-1],temp[i][j-1]]
            temp[i][j]=min(l)+1
            if(temp[i][j]>longest):
                longest=temp[i][j]
print(longest)