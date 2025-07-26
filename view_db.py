import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('SELECT name, price, category FROM books')
books = cursor.fetchall()

print(f'Total books: {len(books)}')

for book in books:
    name, price, category = book
    print(f'Book: {name}, Price: {price}, Category: {category}')

conn.close()