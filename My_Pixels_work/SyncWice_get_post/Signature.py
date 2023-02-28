import hashlib
import hmac
import base64
import time

def calculate_signature(to_sign_str, sign_method, secret_key):
    """Вычисляет подпись для строки"""
    message = to_sign_str.encode('utf-8')
    key = secret_key.encode('utf-8')
    if sign_method == 'HmacSHA256':
        algorithm = hashlib.sha256
    else:
        raise ValueError(f'Неподдерживаемый метод подписи: {sign_method}')
    signature = hmac.new(key, message, algorithm).digest()
    signature_b64 = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
    return signature_b64

def to_sign(action_id, app_api_key, api_key, api_version, sig_version, sig_method, response_format):
    """Создает строку для подписи"""
    timestamp_str = time.strftime('%y%m%d%H%M%S%z')
    params = [action_id, app_api_key, api_key, api_version, sig_version, sig_method, timestamp_str, response_format]
    params_str = '/'.join(params)
    print(timestamp_str)
    return params_str

# Пример использования
action_id = 'CourseGeofenceList'
app_api_key = 'FVyzsVqr-BmP280'
api_key = 'igorperetssuperior'
api_version = '1.0'
sig_version = '2.0'
sig_method = 'HmacSHA256'
response_format = 'JSON'
secret_key = 'F6ozDPUhzZCu4VFQk_hyPcfDxLdrdslOX232r9GmjY1tB-rutihBlol6kT8J' # 'your_application_secret_key'

to_sign_str = to_sign(action_id, app_api_key, api_key, api_version, sig_version, sig_method, response_format)
signature = calculate_signature(to_sign_str, sig_method, secret_key)

# Добавьте полученную подпись в параметры запроса

# print(to_sign_str)
print(signature)