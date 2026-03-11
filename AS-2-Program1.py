'''Write a Function to Perform Arithmetic Operations
Create separate functions for addition,subtraction, multiplication and division
Call them based on user input.'''

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result =", addition(a, b))
elif choice == 2:
    print("Result =", subtraction(a, b))
elif choice == 3:
    print("Result =", multiplication(a, b))
elif choice == 4:
    print("Result =", division(a, b))
else:
    print("Invalid Choice")
