def fun(s):
    s=str(s)
    while(True):
        if(s[-1]=='0'):
            s=s[:-1]
        else:
            return int(s)
num=int(input())
# l=list()
# while(True):
#     while(True):
#         if(num[-1]=='0'):
#             num=num[:-1]
#         else:
#             break
#     l.append(int(num))
#     if(int(num)+1 not in l):
#         num=str(int(num)+1)
#     else:
#         print("IN")
#         break
# print(l)
# print(len(l))
c=0
l=[0]*10
print(l)
l[0]=1
while(True):
    if(str(num)[-1]=='0'):
        num=fun(num)
    if(num<10):
        # print(type(num))
        if(l[num]==1):
            break
        else:
            # print("in")
            l[num]=1
    if(num>10):
        c+=10-(num%10)
        num+=10-(num%10)
    else:
        num+=1
        c+=1
    # print("num : ",num," c : ",c)
    # print(l)
print(c)
