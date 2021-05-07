# 6 4
# 2 1 3 1 4
# 4 1 2

m,n=map(int,input().split())
hcuts=list(map(int,input().split()))
vcuts=list(map(int,input().split()))
cost=0
hcuts.sort()
vcuts.sort()
hcuts.reverse()
vcuts.reverse()
x=y=0
hboxes=vboxes=1

while(x<len(hcuts) and y<len(vcuts)):
    if(hcuts[x]>vcuts[y]):
        cost+=hcuts[x]*vboxes
        print(hcuts[x]," * ",vboxes)
        hboxes+=1
        x+=1
    else:
        cost+=vcuts[y]*hboxes
        print(vcuts[y]," * ",hboxes)
        vboxes+=1
        y+=1
while(x<len(hcuts)):
    cost+=hcuts[x]*vboxes
    print(hcuts[x]," * ",vboxes)
    hboxes+=1
    x+=1
while(y<len(vcuts)):
    cost+=vcuts[y]*hboxes
    print(vcuts[y]," * ",hboxes)
    vboxes+1
    y+=1
print(cost)
