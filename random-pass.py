#!/usr/bin/env python
"""random password"""
import random
import string
import sys

uppercase_characters = [x for x in string.ascii_uppercase]
lowercase_characters = [x for x in string.ascii_lowercase]
numbers = [str(x) for x in range(50)]
special_char = [x for x in string.punctuation]

def generate_password(length):
    """Generate a random password with specified length."""
    characters = uppercase_characters + lowercase_characters + numbers + special_char
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    """Get the desired length of the password."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == '__main__':
    password_length = get_password_length()
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
