'''Function to Find Largest of Three Numbers
Accept three numbers as parameters.
Return the largest number'''
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c



x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

print("Largest number is:", largest(x, y, z))
