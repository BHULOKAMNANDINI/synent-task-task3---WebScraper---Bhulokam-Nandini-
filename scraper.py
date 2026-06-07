import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Store data
book_list = []

for book in books:
    title = book.h3.a["title"]

    price = book.find(
        "p",
        class_="price_color"
    ).text

    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    book_list.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# Display data in terminal
for item in book_list:
    print(item)

# Save to CSV
df = pd.DataFrame(book_list)
df.to_csv("data.csv", index=False)

# Save to JSON
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(book_list, file, indent=4)

print("\nData Scraped Successfully!")
print("CSV File Created: data.csv")
print("JSON File Created: data.json")