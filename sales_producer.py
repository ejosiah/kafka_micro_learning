import config
import csv
import json
from confluent_kafka import Producer

p = Producer(config.producer_config)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

with open('sample_superstore.csv', encoding = "ISO-8859-1") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        p.poll(0)
        key = row['Customer ID']
        value = json.dumps(row)
        p.produce('ACM-SALES', value, key, callback=delivery_report)

p.flush()