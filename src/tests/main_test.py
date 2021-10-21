import json
import pytest
import mock
import logging

from modules.file import FileHandler
from modules.utils import discovery_columns_from_data
from modules.kafka import Kafka
from modules.mocks.sample_data import sample_data
from modules.mocks.file import OsMock, open_fn_mock
from modules.mocks.kafka import KafkaConsumerMock

def test_main(mocker):
  logger = logging.getLogger()
  conf = {
    'bootstrap_servers': ['localhost:9092'],
    'topic_name': 'sample',
  }
  consumerMock = KafkaConsumerMock(
    conf['topic_name'],
    bootstrap_servers=conf['bootstrap_servers'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='kafka-group',
    value_deserializer=lambda x: json.loads(x),
  )
  mocker.patch.object(consumerMock, 'poll', return_value=sample_data)

  osMock = OsMock()
  kafka = Kafka()
  data = kafka.read_topic(consumerMock, 10, 50)
  logger.debug(data)
  columns = discovery_columns_from_data(data)
  logger.debug(columns)
  columns_check = list([list(c.keys())[0] for c in data])
  logger.debug(columns_check)

  assert len(data) == 1
  assert len(columns) == 1
  assert columns == columns_check

  file_path = './output.csv'
  fileHandler = FileHandler(osMock, open_fn_mock)
  assert fileHandler.remove_file(file_path) is None
  assert fileHandler.save_file(file_path, columns, data, ',') is None
