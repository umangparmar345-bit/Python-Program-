#Write a program to demonstrate the use of break statement

fruits = ["Apple", "Banana", "Mango", "grapes", "orange"]

for i in fruits:
    print(i)  
    if i == "orange":
        print("Found Orange! Stopping the loop")
        break
