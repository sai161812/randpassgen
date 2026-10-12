"""Generate passwords using the operating system's cryptographic randomness."""
import secrets
import string

ALPHABET = string.ascii_letters + string.digits + "!@#$%&*"


MAX_LENGTH = 4096


def generate_password(length):
    if isinstance(length, bool) or not isinstance(length, int):
        raise ValueError("Password length must be an integer.")
    if not 1 <= length <= MAX_LENGTH:
        raise ValueError(f"Password length must be between 1 and {MAX_LENGTH}.")
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main():
    length = int(input("Enter the length of your password: "))
    print(generate_password(length))


if __name__ == "__main__":
    main()
