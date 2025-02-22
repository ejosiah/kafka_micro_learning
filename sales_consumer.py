import config
import json
import confluent_kafka as ck
import time
from threading import Thread

class Consumer(Thread):
    def __init__(self, tracker):
        Thread.__init__(self)
        self.consumer = ck.Consumer(config.consumer_config)
        self.tracker = tracker

    def run(self):
        self.consumer.subscribe(['ACM-SALES'])

        while(self.tracker.running):
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                print(f'Consumer error: {msg.error()}')
                continue

            sales = json.loads(msg.value().decode('utf-8'))
            self.tracker.update(sales['Profit'])
            time.sleep(2)
        
        self.consumer.close()
        print("consumer succesfully shutdown")