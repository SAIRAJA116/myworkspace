import math
n=int(input())
s=1
i=2
while(i<=math.sqrt(n)):
    if(n%i==0):
        if(n%i!=n//i):
            s+=i+n//i
        else:
            s+=i
    i+=1
if(s==n):
    print("YES")
else:
    print("NO")