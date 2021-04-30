s=input()
if(s==""):
    print("INVALID INPUT")
else:
    l=[]
    l[:0]=s

    a=e=i=o=u=0
    flag=0

    for j in range(0,len(l)):
        if(l[j]=='a' or l[j]=="A"):
            a+=1
            l[j]=""
            flag+=1
            
        elif(l[j]=='e'or l[j]=="E"):
            e+=1
            l[j]=""
            flag+=1
        elif(l[j]=='i'or l[j]=="I"):
            i+=1
            l[j]=""
            flag+=1
        
        elif(l[j]=='o'or l[j]=="O"):
            o+=1
            l[j]=""
            flag+=1
        elif(l[j]=='u'or l[j]=="U"):
            u+=1
            l[j]=""
            flag+=1

    if(flag!=0):
        print(a)
        print(e)
        print(i)
        print(o)
        print(u)

        a="".join(l)
        print(a)
    else:
        print("0")