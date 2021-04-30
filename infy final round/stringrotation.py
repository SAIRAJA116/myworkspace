l=input().split(',')
print(l)
d=dict()
for i in l:
    a,b=i.split(':')
    d[a]=b
print(d)
for i in d:
    s=0
    for j in d[i]:
        s+=int(j)**2
    if(s%2==0):
        a=i[len(i)-1]+i[:len(i)-1]
    else:
        a=i[2:]+i[:2]
    print(a)