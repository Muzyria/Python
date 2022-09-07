from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result_compress_size = sum([value.compress_size for value in info if not value.is_dir()])
    result_file_size = sum([value.file_size for value in info if not value.is_dir()])
    print(f'Объем исходных файлов: {result_file_size} байт(а)')
    print(f'Объем сжатых файлов: {result_compress_size} байт(а)')
