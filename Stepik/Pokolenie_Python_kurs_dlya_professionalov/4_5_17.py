from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result = [file.filename.split('/')[-1] for file in info if not file.is_dir()
              and datetime(*file.date_time) > datetime(2021, 11, 30, 14, 22, 00)]

    [print(i) for i in sorted(result)]
