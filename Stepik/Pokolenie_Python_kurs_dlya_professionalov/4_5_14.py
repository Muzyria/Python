from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    result = [file for file in zip_file.infolist() if file.file_size > 0]
    print(len(result))
