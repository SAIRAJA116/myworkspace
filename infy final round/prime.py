import math
def isprime(n):
    if(n==2 or n==3):
        return True
    if(n%2==0 or n%3==0):
        return False
    else:
        i=1
        while(1):
            a,b=6*i+1,6*i-1
            if(n%a==0 and a<n):
                print(a," ",b," ",n)
                return False
            if(n%b==0 and b<n):
                print(a," ",b," ",n)
                return False
            if(a>n and b>n):
                break
            i+=1
    return True

o = int(input())
while(o!=0):
    print(isprime(o))
    o = int(input())