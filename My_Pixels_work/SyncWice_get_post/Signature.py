import hashlib
import hmac
import base64

METHOD = "HmacSHA256"
CHARACTER_ENCODING = "UTF-8"

secret_key = "my_secret_key"  # замените на ваш секретный ключ
secret_key_bytes = secret_key.encode(CHARACTER_ENCODING)
to_sign = "data_to_sign"  # замените на данные, которые необходимо подписать
to_sign_bytes = to_sign.encode(CHARACTER_ENCODING)
mac = hmac.new(secret_key_bytes, msg=to_sign_bytes, digestmod=hashlib.sha256)
raw_sig = mac.digest()
signature = base64.urlsafe_b64encode(raw_sig).decode(CHARACTER_ENCODING)


