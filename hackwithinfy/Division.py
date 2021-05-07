def fun(a,b,c):
    rem=c%a
    if(a==1):
        return -1
    if(rem==b):
        return c
    elif(rem>b):
        return c -(rem-b)
    else:
        return c-(rem+(a-b))
        

while(True):
    a,b,c=map(int,input().split())
    print(fun(a,b,c))