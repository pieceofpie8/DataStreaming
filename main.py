import yfinance as yf
from kafka import KafkaProducer
import json
import time
import argparse

def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data.to_json()

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

topic = 'yahoo_finance_data'
parser = argparse.ArgumentParser(description="Fetch and process stock data.")
parser.add_argument("--ticker", type=str, required=True, help="Ticker symbol to fetch data for (e.g., AAPL)")
args = parser.parse_args()
ticker = args.ticker

while True:
    try:
        data = fetch_data(ticker)
        producer.send(topic, data)
        print(f"Sent data for {ticker}: {data}")
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")
