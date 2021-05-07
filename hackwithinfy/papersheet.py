h=int(input())
w=int(input())
h1=int(input())
w1=int(input())
count=0
while(True):
    count+=1
    if(h//2>=(h-h1)):
        h=h1
        print(h)
        break
    h=h-h//2
    
while(True):
    count+=1 
    if(w//2>=(w-w1)):
        w=w1
        break
    w=w-w//2
       
print(h," ",w)
print(count)