a=(input("enter your number: ")).split(" ")
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
print(a[1])