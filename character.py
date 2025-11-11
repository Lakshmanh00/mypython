Check whether the entered character is a vowel, consonant, digit, or special character
ch = input("Enter a single character: ")

if ch.isalpha():
    if ch.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
