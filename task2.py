
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
def add_user(new_user):
    users.append(new_user)
    print(f"User added: {new_user}")

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User updated: {user}")
            return
    print("User not found.")

def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    print(f"User with ID {user_id} deleted.")

def list_users():
    print("User List:")
    for user in users:
        print(user)

def main():
    while True:
        print("1. List all users")
        print("2. Add a user")
        print("3. Get user by ID")
        print("4. Update user")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            list_users()

        elif choice == '2':
            try:
                user_id = int(input("Enter user ID: "))
                name = input("Enter name: ")
                email = input("Enter email: ")
                add_user({"id": user_id, "name": name, "email": email})
            except ValueError:
                print("Invalid input.")

        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to retrieve: "))
                user = get_user_by_id(user_id)
                if user:
                    print(user)
                else:
                    print("User not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to update: "))
                name = input("Enter new name: ")
                email = input("Enter new email: ")
                update_user(user_id, name or None, email or None)
            except ValueError:
                print("Invalid input.")

        elif choice == '5':
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("Invalid input.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
