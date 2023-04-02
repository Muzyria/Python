def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, 'r', encoding='utf-8') as file:
        for _ in range(n):
            print(file.readline().strip())
