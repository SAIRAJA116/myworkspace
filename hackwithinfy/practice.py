def fun(l):
    s=list()
    for i in l:
        if i not in s:
            s.append(i)
    d=dict()
    for i in s:
        d[i] = l.count(i)      
    ss=sorted(d,key=d.get,reverse=True)
    for i in ss:
        print(i,"=",d[i])
        
s=input()
fun(s)