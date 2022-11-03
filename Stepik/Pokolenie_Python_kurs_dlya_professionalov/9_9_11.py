from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


t = 'Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....'
e = "timyrik20@beegeek.ru"
n = "Тимур"

to_Timur = partial(send_email, t)

send_an_invitation = partial(to_Timur, n, e)


print(send_an_invitation())

try:
    to_Timur('первое', 'второе')
except:
    print('ok')

print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))
