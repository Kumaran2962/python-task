a=int(input("enter the number:"))
b=a
d=len(str(a))
sum=0
while a!=0:
    c=a%10
    sum+=(c**d)
    a=a//10
print(sum)
if b==sum:
    print("Yes")
else:
    print("No")