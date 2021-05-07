n=int(input())
l=[]
for _ in range(n):
    l.append(int(input())
count=0
for i in range(len(l)):
    if(l[i]>=l[i+1]):
        l[i+1]=l[i]
        
        