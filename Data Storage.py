import sqlite3

db_file = 'data.db'

# Function to encode data to ASCII
def encode_data(data):
    return data.encode('ascii')

# Function to decode data from ASCII
def decode_data(data):
    return data.decode('ascii')

# Function to create database table
def create_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data
                      (title TEXT PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

# Function to add or update data in the database
def put_data(title, content):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    encoded_title = encode_data(title)
    encoded_content = encode_data(content)
    cursor.execute("INSERT OR REPLACE INTO data (title, content) VALUES (?, ?)", (encoded_title, encoded_content))
    conn.commit()
    conn.close()

# Function to retrieve data from the database
def get_data(title):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    encoded_title = encode_data(title)
    cursor.execute("SELECT content FROM data WHERE title=?", (encoded_title,))
    row = cursor.fetchone()
    conn.close()
    if row is not None:
        encoded_content = row[0]
        content = decode_data(encoded_content)
        return content
    else:
        return None

# Function to delete data from the database
def delete_data(title):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    encoded_title = encode_data(title)
    cursor.execute("DELETE FROM data WHERE title=?", (encoded_title,))
    conn.commit()
    conn.close()

# Function to list all data titles in the database
def list_data():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM data")
    rows = cursor.fetchall()
    conn.close()
    titles = []
    for row in rows:
        encoded_title = row[0]
        title = decode_data(encoded_title)
        titles.append(title)
    return titles

# Create database table if it does not exist
create_table()

# Main program loop
while True:
    print('Welcome to the key-value database')
    print('What do you want to do?')
    action = input('Enter P to [P]ut, G to [G]et, D to [D]elete, L to [L]ist or Q to [Q]uit: ').upper()
    if action == 'P':
        title = input('Enter title: ')
        content = input('Enter content: ')
        put_data(title, content)
    elif action == 'G':
        title = input('Enter title: ')
        content = get_data(title)
        if content is not None:
            print('Your content: %s' % content)
        else:
            print('No such title')
    elif action == 'D':
        title = input('Enter title: ')
        delete_data(title)
    elif action == 'L':
        titles = list_data()
        if titles:
            print('DB contents:')
            for title in titles:
                print('- %s' % title)
        else:
            print('DB is empty')
    elif action == 'Q':
        print('Bye')
        break
    else:
        print('Invalid input, try again')
