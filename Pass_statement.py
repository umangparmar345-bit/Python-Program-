#Write a program to demonstrate the use of pass statement inside a loop.

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]

for fruit in fruits:
    if fruit == "Banana":
        pass
    else:
        print(f"I like {fruit}")
