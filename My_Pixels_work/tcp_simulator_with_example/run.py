import os
from threading import Thread

PATH = fr"C:\Program Files\Java\jre-1.8\bin\java.exe"

# os.system(fr'cd C:\Git_Muzyria\Python\Python\My_Pixels_work\tcp_simulator_with_example')


os.system(fr'java -jar syncwise-tcp-simulator-0.6.jar --help')



# os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.6.jar -env dev --request-type utilitygauge --device S10150000211018049 --limit 10 -i 0')


def first_fun():
    print('First GO')
    os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.6.jar -env live --request-type utilitygauge --device S10150000211018049 --limit 10 -i 0')
    print('First has DONE')


def second_fun():
    print('Second GO')
    os.system(fr'"{PATH}" -jar syncwise-tcp-simulator-0.6.jar -env live --request-type utilitygauge --device L10116001811250A52 --limit 10 -i 0')
    print('Second has DONE')


th1 = Thread(target=first_fun)
th1.start()
th2 = Thread(target=second_fun)
th2.start()
