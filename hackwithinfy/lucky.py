import math
while(True):
    n=input()
    if(n=="stop"):
        break
    else:
        n=int(n)
        a,b=2,3
        flag=True
        k=2
        while(a<=math.sqrt(n) or b<=math.sqrt(n)):
            if(math.sqrt(n)%a==0 or math.sqrt(n)%b==0):
                flag=False
                break
            a,b=6*k+1,6*k-1
            k+=1
        if(flag):
            print("Lucky")
        else:
            print("Not Lucky")