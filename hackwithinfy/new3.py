a={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':12,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
d=dict()
str=input()
str=str.upper()
print(str)
for i in str:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
for i in l:
    flag=False
    for j in d:
        if(i%a[j]==0):
            if(i<=a[j]*d[j]):
                flag=True
                break
    if(flag):
        print("Yes")
    else:
        print("No")