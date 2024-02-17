import random
import string

def generate_password(length):
    """
    Generate a random password of a specified length.

    Parameters:
    length (int): The length of the password.

    Returns:
    str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    print("----------------------------------------")
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
