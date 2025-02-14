import requests
from bs4 import BeautifulSoup
from proxy_testing import proxy1, proxy2, proxy3, proxy4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

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

proxy_list = [proxy1.get_proxy_string(), proxy2.get_proxy_string(), proxy3.get_proxy_string(), proxy4.get_proxy_string()]

# Перевірка проксі
def test_proxy(proxy_url):
    proxy_dict = {
        'http': proxy_url,
        'https': proxy_url
    }
    try:
        test_response = requests.get("https://httpbin.org/ip", proxies=proxy_dict, timeout=10)
        print(f"Проксі працює: {test_response.text}")
        return True
    except:
        print(f"Проксі не працює: {proxy_url}")
        return False

def try_requests():
    proxy = {
        'http': proxy_list[0],
        'https': proxy_list[0]
    }
    
    time.sleep(2)
    
    try:
        response = requests.get(
            url, 
            headers=headers, 
            proxies=proxy,
            timeout=10,
            allow_redirects=True
        )
        print(f"Status Code: {response.status_code}")
        return response.text if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"Помилка requests: {e}")
        return None

def try_selenium():
    try:
        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy_list[0]}')
        chrome_options.add_argument('--headless')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        return page_source
    except Exception as e:
        print(f"Помилка selenium: {e}")
        return None

if test_proxy(proxy_list[0]):
    content = try_requests()
    
    if not content or "403" in content:
        print("Пробуємо Selenium...")
        content = try_selenium()
    
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        print("Успішно отримано контент!")
        
        with open('carid_wheels.html', 'w', encoding='utf-8') as file:
            file.write(content)
        print("HTML-контент збережено в carid_wheels.html")
        
        with open('carid_wheels.txt', 'w', encoding='utf-8') as file:
            file.write(soup.get_text())
        print("Текстовий контент збережено в carid_wheels.txt")
        
        print("Перші 500 символів контенту:")
        print(content[:500])
    else:
        print("Не вдалося отримати контент")
else:
    print("Проксі не працює, спробуйте інший")