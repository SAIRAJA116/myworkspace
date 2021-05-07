# def fun(l):
#     s=list()
#     for i in l:
#         if i not in s:
#             s.append(i)
#     d=dict()
#     for i in s:
#         d[i] = l.count(i)      
#     ss=sorted(d,key=d.get,reverse=True)
#     for i in ss:
#         print(i,"=",d[i])
        
# s=input()
# fun(s)
def fun(a,b):
    if(a==0):
        return
    global s
    s=s+a
    print(s)
    print(a+b)
    fun(a-1,b-1)

s=0
a,b=map(int,input().split())
fun(a,b)
print(s)