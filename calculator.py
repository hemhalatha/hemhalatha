print("CALCULATOR")
x=input("print 1 for add, 2 for sub, 3 for mul and 4 for division")
a=input("no1=")
b=input("no2=")
def add(a,b):
    print(a+b)
def sub(a,b):
    print(abs(a-b))
def mul(a,b):
    print(a*b)
def div(a,b):
    if b!=0:
        print(a//b)
    else:
        print("division by zero is not allowed")
match x:
    case 1:
        print( add(a,b))
    case 2:
        sub(a,b)
    case 3:
        mul(a,b)
    case 4:
        div(a,b)
    case _:
        print("invalid input")
