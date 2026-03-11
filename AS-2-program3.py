'''Function to Calculate Factorial (Using Recursion)
Implement factorial using:
Normal function
Recursive function'''

def factorial_normal(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Recursive Function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial not defined for negative numbers")
else:
    print("Factorial (Normal) =", factorial_normal(num))
    print("Factorial (Recursive) =", factorial_recursive(num))
