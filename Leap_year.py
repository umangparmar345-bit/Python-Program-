#Write a program to check whether a given year is a leap year.

year=int(input("Enter the Year:="))

if year%4==0:
    print("Year",year,"is Leap Year")
else:
    print("Year",year,"is not Leap Year")
