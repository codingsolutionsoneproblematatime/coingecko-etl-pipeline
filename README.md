# CoinGecko ETL Pipeline

This project is an end-to-end automated data pipeline that extracts cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/en/api), transforms it using Python, and loads it into a SQL Server database. The pipeline is designed to support business intelligence reporting with tools like Power BI.

## Features
- Pulls real-time market data for top cryptocurrencies
- Transforms JSON API responses to a structured tabular format
- Loads data into a local SQL Server table (`DailyPrices`)
- Easily extendable for scheduling, historical analysis, or Power BI dashboards

## Tech Stack
- Python
- SQL Server
- CoinGecko API
- `pyodbc` SQL driver
- Power BI (for visualization – coming soon)

## How to Run

Clone the repo and navigate into it:

```bash
git clone https://github.com/codingsolutionsoneproblematatime/coingecko-etl-pipeline.git
cd coingecko-etl-pipeline
