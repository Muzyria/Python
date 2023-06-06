import hashlib
import hmac
import base64
import time

host = "https://dev-api.syncwise360.com"
SLASH = "/"
APIVersion = "1.0"
SignatureVersion = "2.0"
SignatureMethod = "HmacSHA256"
ResponseFormat = "JSON"


def create_url_test_with_private():
    application_api_key = "FVyzsVqr-BmP280"
    application_secret_key = "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"

    user_secret_key = "4AHtsKkyBhBtdRjU40O6pC3FnJo-dr5FSi_QwjQcoU2LklM1ZLFrp8IJaRMu"
    username = "igorperetssuperior"

    print(get_url_for_action("CourseGeofenceList", True, user_secret_key, username,
                             application_api_key, application_secret_key))


def create_url_test_with_public():
    application_api_key = "FVyzsVqr-BmP280"
    application_secret_key = "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"

    user_secret_key = ""
    username = ""

    print(get_url_for_action("CourseGeofenceList", False, user_secret_key, username,
                             application_api_key, application_secret_key))


def get_url_for_action(action, is_private, secret_key, username, application_api_key, application_secret_key):
    url_builder = []
    url_end = []

    url_builder.append(action)
    url_builder.append(SLASH)
    url_builder.append(application_api_key)
    url_builder.append(SLASH)

    if is_private:
        url_builder.append(username)
        url_builder.append(SLASH)

    url_builder.append(APIVersion)
    url_builder.append(SLASH)
    url_builder.append(SignatureVersion)
    url_builder.append(SLASH)
    url_builder.append(SignatureMethod)
    url_builder.append(SLASH)

    # Signature

    url_end.append(get_timestamp())
    url_end.append(SLASH)
    url_end.append(ResponseFormat)

    src = "".join(url_builder) + "".join(url_end)

    if is_private:
        signature = make_signature(src, application_secret_key + secret_key)
    else:
        signature = make_signature(src, application_secret_key)

    url_builder.append(signature)
    url_builder.append(SLASH)
    url_builder.append("".join(url_end))

    return "".join(url_builder)


def get_timestamp():
    return time.strftime("%y%m%d%H%M%S%z")


def make_signature(src, secret):
    try:
        sc = secret.encode('utf-8')
        bt = hmac.new(sc, src.encode('utf-8'), hashlib.sha256).digest()
        s = base64.urlsafe_b64encode(bt).rstrip(b'=').decode('utf-8')

        return s.replace('+', '-').replace('/', '_')
    except Exception as e:
        raise RuntimeError(e)


# использования
