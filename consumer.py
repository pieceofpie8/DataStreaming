from kafka import KafkaConsumer
import json

def main():
    consumer = KafkaConsumer(
        'yahoo_finance_data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    for message in consumer:
        print(f"Received message: {message.value}")

if __name__ == '__main__':
    main()
