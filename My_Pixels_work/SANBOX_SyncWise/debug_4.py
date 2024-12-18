import subprocess
import time
import pandas as pd
from datetime import datetime


def execute_adb_command():
    """Выполняет команду adb shell ps и возвращает вывод."""
    result = subprocess.run(["adb", "shell", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Ошибка выполнения команды: {result.stderr}")
        return None


def parse_ps_output(output):
    """Парсит вывод команды adb shell ps в формат списка словарей."""
    lines = output.splitlines()
    headers = lines[0].split()  # Первая строка - заголовки
    data = []
    for line in lines[1:]:
        if line.strip():
            values = line.split(maxsplit=len(headers) - 1)  # Делим на количество колонок
            data.append(dict(zip(headers, values)))
    return data


def save_to_csv(data, filename="process_log.csv"):
    """Сохраняет данные в CSV файл."""
    df = pd.DataFrame(data)
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Добавляем метку времени
    if not df.empty:
        # Добавляем данные в файл, создавая его, если он не существует
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))


def main():
    """Основной цикл для записи данных каждые 30 секунд."""
    filename = "process_log.csv"
    print(f"Начинаю запись данных в файл: {filename}")

    try:
        while True:
            output = execute_adb_command()
            if output:
                data = parse_ps_output(output)
                save_to_csv(data, filename)
            print("Данные сохранены. Ожидание 30 секунд...")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nСбор данных завершен.")


if __name__ == "__main__":
    main()
