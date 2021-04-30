class Invalidlength(Exception):
    pass
class A:
    def __init__(self,n):
        self.n=n
    def fun(self):
        try:
            if(len(self.n)!=10):
                raise Invalidlength
            else:
                print("Valid number")
        except Invalidlength:
            print("Exception handled-Inside class")
        print("Inside a class")

o=A('12345')
try:
    o.fun()
    print("outside class")
except Invalidlength:
    print("Exception handled-outside class")
    