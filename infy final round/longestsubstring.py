s = input()
longest=-1
win=""
for i in s:
    if((i not in win) and (len(win)==len(set(win)))):
        win+=i
    else:
        win = win[1:]+i
    length=len(win)
    if(length>longest):
        longest=length
    print(win," ",longest)
print(longest)