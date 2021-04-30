l=[]
a="k"
while(1):
    a=input()
    if(a=='Q' or a=="q"):
        break
    l.append(a)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i]," VS ",l[j])