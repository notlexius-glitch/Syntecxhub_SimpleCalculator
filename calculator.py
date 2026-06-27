def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("----------------Welcome to the Simple Calculator----------------")

while True:

    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    operator = input("Choose (+, -, *, /): ")

    if operator == "+":
       print("Result:", add(num1, num2))

    elif operator == "-":
       print("Result:", subtract(num1, num2))

    elif operator == "*":
        print("Result:", multiply(num1, num2))

    elif operator == "/":
        print("Result:", divide(num1, num2))

    else:
        print("Invalid Operator")

    choice = input("Do you want to calculate again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the calculator!")
        break