a=int(input("enter the number of natural number to be printed: "))
b=0
print("the even numbers are:")
for i in range (1,a+1):
    print(2*i)
    b+=(2*i)
print("the sum of n odd natural numbers is: ",b)