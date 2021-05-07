n=int(input())
l=input().split()
d=dict()
d[l[0]]=0
a=l[0]
for i in range(1,len(l[0])):
    a=a[1:]+a[0]
    d[a]=i
print(d)
for i in range(1,n):
    a=l[i]
    for j in range(len(a)):
        d[a]+=j
        a=a[1:]+a[0]
print(d)
min=99999
print(l)
for i in l:
    if(min>d[i]):
        min=d[i]

print(min)