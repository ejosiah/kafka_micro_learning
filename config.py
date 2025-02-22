import random

groupid = 0

with open('consumer_group_index.txt', 'r') as file:
    groupid = int(file.readline())

with open('consumer_group_index.txt', 'w') as file:
    file.write(f'{groupid+1}')   

producer_config = {
    'bootstrap.servers': 'kafka-broker-1:9092,kafka-broker-2:9094,kafka-broker-1:9096'
}

consumer_config = {
    'bootstrap.servers': 'kafka-broker-1:9092,kafka-broker-2:9094,kafka-broker-1:9096',
    'group.id': f'test-consumer-group-{groupid}',
    'auto.offset.reset': 'earliest'
}