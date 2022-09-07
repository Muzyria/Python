from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result = min([i for i in info if not i.is_dir()], key=lambda x: x.compress_size / x.file_size * 100)
    print(result.filename.split('/')[-1])
