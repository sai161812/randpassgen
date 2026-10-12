"""Generate passwords using the operating system's cryptographic randomness."""
import argparse
import sys
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


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, help=f"Password length (1–{MAX_LENGTH}); prompts if omitted")
    args = parser.parse_args(argv)
    try:
        length = args.length if args.length is not None else int(input("Enter the length of your password: "))
        password = generate_password(length)
    except (ValueError, EOFError) as error:
        print(f"Error: {error or 'No password length provided.'}", file=sys.stderr)
        return 2
    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
