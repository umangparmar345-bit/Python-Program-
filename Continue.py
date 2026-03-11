#Write a program to demonstrate the use of continue statement.

x=[10,20,33,44,55,65,99,20,22]

for i in x:
    if i%2!=0:
        continue
    print(i,end="\n")
