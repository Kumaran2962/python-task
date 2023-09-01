def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def reduce(x):
    return x/2

def add_percentage(x, y):
    percentage_value = (y / 100) * x
    return x + percentage_value

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reduce to half")
    print("6. Add with Percentage")

    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    num1 = float(input("Enter first number: "))
    if choice!=5:
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == "5":
        print(num1, "/", 2, "=", reduce(num1))
    elif choice == '6':
        print(f"{num2}% of {num1} added to {num1} =", add_percentage(num1, num2))
    else:
        print("Invalid input")
