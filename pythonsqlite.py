import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('crud_app.db')
c = conn.cursor()

# Create table
c.execute('CREATE TABLE IF NOT EXISTS users  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')

# Function to create a new user
def create_user(name, email):
    c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))
    conn.commit()
            
def update_user(user_id, name=None, email=None):
    if name:
        c.execute('''UPDATE users SET name = ? WHERE id = ?''', (name, user_id))
    if email:
        c.execute('''UPDATE users SET email = ? WHERE id = ?''', (email, user_id))
    conn.commit()

# Function to delete a user by ID
def delete_user(user_id):
    c.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    conn.commit()
create_user("Alice", "alice@example.com")
create_user("Bob", "bob@example.com")