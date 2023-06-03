import hashlib
import hmac
import base64
from urllib.parse import quote

def generate_signature_public(action_code, app_api_key, api_version, signature_version, signature_method, timestamp, response_format):
    string_to_sign = "/".join([action_code, app_api_key, api_version, signature_version, signature_method, timestamp, response_format])

    signature = hmac.new(app_secret_key.encode(), string_to_sign.encode(), hashlib.sha256).digest()
    signature_base64 = base64.urlsafe_b64encode(signature).decode()

    return quote(signature_base64, safe='')

# Example usage:
app_api_key = "[Client Key]"
app_secret_key = "[30 character Application Secret Key]"
action_code = "[Action Name]"
api_version = "1.0"
signature_version = "2.0"
signature_method = "HmacSHA256"
timestamp = "121224230903+0200"
response_format = "JSON"

signature = generate_signature_public(action_code, app_api_key, api_version, signature_version, signature_method, timestamp, response_format)
print(signature)