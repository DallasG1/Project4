import hashlib
import sqlite3


def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_db():
    """Initialize the SQLite database and create the users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


user_file = "Users.txt"
with open(user_file, "r") as file:
    users = file.read()
    print(users)


def register_user(username: str, email: str, password: str):
    """Register a new user with a username, email, and password."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))
        conn.commit()
        print(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print(
            f"Username {username} already exists. Choose a different username.")
    conn.close()


# def load_users():
#     """Load users from the user file."""
#     users = {}
#     if not os.path.exists(user_file):
#         return users

#     with open(user_file, "r") as file:
#         for line in file:
#             parts = line.strip().split()
#             if len(parts) != 3:
#                 continue  # skip empty or malformed lines
#             username, email, hashed_password = parts
#             users[username] = {
#                 "username": username,
#                 "password": hashed_password
#             }
#     return users


def verify_user(username: str, password: str) -> bool:
    """Verify a user's credentials."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    print(users)

    if result and result[0] == hash_password(password):
        return True
    return False


def login_user():
    """Login a user with a username and password."""
    username = input("Enter your username: ")

    # input("Enter your password: ")
    password = input("Enter your password: ")
    if verify_user(username, password):
        print(f"User {username} logged in successfully.")
    else:
        print("Invalid username or password.")


def main():
    """Main function to run the user login and registration system."""
    initialize_db()
    print("Welcome to the User Login System!")
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
