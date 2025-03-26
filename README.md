# DataStreaming
Simple market data streaming service using **yfinance** to get the data, then **kafka** to stream it.

## Instructions
If you don't have Kafka installed, follow this link: https://kafka.apache.org/downloads

After successfully running Kafka, install the required packages:
```
pip install yfinance kafka-python
```
Then run the ``main.py`` file in one terminal, then ``consumer.py`` in another terminal to see the results!
