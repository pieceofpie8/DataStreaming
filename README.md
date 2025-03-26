# DataStreaming
Simple market data streaming service using **yfinance** to get custom ticker data, then **kafka** to stream it.

## Instructions
If you don't have Kafka installed, follow this link: https://kafka.apache.org/downloads

After successfully running Kafka, install the required packages:
```
pip install yfinance kafka-python
```
Then run the ``main.py`` file in one terminal, using this command (e.g. for AAPL):
```
python3 main.py --ticker=AAPL
```
Then run ``consumer.py`` in another terminal:
```
python3 consumer.py
```
And here you go!

~Jason
