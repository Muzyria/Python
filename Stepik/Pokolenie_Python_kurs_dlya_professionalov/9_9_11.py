from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


# to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')

def to_Timur(text, *args, **kwargs):
    return send_email('Тимур', 'timyrik20@beegeek.ru', text)


send_an_invitation = partial(to_Timur, 'Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')



print(send_an_invitation())

try:
    to_Timur('первое', 'второе')
except:
    print('ok')

print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))
