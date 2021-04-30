#34,89,6,321,53,45,2211,81
l=input().split(',')
print(l)
digit_sum=[]
for i in l:
    s=0
    for j in i:
        s+=int(j)
    digit_sum.append(s)
print(digit_sum)
ack=[]
res=0
for i in digit_sum:
    c=digit_sum.count(i)
    if(c>=2 and i not in ack):
        res+=c*(c-1)//2
        ack.append(i)
print(res) 
