user = int(input("enter the number of rows:"))
user+=1
for i in range(user, 0, -1):
    print(" " * i, end="")
    for j in range(2*(user-i)-1):
        print("#", end=" ")
    print()