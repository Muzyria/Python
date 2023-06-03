import hashlib
import hmac
import base64

def generate_signature(to_sign_str, secret_key, sig_method):
    key = secret_key.encode('utf-8')
    message = to_sign_str.encode('utf-8')
    signature = hmac.new(key, message, getattr(hashlib, sig_method)).digest()
    signature = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
    return signature

# Пример использования
to_sign_str = "UserAccountLogin/FVyzsVqr-BmP280/1.0/2.0/HmacSHA256/230602154652+0300/JSON"
secret_key = "7Tk_QvgGL3hfCZMgUOrlOm417pXfdPVu-lCdYnc9vaG340vbmPEKNhqFjGmh"
sig_method = "SHA256"

signature = generate_signature(to_sign_str, secret_key, sig_method)
print(signature)