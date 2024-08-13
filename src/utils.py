# src/utils.py

import random
import string

def get_charset(include_uppercase=True, include_digits=True, include_symbols=True):
    """Returns a character set based on user preferences."""
    charset = string.ascii_lowercase
    if include_uppercase:
        charset += string.ascii_uppercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        charset += string.punctuation
    return charset

def generate_random_password(length, charset):
    """Generates a random password of the specified length using the given charset."""
    return ''.join(random.choice(charset) for _ in range(length))

def validate_input(length):
    """Validates the length input to ensure it is a positive integer."""
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Password length must be a positive integer.")
