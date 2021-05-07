n=3
c=3
while(n!=1000):
    #n=int(input())
    if(n==1):
        print(0)
    elif(n==2):
        print(5)
    else:
        s=0
        a=(n-1)//2
        res=(a*4+((n-1)-a)*5)+5
        for i in str(res):
            s=s+int(i)
        if(s%5==0):
            print(res," -> ",c)
            c+=1 
    n+=1
