import sqlite3
from sqlite3 import Error

# --- Database Setup Functions ---
def connect_db():
    try:
        conn = sqlite3.connect('ebookstore.db')
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

def create_tables():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT NOT NULL
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            authorID INTEGER,
            qty INTEGER NOT NULL,
            FOREIGN KEY (authorID) REFERENCES author(id)
        )''')
        conn.commit()

def populate_initial_data():
    authors = [
        (1290, 'Charles Dickens', 'England'),
        (8937, 'J.K. Rowling', 'England'),
        (2356, 'C.S. Lewis', 'Ireland'),
        (6380, 'J.R.R. Tolkien', 'South Africa'),
        (5620, 'Lewis Carroll', 'England')
    ]

    books = [
        (3001, 'A Tale of Two Cities', 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
        (3004, 'The Lord of the Rings', 6380, 37),
        (3005, "Alice’s Adventures in Wonderland", 5620, 12)
    ]

    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.executemany('INSERT OR IGNORE INTO author VALUES (?, ?, ?)', authors)
        cursor.executemany('INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)', books)
        conn.commit()

# --- Validation ---
def is_valid_id(id_str):
    return id_str.isdigit() and len(id_str) == 4

# --- CRUD Operations ---
def add_book():
    try:
        book_id = input("Enter Book ID (4-digit number): ")
        if not is_valid_id(book_id):
            print("Invalid Book ID. It must be a 4-digit number.")
            return

        title = input("Enter Book Title: ").strip()
        if not title:
            print("Book title cannot be empty.")
            return

        author_id = input("Enter Author ID (4-digit number): ")
        if not is_valid_id(author_id):
            print("Invalid Author ID. It must be a 4-digit number.")
            return

        qty_input = input("Enter Quantity: ")
        if not qty_input.isdigit():
            print("Quantity must be a positive number.")
            return
        qty = int(qty_input)

        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM author WHERE id = ?", (int(author_id),))
            if not cursor.fetchone():
                print("Author ID does not exist in the author table.")
                return

            cursor.execute('INSERT INTO book VALUES (?, ?, ?, ?)', (int(book_id), title, int(author_id), qty))
            conn.commit()
            print("\u2705 Book added successfully.")

    except Error as e:
        print(f"\u274C Database error: {e}")

def update_book():
    try:
        book_id = input("Enter Book ID to update: ")
        if not is_valid_id(book_id):
            print("Invalid Book ID.")
            return

        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT book.title, author.name, author.country
                              FROM book
                              INNER JOIN author ON book.authorID = author.id
                              WHERE book.id = ?''', (int(book_id),))
            result = cursor.fetchone()

            if not result:
                print("Book not found.")
                return

            print(f"Current Title: {result[0]}\nAuthor: {result[1]}\nCountry: {result[2]}")
            print("What would you like to update?\n1. Title\n2. Quantity\n3. Author Name\n4. Author Country")
            choice = input("Enter choice: ")

            if choice == '1':
                new_title = input("Enter new title: ")
                cursor.execute('UPDATE book SET title = ? WHERE id = ?', (new_title, int(book_id)))
            elif choice == '2':
                new_qty = input("Enter new quantity: ")
                if not new_qty.isdigit():
                    print("Quantity must be a number.")
                    return
                cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (int(new_qty), int(book_id)))
            elif choice == '3':
                new_name = input("Enter new author name: ")
                author_id = get_author_id_by_book_id(int(book_id))
                if author_id is None:
                    print("Cannot update author name: Author not found.")
                    return
                cursor.execute('UPDATE author SET name = ? WHERE id = ?', (new_name, author_id))
            elif choice == '4':
                new_country = input("Enter new author country: ")
                author_id = get_author_id_by_book_id(int(book_id))
                if author_id is None:
                    print("Cannot update author country: Author not found.")
                    return
                cursor.execute('UPDATE author SET country = ? WHERE id = ?', (new_country, author_id))
            else:
                print("Invalid choice.")
                return

            conn.commit()
            print("\u2705 Update successful.")
    except Error as e:
        print(f"\u274C Error: {e}")

def get_author_id_by_book_id(book_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT authorID FROM book WHERE id = ?', (book_id,))
        result = cursor.fetchone()
        return result[0] if result else None

def delete_book():
    try:
        book_id = input("Enter Book ID to delete: ")
        if not is_valid_id(book_id):
            print("Invalid Book ID.")
            return

        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM book WHERE id = ?', (int(book_id),))
            conn.commit()
            print("\u2705 Book deleted successfully.")
    except Error as e:
        print(f"\u274C Database error: {e}")

def search_books():
    title = input("Enter book title to search: ").strip()
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM book WHERE title LIKE ?', ('%' + title + '%',))
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No books found.")

def view_details():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT book.id, book.title, author.name, author.country, book.qty
                          FROM book
                          INNER JOIN author ON book.authorID = author.id''')
        results = cursor.fetchall()
        if results:
            for row in results:
                print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Country: {row[3]}, Quantity: {row[4]}")
        else:
            print("No books found.")
# --- Main Menu ---
def main():
    create_tables()
    populate_initial_data()

    while True:
        print("""
        Menu
        1. Enter book
        2. Update book
        3. Delete book
        4. Search books
        5. View details of all books
        0. Exit
        """)
        option = input("Enter option: ")

        if option == '1':
            add_book()
        elif option == '2':
            update_book()
        elif option == '3':
            delete_book()
        elif option == '4':
            search_books()
        elif option == '5':
            view_details()
        elif option == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()

# end of code