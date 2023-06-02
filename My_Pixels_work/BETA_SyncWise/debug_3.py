import requests
import json
import hashlib
import hmac
import time
import datetime

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
    # First, carefully read the documentation of Request Authentication

    config = {
        "host": "https://api-dna.igolf.com",  # live environment for sw360
        "apiKey": "FVyzsVqr-BmP280",
        "secretKey": "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO",
    }

    user_secret_key = 'fY15nmthrxp8oo6VT5QuW4fNWDXxg9gJ0rW4lWQdEp-7UICbPdhfuJznjBww'  # replace with actual value from sessionStorage
    user_name = "igorperetssuperior"  # replace with actual value from sessionStorage

    is_public_action = action in public_actions

    api_params = {
        "action": action,
        "apiKey": config["apiKey"],
        "username": user_name + "/" if not is_public_action and user_name else "",
        "apiVersion": "1.0",
        "signatureVersion": "2.0",
        "signatureMethod": "HmacSHA256",
        "timestamp": datetime.datetime.utcnow().strftime("%y%m%d%H%M%S"),
        "responseFormat": "JSON",
    }

    signature_string = "/".join([str(api_params[key]) for key in sorted(api_params.keys()) if api_params[key]])
    signature = hmac.new(config["secretKey"].encode(), signature_string.encode(), hashlib.sha256).hexdigest()

    url = "{}/rest/action/{}/{}/{}/{}/{}/{}/{}/{}".format(
        config["host"],
        api_params["action"],
        api_params["apiKey"],
        api_params["username"],
        api_params["apiVersion"],
        api_params["signatureVersion"],
        api_params["signatureMethod"],
        signature,
        api_params["timestamp"],
    )

    headers = {
        "Content-Type": "application/json"
    }

    res = requests.post(url, headers=headers, json=body)

    return res.json()

body = {
    "username": "igorperetssuperior",
    "password": "1234"
}

print(request("UserAccountLogin", body))
