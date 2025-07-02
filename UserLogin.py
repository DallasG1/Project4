import os
import hashlib
import getpass


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


user_file = "Users.txt"
with open(user_file, "r") as file:
    users = file.read()
    print(users)


def register_user(username: str, email: str, password: str):
    """Register a new user with a username, email, and password."""
    hashed_password = hash_password(password)
    with open(user_file, "a") as file:
        file.write(f"{username} {email} {hashed_password}\n")
    print(f"User {username} registered successfully.")


def load_users():
    """Load users from the user file."""
    users = {}
    if not os.path.exists(user_file):
        return users

    with open(user_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 3:
                continue  # skip empty or malformed lines
            username, email, hashed_password = parts
            users[username] = {
                "username": username,
                "password": hashed_password
            }
    return users


def verify_user(username: str, password: str) -> bool:
    """Verify a user's credentials."""
    users = load_users()
    hashed_password = hash_password(password)
    print(users)
    if username in users and users[username]["password"] == hashed_password:
        return True
    return False


def login_user():
    """Login a user with a username and password."""
    username = input("Enter your username: ")

    # input("Enter your password: ")
    password = getpass.getpass("Enter your password: ")
    if verify_user(username, password):
        print(f"User {username} logged in successfully.")
    else:
        print("Invalid username or password.")


def main():
    while True:
        choice = input(
            "Enter '1' to login or '2' to register or '3' to Exit: ")
        if choice == '1':

            login_user()

        elif choice == '2':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            register_user(username, email, password)
            print(f"User {username} registered successfully.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
