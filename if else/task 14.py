a=int(input("enter the first angle:"))
b=int(input("enter the second angle:"))
c=int(input("enter the third angle:"))
if (a+b>c and a+c>b and b+c>a):
    print("the triangle is valid")
else:
    print("the triangle is invalid")