l=input().split(',')
d=dict()
for i in l:
    a,b=i.split(':')
    d[a]=sorted(list(map(int,b)),reverse=True)
print(d)
password=''
for i in d:
    longest=0
    print(d[i])
    for j in d[i]:
        if(j>longest and j<=len(i)):
            longest=j
    if(longest==0):
        password+='X'
    else:
        print(i," ",longest)
        password+= i[longest-1]
print(password)
    