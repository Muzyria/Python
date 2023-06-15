import contextlib, io, pathlib


@contextlib.contextmanager
def safe_write(filename):
    buffer = io.StringIO()
    mode = 'r+' if pathlib.Path(filename).is_file() else 'w'
    try:
        file = open(filename, mode)
        yield buffer
        file.write(buffer.getvalue())
        buffer.close()
        file.close()      
    except Exception as error:
        print(
            f'Во время записи в файл было возбуждено исключение'
            f' {error.__class__.__name__}'
        )
