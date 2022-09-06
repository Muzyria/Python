from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    result = [file for file in zip_file.infolist() if file.file_size > 0]
    print(len(result))


# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as z_file:
#     print(sum(map(lambda x: not x.is_dir(), z_file.infolist())))