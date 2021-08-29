string = str(input())
cipher = str(input())

message_to_cipher = str(input())
cipher_to_message = str(input())
ciphered_message = ''
unciphered_message = ''

encryption = {}

# Наполняем шифровальный словарь
for i in range(len(string)):
    encryption[string[i]] = cipher[i]

# Зашифровываем сообщение по наполненному словарю    
for i in range(len(message_to_cipher)):
    for key in encryption.keys():
        if message_to_cipher[i] == key:
            ciphered_message += encryption[key]

# Расшифровываем сообщение по наполненному словарю             
for i in range(len(cipher_to_message)):
    for key, value in encryption.items():
        if cipher_to_message[i] == value:
            unciphered_message += key

print(ciphered_message)
print(unciphered_message)