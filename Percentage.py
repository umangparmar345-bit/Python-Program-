#write a program to display grade of a student based on percentage using if-elif-else.

percentage=float(input("Enter the Percentage:="))

if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>40:
    print("Grade E")
else:
    print("Fail")
