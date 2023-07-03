x = float(input("Input the Value of x: "))
n = int(input("Input the number of terms: "))
sum = 1.0
t = 1.0

for i in range(1, n):
    d = (2 * i) * (2 * i - 1)
    t = -t * x * x / d
    sum += t

print("\nThe sum =", sum)
print("Number of terms =", n)
print("Value of x =", x)