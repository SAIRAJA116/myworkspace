s=input()
while(1):
    t=s[::-1]
    if(s==t):
        print(s)
        print(len(s))
        break
    else:
        s=int(s)+int(t)
        s=str(s)
