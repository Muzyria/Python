import hashlib
import hmac
import base64
from urllib.parse import quote

def calculate_signature(to_sign_str, sign_method, secret_key):
    mac = hmac.new(secret_key.encode('utf-8'), msg=to_sign_str.encode('utf-8'), digestmod=hashlib.sha256)
    raw_sig = mac.digest()
    signature = base64.urlsafe_b64encode(raw_sig).decode('utf-8').rstrip('=')
    return signature

def to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format):
    params = [
        action_code,
        app_api_key,
        api_version,
        sig_version,
        sig_method,
        timestamp_str,
        response_format
    ]
    to_sign_str = '/'.join([quote(param, safe='') for param in params])
    return to_sign_str

# Пример использования
action_code = 'UserLogin'
app_api_key = 'uUqnXUKU86kghJk'
api_version = '1.0'
sig_version = '2.0'
sig_method = 'HmacSHA256'
timestamp_str = '121224235920+0200'
response_format = 'JSON'
secret_key = 'YourSecretKey'

to_sign_str = to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format)
signature = calculate_signature(to_sign_str, sig_method, secret_key)
print(signature)
