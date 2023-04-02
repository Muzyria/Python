def find_lines_len_more_6(file_name: str) -> int:
    with open(file_name, 'r', encoding='utf-8') as file:
        return len([line for line in file if len(line.strip()) > 6])
