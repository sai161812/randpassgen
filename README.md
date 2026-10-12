# Random password generator

A Python CLI that selects each character independently using `secrets.choice`, backed by the operating system's cryptographic random source. No third-party packages or network access are required.

## Run

Requires Python 3.6 or newer.

```sh
python passgen.py --length 24
```

Omit `--length` for the interactive length prompt. Invalid lengths and missing interactive input exit with status 2; successful generation exits with status 0. The flag-based form prints only the password to stdout.

The alphabet contains ASCII lowercase and uppercase letters, digits, and `!@#$%&*`. Lengths from 1 to 4096 are accepted; a permitted length is not a recommendation. Characters can repeat, so passwords can be longer than the alphabet. Random selection does not guarantee every character category occurs in every password.

Passwords are printed to your terminal. Avoid directing real credentials into logs, shared screens, or committed files. This tool does not store or manage passwords.

## Verify

```sh
python -m unittest discover -s tests -v
```

Checks cover the randomness API, alphabet, boundary lengths, invalid input, interactive mode, and subprocess exit/output behavior.
