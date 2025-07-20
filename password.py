import random
import string


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character set!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("🔐 Welcome to the Random Password Generator! 🔐")

try:
    length = int(input("Enter desired password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
except ValueError:
    print("Please enter a valid number for length.")
