# CoinGecko ETL Pipeline

This project is an end-to-end automated data pipeline that extracts cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api), transforms it using Python, and loads it into a SQL Server database. The pipeline is designed to support business intelligence reporting with tools like Power BI.

## Features
- Pulls real-time market data for top cryptocurrencies
- Transforms JSON API responses to a structured tabular format
- Loads data into a local SQL Server table (`DailyPrices`)
- Easily extendable for scheduling, historical analysis, or Power BI dashboards

## Automation & Logging

- The ETL script includes error-handling for API requests and SQL Server connection issues.
- Errors are logged to a local file (`etl_errors.log`) for debugging and auditing.
- The script is designed to be scheduled using Windows Task Scheduler for automated daily data pulls.

## Tech Stack
- Python
- SQL Server
- CoinGecko API
- `pyodbc` SQL driver
- Power BI (for visualization – coming soon)

## How to Run

### 1. Set up the SQL Server database and table
Open SQL Server Management Studio (SSMS) and run the following:

```sql
CREATE DATABASE CoinGeckoData;
GO

USE CoinGeckoData;
GO

CREATE TABLE DailyPrices (
    id INT IDENTITY(1,1) PRIMARY KEY,
    symbol NVARCHAR(10),
    name NVARCHAR(50),
    date DATE,
    price_usd FLOAT,
    market_cap_usd FLOAT,
    total_volume_usd FLOAT
);
```

### 2. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/coingecko-etl-pipeline.git
cd coingecko-etl-pipeline
```

### 3. Install Python dependencies

Make sure you have Python installed, then run:

```bash
pip install requests pyodbc
```

### 4. Run the ETL script

From the project folder, run:

```bash
python etl_coingecko_to_sql.py
```

This will pull the top 5 cryptocurrencies from the CoinGecko API and insert the data into the DailyPrices table in SQL Server.

### 5. Prerequisites

- SQL Server installed and running
- ODBC Driver 17 for SQL Server
- Python 3.8 or newer
- `requests` and `pyodbc` Python libraries installed
- `CoinGeckoData` database and `DailyPrices` table created
