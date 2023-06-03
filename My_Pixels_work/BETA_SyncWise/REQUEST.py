import requests
import hashlib
import base64
import datetime


def create_signature(data, secret_key):
    signature_data = "/".join([str(data[key]) for key in sorted(data.keys())])
    signature = base64.urlsafe_b64encode(hashlib.sha256(signature_data.encode()).digest()).decode().replace("_",
                                                                                                            "/").replace(
        "-", "+").replace("=", "")
    return signature


def send_request(action, payload):
    host = "https://sandbox.syncwise360.com"
    app_api_key = "FVyzsVqr-BmP280"
    api_key = "FVyzsVqr-BmP280"
    api_version = "1.0"
    signature_version = "2.0"
    signature_method = "HmacSHA256"
    timestamp = datetime.datetime.now().strftime("%y%m%d%H%M%S%z")
    response_format = "JSON"

    data = {
        "Action Code": action,
        "App API Key": app_api_key,
        "API Key": api_key,
        "API Version": api_version,
        "Signature Version": signature_version,
        "Signature Method": signature_method,
        "Timestamp": timestamp,
        "Response Format": response_format
    }

    signature = create_signature(data, "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO")
    url = f"{host}/rest/action/{action}/{app_api_key}/{api_key}/{api_version}/{signature_version}/{signature_method}/{signature}/{timestamp}+0300/{response_format}"

    response = requests.post(url, json=payload)
    return response.json()


# Example usage
payload = {
  "username": "igorperetssuperior",
  "password": "1234"
}
response = send_request("UserAccountLogin", payload)
print(response)
