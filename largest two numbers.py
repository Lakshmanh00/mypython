 Program to find the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"{a} is the largest number.")
elif a < b:
    print(f"{b} is the largest number.")
else:
    print("Both numbers are equal.")
