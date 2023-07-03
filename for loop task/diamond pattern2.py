user = int(input("enter the number of rows:"))
user+=1
number=1
for i in range(user, 0, -1):
    print(" " * i, end="")
    for j in range(0,user-i):
        print(number, end=" ")
        number+=1
    print()