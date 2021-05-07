def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))

#lcm of l1
lcm=l1[0]
for i in range(1,len(l1)):
    g=gcd(lcm,l1[i])
    lcm=(lcm*l1[i])//g
    # #print(lcm)
    # print(lcm," ",g)
# print(lcm)

#gcd of l2
g=l2[0]
for i in range(1,len(l2)):
    g=gcd(g,l2[i])
# print(g)
#identifing the numbers that are inbetween lcm and gcd that are the factors of all the elements in l2
count=0
res=lcm
while(res<=g):
    if(g %res==0):
        count+=1
    res+=lcm
print(count)
