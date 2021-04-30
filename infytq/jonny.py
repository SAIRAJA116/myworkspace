class A :
    def __init__(self):
        print("Parent class")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child class")

o=B()
