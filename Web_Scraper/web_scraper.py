import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    
    # Find the price element within the current book article
    price_element = book.select_one(".price_color")
    
    # Check if the price element is found
    if price_element:
        price = price_element.get_text()
        print(f"Title of Book: {title}, has rating: {rating} star, Price: {price}")
    else:
        print(f"Title of Book: {title}, has rating: {rating} star, Price not found")
