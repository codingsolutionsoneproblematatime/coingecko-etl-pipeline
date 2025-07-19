import requests
import pyodbc
from datetime import datetime

# extract from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(url, params=params)
data = response.json()

# connect to SQL Server
server = 'localhost\\SQLEXPRESS'
database = 'CoinGeckoData'
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# transform it and load it and load it
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
cursor.close()
conn.close()

print("ETL complete, data inserted.")
