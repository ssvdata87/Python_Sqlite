import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('crud_app.db')
c = conn.cursor()

# Create table
c.execute('CREATE TABLE IF NOT EXISTS users  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')

# Function to create a new user
def create_user():
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")
    c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))
    conn.commit()
    print("User Successfully Created")
    
            
def update_user():
    user_id = int(input("Enter user ID: "))
    name = input("Enter new name (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    if name or email:
        if name:
            c.execute('''UPDATE users SET name = ? WHERE id = ?''', (name, user_id))
        if email:
            c.execute('''UPDATE users SET email = ? WHERE id = ?''', (email, user_id))
        conn.commit()
    else:
        print("No changes made.")


# Function to delete a user by ID
def delete_user():
    user_id=int(input("Enter UserID :"))
    c.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    conn.commit()

# Function to retrieve all users
def get_all_users():
    c.execute('''SELECT * FROM users''')
    return c.fetchall()

# Function to retrieve a user by ID
def get_user_by_id():
    user_id = int(input("Enter user ID: "))
    c.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
    return c.fetchone()

while True:
    print("\n1. Create user")
    print("2. Get all users")
    print("3. Get user by ID")
    print("4. Update user")
    print("5. Delete user")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        print("All users:")
        print(get_all_users())
    elif choice == '3':
        print("User details:")
        print(get_user_by_id())
    elif choice == '4':
        update_user()
    elif choice == '5':
        delete_user()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

# Close connection
conn.close()


