a=int(input("enter the first angle:"))
b=int(input("enter the second angle:"))
c=int(input("enter the third angle:"))
if (a==b==c):
    print("it is Equilateral triangle")
elif (a==b or b==c or a==c):
    print("it is Isoscles triangle")
else:
    print("it is scalene triangle")        