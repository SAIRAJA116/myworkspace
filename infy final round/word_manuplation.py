str = input()
print(str)
temp = str.upper()
s = set(temp)
s = list(s)
s.sort()
print(s)
l=[]

for i in s:
    a=''
    for j in range(len(temp)):
        if(i==temp[j]):
            a+=str[j]
    l.append(a)
print(l)
low=0
high = len(l)-1
newstr=""
while(low<high):
    newstr+=l[low]+l[high]
    low+=1
    high=high-1
if(l[low]==l[high]):
    newstr+=l[low]
print(newstr)