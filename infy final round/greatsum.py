import itertools
l = list(map(int,input().split()))
s=int(input())
tl=list(itertools.combinations(l,4))
c=0
for i in tl:
    if sum(i)==s:
        c+=1
print(c)