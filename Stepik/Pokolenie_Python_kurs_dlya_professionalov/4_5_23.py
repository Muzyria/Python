from zipfile import ZipFile


def get_size(size: int) -> str:
    if 0 <= size < 1024:
        return f'{size} B'
    elif 1024 <= size < 1024 * 1024:
        return f'{round(size / 1024)} KB'
    elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
        return f'{round(size / (1024 * 1024))} MB'
    else:
        return f'{round(size / (1024 * 1024 * 1024))} GB'


if __name__ == '__main__':
    my_files = []
    with ZipFile('desktop.zip') as zip_file:
        files = zip_file.infolist()
        for file in files:
            size = file.file_size
            path_file = [elm for elm in file.filename.split('/') if elm != '']
            if size > 0:
                path_file[-1] += f' {get_size(size)}'
            for i, elm in enumerate(path_file):
                if '  ' * i + elm not in my_files:
                    my_files.append('  ' * i + elm)
    print(*my_files, sep='\n')
