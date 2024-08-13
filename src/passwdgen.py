import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter the password length (8-16): "))
            if 8 <= length <= 16:
                return length
            else:
                print("Password length must be between 8 and 16 characters.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_set():
    character_set = ""
    while True:
        print("Choose character set for password:")
        print("1. Digits")
        print("2. Letters")
        print("3. Special characters")
        print("4. Exit")
        choice = input("Pick a number: ")
        if choice == "1":
            character_set += string.digits
        elif choice == "2":
            character_set += string.ascii_letters
        elif choice == "3":
            character_set += string.punctuation
        elif choice == "4":
            if character_set:
                return character_set
            else:
                print("Please select at least one character set.")
        else:
            print("Invalid choice. Please try again.")

def generate_password(length, character_set):
    password = [random.choice(character_set) for _ in range(length)]
    return "".join(password)

def main():
    length = get_password_length()
    character_set = get_character_set()
    password = generate_password(length, character_set)
    print("The random password is:", password)

if __name__ == "__main__":
    main()