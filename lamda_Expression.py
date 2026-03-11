'''10.Write a program to create 4 lambda functions which shall accept 2
numbers and one arithmetic operator. As per arithmetic operator related
lambda functions shall be invoked.'''


add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b if b!= 0 else "Division by zero not allowed"

num1=float(input("Enter the First Number:="))
num2=float(input("Enter the Second Number:="))
operator=input("Enter the arithmetic Operator(+,-,*,/) :")

operations = {
        '+':add,
        '-':sub,
        '*':mul,
        '/':div
        }

if operator in operations:
        result=operations[operator](num1,num2)
        print("Result:=",result)
else:
    print("Invalid operator")
