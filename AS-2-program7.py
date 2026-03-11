'''Menu Driven Program: Student Result
System
Operations:
Enter Marks
Calculate Percentage
Assign Grade'''

marks = []

def enter_marks():
    global marks
    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks of subject {i}: "))
        marks.append(m)

def calculate_percentage():
    if len(marks) == 0:
        print("Please enter marks first!")
        return None
    total = sum(marks)
    per = total / 5
    return per

def assign_grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"


while True:
    print("\n1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enter_marks()
    elif choice == 2:
        percentage = calculate_percentage()
        if percentage is not None:
            print("Percentage =", percentage)
    elif choice == 3:
        percentage = calculate_percentage()
        if percentage is not None:
            print("Grade =", assign_grade(percentage))
    elif choice == 4:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
