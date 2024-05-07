import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information about each book
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a.attrs['title']
        rating = book.p.attrs['class'][1]  # Assuming the rating class is 'star-rating' followed by the rating value
        price = book.select_one('div p.price_color').get_text(strip=True)

        print(f'Title: {title}, Rating: {rating}, Price: {price}')

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
