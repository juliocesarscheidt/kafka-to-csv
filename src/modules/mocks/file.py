class OsMock:
  def remove(self, file_path):
    pass

class FileMock(object):
  def __init__(self, file_path, mode):
    self.file_path = file_path
    self.mode = mode
  def __enter__(self):
    return self
  def __exit__(self, type, value, traceback):
    return False
  def write(self, data):
    print('Writing data {}'.format(data))
    pass
  def close(self):
    pass

def open_fn_mock(file_path, mode):
  return FileMock(file_path, mode)
