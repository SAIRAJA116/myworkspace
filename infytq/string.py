str = "helloworld"
# print(str[0:])
# print(str[-2:])

i='e'
while i in str:
    str = str[-2:]
    print(str)
    # print(i,end=" ")