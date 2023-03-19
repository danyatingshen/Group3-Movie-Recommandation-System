from os import path
import sys, os
from datetime import datetime
from json import dumps, loads
from time import sleep
from random import randint
import numpy as np
# ssh -o ServerAliveInterval=60 -L 9092:localhost:9092 tunnel@128.2.24.106 -NTf
from kafka import KafkaConsumer, KafkaProducer

# Update this for your demo otherwise you'll see my data :)
topic = 'movielog3'

# Create a consumer to read data from kafka
# Ref: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    # Read from the start of the topic; Default is latest
    auto_offset_reset='earliest',
    # auto_offset_reset='latest',
    # group_id='team13',
    # Commit that an offset has been read
    enable_auto_commit=True,
    # How often to tell Kafka, an offset has been read
    auto_commit_interval_ms=1000
)

print('Reading Kafka Broker')
for message in consumer:

    message = message.value.decode()
    # Default message.value type is bytes!
    print(loads(message))
    os.system(f"echo {message} >> kafka_log.csv")