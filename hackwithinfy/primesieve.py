n=int(input())
l=[0]*(n+1)
for i in range(2,n+1):
    if(i*i>n):
        break
    else:
        if(l[i]==0):
            j=i*i
            while(j<n+1):
                l[j]=1
                j+=i
for i in range(2,n+1):
    if(l[i]==0):
        print(i)