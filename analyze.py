import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('books.db')
df = pd.read_sql_query('SELECT * FROM books', conn)
conn.close()

avg_prices = df.groupby('category')['price'].mean().reset_index()

print('Average price by category')
print(avg_prices)

plt.figure(figsize=(12,6))
sns.barplot(data=avg_prices, x='price', y='category', hue='category', palette='viridis')
plt.title('Average Book Price by Category')
plt.xlabel('Average Price (£)')
plt.ylabel('Category')
plt.tight_layout()

plt.savefig('avg_price_by_category.png')
plt.show()