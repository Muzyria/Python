# import hashlib
# import hmac
# import base64
# import time
#
# def create_signature(action_code, app_api_key, api_version, sig_version, sig_method, secret_key, user_key=None, timestamp=None, response_format='JSON'):
#     # Step 1: Create the string to sign
#     if user_key:
#         string_to_sign = f"{action_code}/{app_api_key}/{user_key}/{api_version}/{sig_version}/{sig_method}/{timestamp}/{response_format}"
#     else:
#         string_to_sign = f"{action_code}/{app_api_key}/{api_version}/{sig_version}/{sig_method}/{timestamp}/{response_format}"
#
#     # Step 2: Concatenate the keys
#     if user_key:
#         composite_key = f"{secret_key}{user_key}"
#     else:
#         composite_key = secret_key
#
#     # Step 3: Configure the HMAC encryption algorithm
#     hmac_algorithm = hashlib.sha256
#
#     # Step 4: Create the hash
#     hmac_hash = hmac.new(composite_key.encode('utf-8'), string_to_sign.encode('utf-8'), hmac_algorithm).digest()
#
#     # Step 5: Convert the hash to base64 URL and Filename Safe Alphabet encoding
#     signature = base64.urlsafe_b64encode(hmac_hash).decode('utf-8').rstrip('=')
#
#     # Step 6: Return the signature
#     return signature
#
# action_code = 'UserLogin'
# app_api_key = 'uUqnXUKU86kghJk'
# api_version = '1.0'
# sig_version = '2.0'
# sig_method = 'HmacSHA256'
# secret_key = 'my_secret_key'
# user_key = 'testigolf@igolf.com'
# response_format = 'JSON'
# timestamp = str(int(time.time()))
#
# signature = create_signature(action_code, app_api_key, api_version, sig_version, sig_method, secret_key, user_key, timestamp, response_format)
# print(signature)


import hmac
import hashlib
import base64
from urllib.parse import quote

def calculate_signature(to_sign, secret_key, sign_method):
    # Concatenate Keys
    composite_key = secret_key

    # Configure the HMAC Encryption Algorithm
    hmac_algorithm = hmac.new(bytes(composite_key, 'utf-8'), msg=bytes(to_sign, 'utf-8'), digestmod=hashlib.sha256)

    # Create Hash
    hmac_digest = hmac_algorithm.digest()

    # Convert Hash
    base64_encoded_hash = base64.urlsafe_b64encode(hmac_digest).decode()

    return quote(base64_encoded_hash)

def create_string_to_sign(params, private_action):
    # Create StringToSign
    if private_action:
        string_to_sign = f"{params['ActionID']}/{params['AppAPIKey']}/{params['APIKey']}/{params['APIVersion']}/{params['SignatureVersion']}/{params['SignatureMethod']}/{params['Timestamp']}/{params['ResponseFormat']}"
    else:
        string_to_sign = f"{params['ActionID']}/{params['AppAPIKey']}/{params['APIVersion']}/{params['SignatureVersion']}/{params['SignatureMethod']}/{params['Timestamp']}/{params['ResponseFormat']}"

    return string_to_sign

# Example usage
params = {
    'ActionID': 'UserLogin',
    'AppAPIKey': 'uUqnXUKU86kghJk',
    'APIKey': 'testigolf@igolf.com',
    'APIVersion': '1.0',
    'SignatureVersion': '2.0',
    'SignatureMethod': 'HmacSHA256',
    'Timestamp': '121224235920+0200',
    'ResponseFormat': 'JSON'
}

private_action = True
secret_key = '30_character_application_secret_key'
user_key = '40_character_user_key'

if private_action:
    composite_key = secret_key + user_key
else:
    composite_key = secret_key

to_sign = create_string_to_sign(params, private_action)
signature = calculate_signature(to_sign, composite_key, params['SignatureMethod'])

# Add to Common Parameters
params['Signature'] = signature

# Use the params dictionary in the request sent to the server
