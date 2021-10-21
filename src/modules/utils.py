from datetime import datetime, timedelta

def get_current_timestamp() -> str:
  return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def discovery_columns_from_data(data) -> list:
  columns = []
  for column_keys in [i.keys() for i in data]:
    for column in list(column_keys):
      if column in columns: continue
      columns.append(str(column).strip())

  return columns
