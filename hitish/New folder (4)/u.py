d={1:80.0,2:130.0,3:100.0,4:80.0,5:90.0,6:110.0,7:120.0,8:140,9:70.0,10:80.0}

s=0
i=q=0
c='y'
while(1):
    i=int(input())
    q=int(input())
    if(q<1 and q>21):
        print("INVALID INPUT")
    else:
        s+=q*d[i]
        c=input()
        if(c=='y' or c=='Y'):
            continue
        elif(c=="N" or c=='N' ):
            break

print("Total Amount : ",s)

