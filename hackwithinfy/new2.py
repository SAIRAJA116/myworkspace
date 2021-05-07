def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)


m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
# print(l1)
lcm=l1[0]
for i in range(1,len(l1)):
    g=gcd(lcm,l1[i])
    # print(g)
    lcm=(lcm*l1[i])//g
# print(lcm)
g=l2[0]
for i in range(1,len(l2)):
    g=gcd(g,l2[i])
# print(g)
k=lcm
count=0
while(k<=g):
    count+=1
    k+=lcm
print(count)