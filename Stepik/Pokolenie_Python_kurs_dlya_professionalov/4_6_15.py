import pickle


def get_control_sum(val):
    numbers = [i for i in val if type(i) == int]
    if len(numbers) == 0:
        return 0
    if type(val) == list:
        return min(numbers) * max(numbers)
    if type(val) == dict:
        return sum(numbers)


with open(input(), 'rb') as file:
    obj = pickle.load(file)
    number = int(input())
    if get_control_sum(obj) == number:
        print("Контрольные суммы совпадают")
    else:
        print("Контрольные суммы не совпадают")
