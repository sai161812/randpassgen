import unittest
from unittest.mock import patch

from passgen import ALPHABET, generate_password


class PasswordTests(unittest.TestCase):
    def test_uses_cryptographic_choice_for_each_character(self):
        with patch("passgen.secrets.choice", return_value="a") as choice:
            self.assertEqual(generate_password(20), "a" * 20)
            self.assertEqual(choice.call_count, 20)
            choice.assert_called_with(ALPHABET)

    def test_password_length_and_alphabet(self):
        for length in (1, 16, 100):
            password = generate_password(length)
            self.assertEqual(len(password), length)
            self.assertTrue(set(password) <= set(ALPHABET))
