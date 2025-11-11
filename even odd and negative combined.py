# Check whether a number is even/odd and positive/negative
num = int(input("Enter a number: "))

if num == 0:
    print("The number is Zero (neither positive nor negative, but even)")
elif num > 0:
    if num % 2 == 0:
        print("The number is Even and Positive")
    else:
        print("The number is Odd and Positive")
else:
    if num % 2 == 0:
        print("The number is Even and Negative")
    else:
        print("The number is Odd and Negative"
