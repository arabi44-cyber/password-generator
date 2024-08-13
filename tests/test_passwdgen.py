import unittest
from passwdgen import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_password_length(self):
        password = generate_password(length=12)
        self.assertEqual(len(password), 12, "Password length should be 12 characters")

    def test_inclusion_of_digits(self):
        password = generate_password(length=12, include_digits=True)
        self.assertTrue(any(char.isdigit() for char in password), "Password should include digits")

    def test_inclusion_of_special_characters(self):
        password = generate_password(length=12, include_special_chars=True)
        self.assertTrue(any(not char.isalnum() for char in password), "Password should include special characters")

    def test_exclusion_of_special_characters(self):
        password = generate_password(length=12, include_special_chars=False)
        self.assertFalse(any(not char.isalnum() for char in password), "Password should not include special characters")

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=-1)

    def test_default_password_generation(self):
        password = generate_password()
        self.assertTrue(len(password) > 0, "Default password should be generated with a positive length")

if __name__ == '__main__':
    unittest.main()
