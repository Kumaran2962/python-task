a1=int(input("enter you first number: "))
a2=int(input("enter you second number: "))
a3=int(input("enter you third number: "))
if(a1<a2<a3):
    print("1st number=",a1)
if(a2<a3):
    print("2nd number=",a2)
if(a3>a2>a1):
    print("3rd number=",a3)
    print("the 3rd number is greatest among three",a3)