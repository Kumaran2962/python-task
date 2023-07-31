a = int(input("enter the number:"))
b = int(0)
while a != 0:
    temp = int(a % 10)
    b = b+temp
    a = a/10
string = str(b)
string_rev = string[:: -1]
if string == string_rev:
    print("Yes")
else:
    print("No")