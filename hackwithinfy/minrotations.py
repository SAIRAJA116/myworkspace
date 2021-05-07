n=int(input())
l=list()
for _ in range(n):
    l.append(input().upper())
possibilites=list()
a=l[0]
d=dict()
for i in range(len(l[0])):
    possibilites.append(a)
    d[a]=i
    a=a[1:]+a[0]
print(possibilites)
print(d)
for i in range(1,len(l)):
    a=l[i]
    for j in range(len(l[i])):
        d[a]+=j
        a=a[1:]+a[0]
    print(d)
print(d)
min=9999999
for i in l:
    if(d[i]<min):
        min=d[i]
print(min)