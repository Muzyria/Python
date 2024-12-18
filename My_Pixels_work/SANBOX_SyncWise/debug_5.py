import subprocess
import time
from datetime import datetime


def execute_adb_command():
    """Выполняет команду adb shell ps и возвращает вывод."""
    result = subprocess.run(["adb", "shell", "ps"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Ошибка выполнения команды: {result.stderr}")
        return None


def save_output_to_file(output, filename="process_log.txt"):
    """Сохраняет вывод команды в файл с временной меткой."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"=== {timestamp} ===\n")
        file.write(output)
        file.write("\n")


def main():
    """Основной цикл для записи данных каждые 30 секунд."""
    filename = "process_log.txt"
    print(f"Начинаю запись данных в файл: {filename}")

    try:
        while True:
            output = execute_adb_command()
            if output:
                save_output_to_file(output, filename)
            print("Данные сохранены. Ожидание 10 секунд...")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nСбор данных завершен.")


if __name__ == "__main__":
    main()
