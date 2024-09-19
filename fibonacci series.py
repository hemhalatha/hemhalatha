#fibonacci series
a,b,x=0,1,0
print(a,b,end=" ")
while a+b<1001:
    x=a+b
    print(x,end=" ")
    a=b
    b=x
