"""Generate passwords using the operating system's cryptographic randomness."""
import secrets
import string

ALPHABET = string.ascii_letters + string.digits + "!@#$%&*"


def generate_password(length):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def main():
    length = int(input("Enter the length of your password: "))
    print(generate_password(length))


if __name__ == "__main__":
    main()
