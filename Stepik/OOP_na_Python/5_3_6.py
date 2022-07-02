
def func(phrase):
    func(phrase)
    
try:
    func('Это рекурсия, детка!')    
except RecursionError:
    print("Кто-то должен остановить это безумие")

