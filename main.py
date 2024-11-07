## Модуль для импорта данных из ris-файла

def get_ris_data(path: str, col_name: str) -> any:
  """
  Выгрузка колонки из ris-файла в ...

  :path: путь к файлу
  :col_name: название колонки
  """
  # прочитать файл с помощью функции open()
  file = open(path, "r")
  # создадим пустой список для хранения аннотаций
  abs = []
  # переберем строки в цикле for 
  for line in file.readlines():
    # разобьем строку по общему символу, предварительно убрав символ переноса строки "\n" 
    splitted_line = line.strip("\n").split("  - ")
    # находим строки с AB и добавляем аннотации в список abs
    if col_name == splitted_line[0]:
      abs.append(splitted_line[1])
  # закрываем чтение файла
  file.close()
  return abs
