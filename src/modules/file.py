class FileHandler:
  def __init__(self, __os, __open_fn):
    self.__os = __os
    self.__open_fn = __open_fn

  def save_file(self, file_path, columns, data, csv_separator) -> None:
    with self.__open_fn(file_path, 'w') as f:
      f.write('{}\n'.format(csv_separator.join(columns)))
      for row in data:
        columns_string = []
        for column in columns:
          columns_string.append(str(row[column]).strip())
        f.write('{}\n'.format(csv_separator.join(columns_string)))
      f.close()

  def remove_file(self, file_path) -> None:
    try:
      self.__os.remove(file_path)
    except Exception as e:
      pass
