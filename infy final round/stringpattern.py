l=input().split()
v=['a','e','i','o','u']
for i in range(0,len(l)):
    l[i]=l[i].lower()
flag=1
for i in l:
    flag=1
    for j in range(len(i)-1):
        if(((i[j] in v) and (i[j+1] in v)) or ((i[j] not in v) and (i[j+1] not in v))):
            flag=0
            break
    if(flag==0):
        print("Invalid")
    else:
        print("Valid")