l=list(map(int,input().split()))
s=list(set(l))
print(l)
print(s)
if(len(s)==1):
    print(s[0])
else:
    d=""
    longest=0
    for i in s:
        sum=0
        j=l.index(i)
        while(j < len(l)):
            if(i==l[j]):
                sum+=1
                j+=2
            else:
                j=j+1
        if(sum>longest):
            longest=sum
            c=i
print(c)
            