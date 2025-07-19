import requests
import pyodbc
from datetime import datetime
import logging

# logging setup
logging.basicConfig(
    filename='etl_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# API params
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    logging.error(f"API request failed: {e}")
    exit(1)

# db connection
server = 'localhost\\SQLEXPRESS'
database = 'CoinGeckoData'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
except pyodbc.Error as db_err:
    logging.error(f"Database connection failed: {db_err}")
    exit(1)

# insert data
try:
    for coin in data:
        symbol = coin['symbol']
        name = coin['name']
        date = datetime.today().date()
        price = coin.get('current_price', 0)
        market_cap = coin.get('market_cap', 0)
        volume = coin.get('total_volume', 0)

        cursor.execute("""
            INSERT INTO DailyPrices (symbol, name, date, price_usd, market_cap_usd, total_volume_usd)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (symbol, name, date, price, market_cap, volume))

    conn.commit()
    print("ETL complete. Data inserted.")
except Exception as e:
    logging.error(f"Data insert failed: {e}")
finally:
    cursor.close()
    conn.close()
