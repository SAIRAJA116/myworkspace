l = list(map(int,input().split(',')))
a=sum(l[0:l.index(5)])+sum(l[l.index(8)+1:])
s=''
for i in range(l.index(5),(l.index(8))+1):
    s+=str(l[i])


print(a+int(s))