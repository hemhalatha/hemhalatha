#palindrome
x=int(input("Enter a number="))
k=x
no=0
while x>0:
    no=no*10+x%10
    x=x//10

print("The reverse=",no)
if no==k:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")