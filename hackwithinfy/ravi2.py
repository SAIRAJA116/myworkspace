def fun(a,b):
    if(b in a):
        i=a.index(b)
        a=a[:i]+a[i+len(b):]
        return fun(a,b)
    else:
        return len(a)
a=input()
b=input()
print(fun(a,b))