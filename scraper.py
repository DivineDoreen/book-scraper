import requests
from bs4 import BeautifulSoup
import sqlite3
import time


conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS books')
cursor.execute("""
    CREATE TABLE books (
        name TEXT,
        price REAL,
        category TEXT
    )
""")
conn.commit()

base_url = 'http://books.toscrape.com'
url = base_url
page_count = 0
max_pages = 50

while url and page_count < max_pages:
    response  = requests.get(url, timeout=7)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        print(f'Fetching: {url}')
    else:
        print(f'Failed to fetch {url}, Error code: {response.status_code}')
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    print(f'found {len(books)} books')

    for book in books:
        name = book.find('h3').find('a')['title']
        price = float(book.find('p', class_='price_color').text.replace('£', ''))

        book_url = book.find('h3').find('a')['href']
        if book_url.startswith('catalogue/'):
            book_url = base_url + '/' + book_url
        else: book_url = base_url + '/catalogue/' + book_url

        try:
            book_response = requests.get(book_url, timeout=7)
            book_response.encoding = 'utf-8'
            book_response.raise_for_status()
            book_soup = BeautifulSoup(book_response.text, 'html.parser')
            breadcrumb = book_soup.find('ul', class_='breadcrumb')
            category = breadcrumb.find_all('li')[2].find('a').text
        except requests.exceptions.RequestException as e:
            print(f'Error Fetching {book_url} : {e}')
            category = 'Unknown'

        cursor.execute('INSERT INTO books (name, price, category) VALUES (?, ?, ?)', (name, price, category))
        print(f'Saved: {name}, Price: {price}, Category: {category}')

        time.sleep(0.3)
    conn.commit()
    page_count += 1

    next_button = soup.find('li', class_='next')
    if next_button:
        next_page = next_button.find('a')['href']
        if next_page.startswith('catalogue/'):
            url = base_url + '/' + next_page
        else:
            url = base_url + '/catalogue/' + next_page
    else:
        url = None

conn.close()
print(f'Scrapped {page_count} pages')