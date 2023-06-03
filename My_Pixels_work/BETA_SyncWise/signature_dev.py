import requests
import datetime
import hashlib
import base64

public_actions = [
    "AdminUserLogin",
    "UserAccountLogin",
    "UserAccountSwipeLogin",
    "UserAccountPasswordReset",
    "CompanyProfileSignup",
    "InformationRequestCreate",
    "CourseList",
    "CountryList",
    "StateList",
    "CustomerNewsletterUnsubscribe",
    "CorporateFAQList",
    "PressReleaseList",
    "ModuleList",
    "ModuleDetails"
]

def request(action, body):
    is_public_action = action in public_actions

    config = {
        "host": "https://sandbox.syncwise360.com",  # live environment for sw360
        "apiKey": "FVyzsVqr-BmP280",
        "secretKey": "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"
    }


    # Get saved data from sessionStorage
    # user_secret_key = sessionStorage.get("sectretKey")
    # user_name = sessionStorage.get("userName")
    user_secret_key = ''
    user_name = ''

    config["host"] = "https://sandbox.syncwise360.com"  # dev test environment for sw360
    config["apiKey"] = "FVyzsVqr-BmP280"

    config["secretKey"] = "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO" + user_secret_key if not is_public_action and user_secret_key else "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"

    api_params = {
        "action": action,
        "apiKey": config["apiKey"],
        "username": user_name + "/" if not is_public_action and user_name else "",
        "apiVersion": "1.0",
        "signatureVersion": "2.0",
        "signatureMethod": "HmacSHA256",
        "timestamp": datetime.datetime.now().strftime("%y%m%d%H%M%S%z"),
        "responseFormat": "JSON"
    }

    signature_data = "/".join([str(api_params[key]) for key in sorted(api_params.keys()) if api_params[key]])

    signature = base64.urlsafe_b64encode(hashlib.sha256(signature_data.encode()).digest()).decode().replace("_", "/").replace("-", "+").replace("=", "")

    url = f"{config['host']}/rest/action/{api_params['action']}/{api_params['apiKey']}/{api_params['username']}{api_params['apiVersion']}/{api_params['signatureVersion']}/{api_params['signatureMethod']}/{signature}/{api_params['timestamp']}+0300/{api_params['responseFormat']}"
    print(url)


    res = requests.post(url, json=body, headers={"Content-Type": "application/json"})


    return res.json()

try:
    response = request('UserAccountLogin', {"username": "igorperetssuperior", "password": "1234"})

except Exception as e:
    print('Error:', str(e))


