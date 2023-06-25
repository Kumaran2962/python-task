a=int(input("enter the number of natural number to be printed: "))
b=0
for i in range (1,a+1):
    print(2*i-1)
    b+=(2*i-1)
print("the sum of n odd natural numbers is: ",b)