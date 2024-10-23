def log_for(logfile: str, date_str: str):
    with (
        open(logfile, "r", encoding="utf=8") as read_file,
        open(f"log_for_{date_str}.txt", "w", encoding="utf=8") as write_file
    ):
        for line in read_file.readlines():
            if line[:10] == date_str:
                write_file.write(line[10:].lstrip())


with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())
