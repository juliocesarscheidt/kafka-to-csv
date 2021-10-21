import os
import json

from kafka import KafkaConsumer

from modules.file import FileHandler
from modules.kafka import Kafka
from modules.utils import discovery_columns_from_data

LIMIT=int(os.environ.get('TIMEOUT', '100'))
TIMEOUT_MS=int(os.environ.get('TIMEOUT_MS', '10000'))
CSV_SEPARATOR=os.environ.get('CSV_SEPARATOR', ',')

def execute():
  conf = {
    'bootstrap_servers': os.environ.get('BOOTSTRAP_SERVERS', 'localhost:9092').split(','),
    'topic_name': os.environ.get('TOPIC_NAME'),
    'sasl_plain_username': os.environ.get('PLAIN_USERNAME'),
    'sasl_plain_password': os.environ.get('PLAIN_PASSWORD'),
  }
  consumer = KafkaConsumer(
    conf['topic_name'],
    bootstrap_servers=conf['bootstrap_servers'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='kafka-group',
    value_deserializer=lambda x: json.loads(x),
    security_protocol='PLAINTEXT',
    sasl_mechanism='PLAIN',
    sasl_plain_username=conf['sasl_plain_username'],
    sasl_plain_password=conf['sasl_plain_password'],
  )
  kafka = Kafka()
  data = kafka.read_topic(consumer, LIMIT, TIMEOUT_MS)
  columns = discovery_columns_from_data(data)
  file_path = './output.csv'
  fileHandler = FileHandler(os, open)
  fileHandler.remove_file(file_path)
  fileHandler.save_file(file_path, columns, data, CSV_SEPARATOR)

if __name__ in '__main__':
  execute()
