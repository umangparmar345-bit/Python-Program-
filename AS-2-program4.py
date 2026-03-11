'''Function with Default Arguments
Write a function to calculate simple interest.
Keep rate default as 5%'''
def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si


principal = float(input("Enter Principal: "))
time = float(input("Enter Time (years): "))

print("Simple Interest =", simple_interest(principal, time))
    
