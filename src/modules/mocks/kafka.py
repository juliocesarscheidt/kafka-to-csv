class KafkaConsumerMock(object):
  def __init__(self, topic_name, bootstrap_servers, auto_offset_reset, enable_auto_commit, group_id, value_deserializer, security_protocol=None, sasl_mechanism=None, sasl_plain_username=None, sasl_plain_password=None):
    self.topic_name = topic_name
    self.bootstrap_servers = bootstrap_servers
    self.auto_offset_reset = auto_offset_reset
    self.enable_auto_commit = enable_auto_commit
    self.group_id = group_id
    self.value_deserializer = value_deserializer
    self.security_protocol = security_protocol
    self.sasl_mechanism = sasl_mechanism
    self.sasl_plain_username = sasl_plain_username
    self.sasl_plain_password = sasl_plain_password
  def poll(self, max_records, timeout_ms) -> dict:
    return {}
  def close(self):
    pass
