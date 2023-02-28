import hashlib
import hmac
import base64
import time

def calculate_signature(to_sign_str, sign_method, secret_key):
    key_bytes = bytes(secret_key, 'utf-8')
    message_bytes = bytes(to_sign_str, 'utf-8')
    if sign_method == 'HmacSHA256':
        digestmod = hashlib.sha256
    else:
        raise ValueError('Unsupported signature method')
    signature = hmac.new(key_bytes, message_bytes, digestmod=digestmod).digest()
    return base64.urlsafe_b64encode(signature).decode('utf-8')

def to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format):
    params = [action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format]
    return '/'.join(params)

# Example usage
action_code = 'UserLogin'
app_api_key = 'uUqnXUKU86kghJk'
api_version = '1.0'
sig_version = '2.0'
sig_method = 'HmacSHA256'
response_format = 'JSON'
secret_key = 'YourApplicationSecretKey'
timestamp_str = time.strftime('%y%m%d%H%M%S%z')
to_sign_str = to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format)
signature = calculate_signature(to_sign_str, sig_method, secret_key)

# Use the resulting value as the value of the Signature request parameter
print(signature)
