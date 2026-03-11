'''Write a program to create function which shall accept any number of
arguments and display total of all the numbers given as argument.'''

def total_sum(*numbers):
    total = sum(numbers)
    print("Total of all numbers:", total)

total_sum(10,2,4,3,5)
total_sum(20,3,0,6,5)
total_sum()
