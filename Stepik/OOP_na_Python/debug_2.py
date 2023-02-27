import hashlib
import hmac
import base64
import time

def create_signature(action_code, app_api_key, api_version, sig_version, sig_method, secret_key, user_key=None, timestamp=None, response_format='JSON'):
    # Step 1: Create the string to sign
    if user_key:
        string_to_sign = f"{action_code}/{app_api_key}/{user_key}/{api_version}/{sig_version}/{sig_method}/{timestamp}/{response_format}"
    else:
        string_to_sign = f"{action_code}/{app_api_key}/{api_version}/{sig_version}/{sig_method}/{timestamp}/{response_format}"

    # Step 2: Concatenate the keys
    if user_key:
        composite_key = f"{secret_key}{user_key}"
    else:
        composite_key = secret_key

    # Step 3: Configure the HMAC encryption algorithm
    hmac_algorithm = hashlib.sha256

    # Step 4: Create the hash
    hmac_hash = hmac.new(composite_key.encode('utf-8'), string_to_sign.encode('utf-8'), hmac_algorithm).digest()

    # Step 5: Convert the hash to base64 URL and Filename Safe Alphabet encoding
    signature = base64.urlsafe_b64encode(hmac_hash).decode('utf-8').rstrip('=')

    # Step 6: Return the signature
    return signature



action_code = 'UserLogin'
app_api_key = 'uUqnXUKU86kghJk'
api_version = '1.0'
sig_version = '2.0'
sig_method = 'HmacSHA256'
secret_key = 'my_secret_key'
user_key = 'testigolf@igolf.com'
response_format = 'JSON'
timestamp = str(int(time.time()))

signature = create_signature(action_code, app_api_key, api_version, sig_version, sig_method, secret_key, user_key, timestamp, response_format)
print(signature)
