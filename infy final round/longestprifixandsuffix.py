str=input()
prefix=str[0]
s=str.replace(prefix,"",1)
s_i = s.rfind(prefix)+len(prefix)
if(s_i-len(prefix)==-1):
    print(-1)
else:
    longest=0
    suffix=str[s_i]
    print(prefix," ",0," ",suffix," ",s_i)
    if(s_i==len(str)-1):
        i=1
        j=len(str)-2
        while(prefix==suffix and len(prefix)<=len(str)//2):
            longest=len(prefix)
            prefix+=str[i]
            suffix+=str[j]
            i+=1
            j-=1
        print(longest)
    else:
        suffix=str[s_i:len(str)]
        prefix=str[0:len(suffix)]
        print(prefix)
        print(suffix)
        if(prefix==suffix):
            print(len(prefix))
        else:
            print(-1)
