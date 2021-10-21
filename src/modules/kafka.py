import json

from .utils import get_current_timestamp

class Kafka(object):
  def read_topic(self, consumer, limit, timeout_ms) -> list:
    result = []
    response = consumer.poll(max_records=limit, timeout_ms=timeout_ms)
    for key, msgs in response.items():
      for m in msgs:
        result.append(m.value)
    consumer.close()

    return result
