def fun(l,i):
    try:
        o=[0]*len(l)
        o[i]=l[i]/int(l[i+1])
        return o
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("Division by zero")
    finally:
        print("End of functoion")
try:
    l1=[2,3,'6',2,8]
    l2=fun(l1,4)
except TypeError:
    print("Invalid type")
except IndexError:
    print("Invalid Index")
finally:
    print("End of program")