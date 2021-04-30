str=input()
a=[')','}',']']
dic={'(':')','{':'}','[':']'}
stack=[]
top=-1
for i in range(len(str)):
    if(i==0):
        stack.append(str[i])
        top+=1
    else:
        if(str[i] in a):
            if(dic[stack[top]]==str[i]):
                stack.pop()
                top-=1
            else:
                print(i+1)
                break
        else:
            stack.append(str[i])
            top+=1
    print(stack," -> ",i)
if(len(stack)!=0):
    print(len(str)+1)

