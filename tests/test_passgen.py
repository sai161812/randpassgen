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

    def test_invalid_lengths_are_rejected_before_random_generation(self):
        for length in (0, -1, 4097, True, 2.5, "16", None):
            with self.subTest(length=length), patch("passgen.secrets.choice") as choice:
                with self.assertRaises(ValueError):
                    generate_password(length)
                choice.assert_not_called()

    def test_maximum_length_is_supported(self):
        self.assertEqual(len(generate_password(4096)), 4096)
