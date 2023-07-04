import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

# Создание потоков
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

print("Завершено")
