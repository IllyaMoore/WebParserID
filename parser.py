import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
    "Accept-Language": "en-US,en;q=0.9"
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = soup.find_all("div", class_="product-item")

    for product in products:
        title_tag = product.find("a", class_="product-title")
        title = title_tag.text.strip() if title_tag else "Без назви"

        price_tag = product.find("span", class_="price")
        price = price_tag.text.strip() if price_tag else "Ціна не вказана"

        print(f"Назва: {title}\nЦіна: {price}\n{'-'*40}")
else:
    print(f"Помилка: {response.status_code}")