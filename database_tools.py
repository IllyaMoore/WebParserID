import psycopg2
import datetime
import requests
from bs4 import BeautifulSoup
import random
from proxy import proxy1, proxy2, proxy3, proxy4

proxy_list = [proxy1.get_proxy_string(), proxy2.get_proxy_string(), proxy3.get_proxy_string(), proxy4.get_proxy_string()]

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "illya11335577"
DB_HOST = "localhost"
DB_PORT = "5432"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

def random_proxy():
    return random.choice(proxy_list)

proxies = {"http": random_proxy(), "https": random_proxy()}

def create_table(conn):
    """Create the laptops table if it doesn't exist"""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS laptops (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                scrape_date TIMESTAMP NOT NULL
            )
        """)
    conn.commit()

def clean_price(price_str):
    """Convert price string to decimal"""
    return float(price_str.replace('$', '').replace(',', ''))

def insert_laptop(conn, title, price):
    """Insert a laptop record into the database"""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO laptops (title, price, scrape_date)
            VALUES (%s, %s, %s)
        """, (title, price, datetime.datetime.now()))
    conn.commit()

def main():
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Successfully connected to the database")
        
        create_table(conn)
        
        # Scraping logic
        url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page='
        n = 1
        
        while n != 10:
            n += 1
            response = requests.get(url + str(n), headers=headers, proxies=proxies)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                prices = soup.find_all(class_='price float-end card-title pull-right')
                titles = soup.find_all(class_='title')
                
                for title, price in zip(titles, prices):
                    title_text = title.get_text(strip=True)
                    price_value = clean_price(price.get_text(strip=True))
                    
                    try:
                        insert_laptop(conn, title_text, price_value)
                        print(f"Inserted - Title: {title_text}, Price: ${price_value}")
                    except Exception as e:
                        print(f"Error inserting record: {e}")
                
            else:
                print(f"Failed to retrieve page {n}")
                
    except Exception as e:
        print(f"Database connection error: {e}")
    
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed")

if __name__ == "__main__":
    main()