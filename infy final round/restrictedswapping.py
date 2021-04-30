n=int(input())
l=list(map(int,input().split(',')))
for i in range(n):
    if(l==sorted(l)):
        break
    a=l[i]
    b=min(l[i+1:])
    if(a>b):
        print("in")
        ind=l[i+1:].index(b)+(i+1)
        temp = l[i]
        l[i]=b
        l[ind]=temp
    print(a," ",b," ",ind)
    print(i," -> ",l)
print(l)