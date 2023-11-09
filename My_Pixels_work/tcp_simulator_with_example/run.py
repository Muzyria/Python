import os
import csv
import time
from threading import Thread

PATH = fr"C:\Program Files\Java\jre-1.8\bin\java.exe"

# os.system(fr'cd C:\Git_Muzyria\Python\Python\My_Pixels_work\tcp_simulator_with_example')

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Execution time for {func.__name__}: {elapsed_time:.2f} seconds")
        return result
    return wrapper


os.system(fr'java -jar syncwise-tcp-simulator-0.6.jar --help')


# os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -sc utilitygauge_2.csv -env dev --request-type utilitygauge --device S10150000211018049 -i 1')

@execution_time_decorator
def run():
    os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -sc utilitygauge_2.csv -env dev --request-type utilitygauge --device L10116001811250A52 -i 1')


run()


# def first_fun():
#     print('First GO')
#     os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 50 -i 0')
#     print('First has DONE')
#
#
# def second_fun():
#     print('Second GO')
#     os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 15')
#     print('Second has DONE')
#
#
# def third_fun():
#     print('Third GO')
#     os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 15 -i 0')
#     print('Third has DONE')
#
#
# def fourth_fun():
#     print('Fourth GO')
#     os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.7-same-recordedDate.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 15 -i 0')
#     print('Fourth has DONE')


# th1 = Thread(target=first_fun)
# th1.start()
# th2 = Thread(target=second_fun)
# th2.start()
# th3 = Thread(target=third_fun)
# th3.start()
# th4 = Thread(target=fourth_fun)
# th4.start()
