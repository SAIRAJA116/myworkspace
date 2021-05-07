n=input()
words=1
c=0
w=0
for i in n:
    if(i.isalnum()):
        c+=1
    elif(i.isspace()):
        w+=1
        words+=1

print(words)
print(c+w)
# print(w)n