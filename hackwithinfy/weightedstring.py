a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
v=[0,1,3]
for i in range(3,27):
    v.append(v[i-1]*(i+1))
# print(v)
d=dict()
for i in range(len(a)):
    d[a[i]]=v[i+1]
# print(d)
num=int(input())
str=""
max=""
while(num!=0):
    for i in a:
        if(d[i]>num):
            break
        max=i
    q=num//d[max]
    num=num%d[max]
    str=q*max+str
print(str)