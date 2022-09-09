from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            [zip_file.extract(i) for i in args]
        else:
            zip_file.extractall()
