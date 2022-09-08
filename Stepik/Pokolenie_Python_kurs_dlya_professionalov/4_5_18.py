from zipfile import ZipFile
from datetime import datetime


if __name__ == '__main__':
    with ZipFile('workbook.zip') as zip_file:
        files = [file for file in zip_file.infolist() if not file.is_dir()]
    files.sort(key=lambda x: x.filename.split('/')[-1].lower())
    for file in files:
        print(file.filename.split('/')[-1])
        print(f'  Дата модификации файла: {datetime(*file.date_time)}')
        print(f'  Объем исходного файла: {file.file_size} байт(а)')
        print(f'  Объем сжатого файла: {file.compress_size} байт(а)')
        print()
