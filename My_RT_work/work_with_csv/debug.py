
import time
from threading import Thread


def first_fun():
    print('First GO')
    time.sleep(3)
    print('First have DONE')


def second_fun():
    print('Second GO')
    time.sleep(3)
    print('Second have DONE')


# first_fun()
# second_fun()

th1 = Thread(target=first_fun)
th1.start()
th2 = Thread(target=second_fun)
th2.start()
