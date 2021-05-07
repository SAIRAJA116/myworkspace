n=int(input())
liters=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
if(liters%n==0):
    if(sum(l)>=liters):
        repeat=True
        while(repeat):
            repeat=False
            for i in range(len(l)):
                if(liters>l[i]):
                    liters-=l[i]
                else:
                    break
                    repeat=True
        print(liters//n)
    else:
        print(-1)
else:
    if(sum(l)<liters):
        print(-1)
    else:
        print((liters//n)+1)