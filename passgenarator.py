"""Generate a random password from character types the user picks."""

import string
import secrets


CHARACTER_TYPES = [
    ("uppercase letters", string.ascii_uppercase),
    ("lowercase letters", string.ascii_lowercase),
    ("numbers", string.digits),
    ("special characters", string.punctuation),
]


def ask_yes_no(prompt: str) -> bool:
    """Return True when the user answers y or yes, in any case."""
    return input(prompt).strip().lower().startswith("y")


def get_character_pool() -> str:
    """Ask which character types to include and return the allowed characters."""
    print("\nChoose character types:")

    characters = ""
    for label, pool in CHARACTER_TYPES:
        if ask_yes_no(f"Include {label}? (y/n): "):
            characters += pool

    return characters


def generate_password(length: int, characters: str) -> str:
    """Return a password of the given length using secrets-safe randomness."""
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:

    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Error: Password length must be a whole number.")
        return

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
