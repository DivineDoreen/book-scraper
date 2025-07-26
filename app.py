import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Book Scraper Dashboard')

conn = sqlite3.connect('books.db')
df = pd.read_sql_query('SELECT * FROM books', conn)
conn.close()

st.subheader('Search by Book Name')
search_term = st.text_input('Enter book name (or part of it)')
if search_term:
    filtered_df = df[df['name'].str.contains(search_term, case=False, na=False)]
else:
    filtered_df = df

st.subheader('Sort by Price')
sort_order = st.radio('Select Sort Order', ['None', 'Ascending', 'Descending'])
if sort_order == 'Ascending':
    filtered_df = filtered_df.sort_values(by= 'price', ascending=True)
elif sort_order == 'Descending':
    filtered_df = filtered_df.sort_values(by= 'price', ascending=False)

st.subheader('Book Data')
st.dataframe(filtered_df)

st.subheader('Filter by Category')
categories = df['category'].unique()
selected_category = st.selectbox('Select Category', ['All'] + list(categories))

if selected_category != 'All':
    filtered_df = df[df['category'] == selected_category]
else:
    filtered_df = df
st.dataframe(filtered_df)

st.subheader('Average Price by Category')
avg_prices = df.groupby('category')['price'].mean().reset_index()
st.dataframe(avg_prices)

plt.figure(figsize=(12, 6))
sns.barplot(data=avg_prices, x='price', y='category', hue='category', palette='viridis')
plt.title('Average Book Price by Category')
plt.xlabel('Average price (£)')
plt.ylabel('Category')
plt.tight_layout()
st.pyplot(plt)

st.write('Data scrapped from books.toscrape.com')