s=input()
dic=dict()
a=''
for i in range(len(s)):
    if(not(s[i].isalnum())):
        dic[i]=s[i]
    else:
        a+=s[i]
print(dic)
length=len(s)
s=''
j=0
a=a[::-1]
for i in range(length):
    if(i not in dic):
        s+=a[j]
        j+=1
    else:
        s+=dic[i]
print(s)

































# s=input()
# # s=list(s)
# # print(s)
# d=dict()
# # l=[]
# for i in range(len(s)):
#     if(s[i].isalnum()==False):
#         d[s[i]]=i
        
# print(s)
# print(d)
# for i in d:
#     s=s.replace(i,"")
# print(s)
# s=s[::-1]
# s=list(s)
# for i in d:
#     s.insert(d[i],i)
# s="".join(s)
# print(s)

