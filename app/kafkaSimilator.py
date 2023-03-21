
from kafka import KafkaConsumer, KafkaProducer
import time
import re
import datetime
# movie stream
topic = 'movielog3'
scores_map = dict()
rec_map = dict()


def show_data(time):
    total = 0
    for key, value in scores_map.items():
        if value != 0:
            total += 1

    percentage_listen_rec = total / len(scores_map)
    print("percentage_listen_rec", percentage_listen_rec)
    rec_map.clear()
    scores_map.clear()
    return percentage_listen_rec


def action_process (raw_data:str):
    # 2023-03-13T19:14:46,176474,GET /data/m/just+love+me+2006/9.mpg
    raw_data_list = raw_data.split(',')
    time = datetime.datetime.fromisoformat(raw_data_list[0])
    userId = raw_data_list[1]
    result = re.search(".*data\/m\/(.*)\/.*", raw_data)
    current_movie = result.group(1)
    if (userId not in rec_map.keys()):
        return 
    rec_movie = rec_map[userId][1]
    if (current_movie in rec_movie):
        if (userId in scores_map.keys()):
            scores_map[userId] += 1
        
# rec_map (userId, (stoptime, list of movie))
def rec_process(raw_data:str):
    raw_data_list = raw_data.split(',')
    time = datetime.datetime.fromisoformat(raw_data_list[0])
    userId = raw_data_list[1]
    result = re.search(".*result:\s(.*)", raw_data)
    movies = result.group(1).split(', ')[:-1]
    if (userId not in scores_map.keys()):
        scores_map[userId] = 0
    
    if (userId in rec_map.keys()):
        # if user ask for another recomendation with spesificy perid, ignore
        deadline = rec_map[userId][0]
        # deadline < time, deadline passed, we should use current rec 
        if (deadline < time): 
            deadline = time + datetime.timedelta(minutes=5)
            rec_map[userId] = (deadline, movies)
            scores_map.pop(userId)
        else: 
            # deadline > time, we are still processing previous userId, so we ignore it
            return
    else:
        deadline = time + datetime.timedelta(minutes=5)
        rec_map[userId] = (deadline, movies)


# kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    auto_commit_interval_ms=1000,
    max_poll_records = 100000
)

# Subscribe to the topic
consumer.subscribe([topic])

# Continuously poll for messages
while True:
    # Fetch messages in batches
    batch = consumer.poll(timeout_ms=300000)
    # Process each message in the batch
    for message in batch.values():
        for record in message:
            raw_data = record.value.decode()
            if '/data/m' in raw_data:
                action_process(raw_data)
            elif 'recommendation request' in raw_data:
                rec_process(raw_data)
    show_data(time=datetime.datetime.now())   
    print("-----")
    time.sleep(1)

