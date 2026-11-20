
import string
import secrets


def get_character_pool():
    characters = ""

    print("\nChoose character types:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Special characters")

    if input("Include uppercase? (y/n): ").lower() == "y":
        characters += string.ascii_uppercase

    if input("Include lowercase? (y/n): ").lower() == "y":
        characters += string.ascii_lowercase

    if input("Include numbers? (y/n): ").lower() == "y":
        characters += string.digits

    if input("Include special characters? (y/n): ").lower() == "y":
        characters += string.punctuation

    return characters


def generate_password(length, characters):

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def main():

    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    length = int(input("Enter password length: "))

    characters = get_character_pool()

    if not characters:
        print("Error: Select at least one character type.")
        return

    if length < 1:
        print("Error: Password length must be positive.")
        return

    password = generate_password(length, characters)

    print("\nGenerated Password:", password)


main()
