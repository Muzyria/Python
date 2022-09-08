from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
