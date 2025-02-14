# Laptop Scraper

## Overview
This project is a web scraper that extracts laptop data (titles and prices) from a test e-commerce website. The extracted data is stored in a PostgreSQL database for further analysis.

## Features
- ✅ **Scrapes** laptop listings from a sample e-commerce website.
- ✅ **Uses** proxies to avoid detection.
- ✅ **Stores** data in a PostgreSQL database.
- ✅ **Cleans** and processes price data.
- ✅ **Implements** error handling for database and web scraping operations.

## Technologies Used
- 🐍 **Python**
- 🗄 **PostgreSQL**
- 🌐 **BeautifulSoup** (for web scraping)
- 🔗 **Requests** (for HTTP requests)
- 🗃 **psycopg2** (for database interactions)

## Prerequisites
Ensure you have the following installed:

- **Python 3.x**
- **PostgreSQL**
- Required Python libraries:
  ```bash
  pip install psycopg2 requests beautifulsoup4
  ```
- A PostgreSQL database with the following credentials:
  - **DB_NAME:** postgres
  - **DB_USER:** postgres
  - **DB_PASSWORD:** (leave empty or set your password)
  - **DB_HOST:** localhost
  - **DB_PORT:** 5432

## Setup Instructions
1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Configure your PostgreSQL database.**
3. **Ensure proxy settings are configured in `proxy.py`.**
4. **Run the scraper:**
   ```bash
   python scraper.py
   ```

## Code Structure
- 📜 `scraper.py` - Main script that scrapes and stores data.
- 🌐 `proxy.py` - Contains proxy configurations.

## How It Works
1. **Establishes** a connection to the PostgreSQL database.
2. **Creates** a table (`laptops`) if it does not exist.
3. **Iterates** through multiple pages of the website, scraping laptop data.
4. **Cleans** the scraped price values and stores them in the database.
5. **Handles** errors and logs the process.

## Notes
- ⚠ **Ensure** the PostgreSQL database is running before executing the script.
- ⚠ **Modify** `proxy.py` to include valid proxy configurations.
- ⚠ **The script** uses `random.choice()` to select a proxy for each request.

## Author
**Your Name**

## License
This project is licensed under the **MIT License**.

