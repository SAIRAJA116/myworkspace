m,n=map(int,input().split())
s=input()
l,r=0,1
index=0
highest=-9999
while(r<len(s)):
    if(s[l]==s[r]):
        r+=1
        if(highest<r-l):
            highest=r-l
            index=l
            lastindex=r
        #print("break"," ",highest," ",l)
    elif(s[l]!=s[r]):
        l=r
        r+=1
    # print(l," ",r)
    s=list(s)
if(n<=index):
    for i in range(index-(n),index+1):
        s[i]=s[index]
elif(n>index and n+index<len(s)):
    for i in range(lastindex,n+lastindex):
        s[i]=s[index]

print("".join(s))

