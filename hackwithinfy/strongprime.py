a,b=map(int,input().split())
l=[]
if(a<=10):
    l=[2,3]
min=((a-1)//6)-1
if(min<=0):
    min=1
max=((b+1)//6)+1
print(min," ",max)
for i in range(min,max+1):
    o=6*i-1,6*i+1
    flag=False
    for i in o:
        j=2
        c=0
        flag=True
        while(j*j<=a):
            if(i%j==0):
                flag=False
                break
            j+=1
        if(flag):
            l.append(i)
print(l)
s=[]
for i in range(len(l)):
    if(l[i]>=a and l[i]<=b):
        print(2*l[i]," == ",l[i-1]+l[i+1])
        if(2*l[i]>l[i-1]+l[i+1]):
            s.append(l[i])
print(s)
