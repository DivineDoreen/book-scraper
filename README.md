# Book Scraper Dashboard

A web application that scrapes book data (names, prices, categories) from [books.toscrape.com](http://books.toscrape.com), stores it in a SQLite database, analyzes it with Pandas, and visualizes it with Seaborn. The app, built with Streamlit, offers interactive features like category filtering, price sorting, and book name search, deployed on Render.

## Features
- Scrapes ~1000 books with names, prices, and categories.
- Filters books by category.
- Sorts books by price (ascending/descending).
- Searches books by name.
- Displays average price by category with a bar chart.
- Deployed at (https://book-scraper-g9mt.onrender.com)

## Technologies Used
- Python 3.10
- Requests, BeautifulSoup4 (scraping)
- SQLite3 (database)
- Pandas, Seaborn, Matplotlib (analysis/visualization)
- Streamlit (web app)
- Render (deployment)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/DivineDoreen/book-scraper.git
   cd book-scraper
