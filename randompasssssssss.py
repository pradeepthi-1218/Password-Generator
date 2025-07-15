import random
import string

print("Welcome to the Random Password Generator!")

try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length must be a positive number.")
    else:
        include_letters = input("Include letters? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        characters = ""

        if include_letters:
            characters += string.ascii_letters  
        if include_numbers:
            characters += string.digits         
        if include_symbols:
            characters += string.punctuation    

        if not characters:
            print("You must select at least one character type!")
        else:
            password = "".join(random.choice(characters) for _ in range(length))

            print(f"\nGenerated Password: {password}")

except ValueError:
    print("Please enter a valid number for password length.")
