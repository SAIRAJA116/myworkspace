r=int(input())
c=r-1
m=[]

def isdivisible(num):
    l=list(str(num))
    l=list(map(int,l))
    if(num%sum(l)==0):
        return True
    else:
        return False



for i in range(r):
    m.append(list(map(int,input().split())))

for i in m:
    print(i)

for i in range(r-1):
    for j in range(c-1):
        if(isdivisible(m[i][j])and isdivisible(m[i][j+1]) and isdivisible(m[i+1][j]) and isdivisible(m[i+1][j+1])):
            print(m[i][j]," ",m[i][j+1])
            print(m[i+1][j]," ",m[i+1][j+1])


