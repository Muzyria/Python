import hashlib
import hmac
import base64
import time

METHOD = "HmacSHA256"
CHARACTER_ENCODING = "UTF-8"

def calculate_signature(to_sign_str, sign_method, secret_key):
    secret_key_bytes = secret_key.encode(CHARACTER_ENCODING)
    mac = hmac.new(secret_key_bytes, to_sign_str.encode(CHARACTER_ENCODING), hashlib.sha256)
    raw_sig = mac.digest()
    s = base64.urlsafe_b64encode(raw_sig).decode(CHARACTER_ENCODING)
    return s

def to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format):
    builder = []
    builder.append(action_code)
    builder.append("/")
    builder.append(app_api_key)
    builder.append("/")
    builder.append(api_version)
    builder.append("/")
    builder.append(sig_version)
    builder.append("/")
    builder.append(sig_method)
    builder.append("/")
    builder.append(timestamp_str)
    builder.append("/")
    builder.append(response_format)
    return "".join(builder)

timestamp_str = time.strftime("%y%m%d%H%M%S%z")
to_sign_str = to_sign(action_code, app_api_key, api_version, sig_version, sig_method, timestamp_str, response_format)
signature = calculate_signature(to_sign_str, METHOD, secret_key)
