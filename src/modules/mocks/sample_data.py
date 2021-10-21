class ItemValue:
  value = {}
  def __init__(self, value):
    self.value = value

sample_data = {
  'items': [
    ItemValue(
      {'message': 'hello world', 'date': '2021-10-21T13:26:33.434914'}
    )
  ]
}
