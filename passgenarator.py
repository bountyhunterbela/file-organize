"""Generate a random password from character types the user picks."""

import string
import secrets


def get_character_pool() -> str:
    """Ask which character types to include and return the allowed characters."""
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


def generate_password(length: int, characters: str) -> str:
    """Return a password of the given length using secrets-safe randomness."""
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:

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


if __name__ == "__main__":
    main()
