import hashlib
import hmac
import base64
from urllib.parse import quote


def generate_signature(params, private_action, secret_key, user_key=None):
    # Create StringToSign
    if user_key:
        string_to_sign = "/".join([
            private_action, params['AppAPIKey'], params['APIKey'], params['APIVersion'],
            params['SignatureVersion'], params['SignatureMethod'], params['Timestamp'], params['ResponseFormat']
        ])
    else:
        string_to_sign = "/".join([
            params['ActionID'], params['AppAPIKey'], params['APIVersion'],
            params['SignatureVersion'], params['SignatureMethod'], params['Timestamp'], params['ResponseFormat']
        ])

    # Concatenate Keys
    composite_key = secret_key + (user_key if user_key else '')

    # Configure the HMAC Encryption Algorithm
    hmac_algorithm = hmac.new(composite_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha256)

    # Create Hash
    hmac_digest = hmac_algorithm.digest()

    # Convert Hash
    signature = base64.urlsafe_b64encode(hmac_digest).decode('utf-8')

    # Add to Common Parameters
    params['Signature'] = quote(signature, safe='')

    return params
"""
Чтобы использовать эту функцию, нужно передать словарь params с обязательными параметрами запроса 
(например, ActionID, AppAPIKey, APIKey, APIVersion, SignatureVersion, SignatureMethod, Timestamp и ResponseFormat),
 а также секретный ключ secret_key. Если это запрос на приватное действие, нужно также передать user_key.
Функция возвращает словарь с теми же параметрами, к которым добавляется параметр Signature, содержащий подпись запроса.

Например, чтобы сгенерировать подпись для запроса на UserLogin с именем пользователя testigolf@igolf.com, 
можно вызвать функцию так:
"""

params = {
    'ActionID': 'UserLogin',
    'AppAPIKey': 'uUqnXUKU86kghJk',
    'APIVersion': '1.0',
    'SignatureVersion': '2.0',
    'SignatureMethod': 'HmacSHA256',
    'Timestamp': '121224235920+0200',
    'ResponseFormat': 'JSON'
}

secret_key = 'my_app_secret_key'

user_key = 'my_user_key'

params = generate_signature(params, private_action=True, secret_key=secret_key, user_key=user_key)

print(params)
