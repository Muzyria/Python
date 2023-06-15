from contextlib import contextmanager
import os

@contextmanager
def safe_write(filename):
    try:
        temp_file = open('temp_file', 'w+')
        yield temp_file
        temp_file.seek(0)
    except Exception as err:
        print(f'Во время записи в файл было возбуждено исключение {type(err).__name__}')
    else:
        file = open(filename, 'w')
        file.writelines(temp_file.readlines())
        file.close()
    finally:
        temp_file.close()
        os.remove('temp_file')
