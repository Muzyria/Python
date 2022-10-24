from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


name1 = 'Тимур'
email1 = 'timyrik20@beegeek.ru'
text1 = 'Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....'



def to_Timur(name1, email1):
    partial(send_email,name1, email1)


def send_an_invitation(text=text1):
    partial(to_Timur,text)



print(send_an_invitation())

try:
    to_Timur('первое', 'второе')
except:
    print('ok')

try:
    to_Timur('первое', 'второе', 'третье')
except:
    print('ok')

print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))
