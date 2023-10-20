import hashlib
import hmac
import base64
import time

class SyncwiseAPI:
    def __init__(self, host):
        self.host = host
        self.SLASH = "/"
        self.APIVersion = "1.0"
        self.SignatureVersion = "2.0"
        self.SignatureMethod = "HmacSHA256"
        self.ResponseFormat = "JSON"

    def create_url_test_with_public(self):
        application_api_key = "FVyzsVqr-BmP280"
        application_secret_key = "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"
        user_secret_key = ""
        username = ""

        url = self.get_url_for_action("UserAccountLogin", False, user_secret_key, username,
                                      application_api_key, application_secret_key)
        print(f'PUBLIC {url}')
        return url

    def create_url_test_with_private(self, action, user_secret_key):
        application_api_key = "FVyzsVqr-BmP280"
        application_secret_key = "L4ccbyhS9xlDjd3vgnw_LZTqsrCvLO"
        username = "igorperetssuperior"

        url = self.get_url_for_action(action, True, user_secret_key, username,
                                      application_api_key, application_secret_key)
        print(f'PRIVATE {url}')
        return url

    def get_url_for_action(self, action, is_private, secret_key, username, application_api_key, application_secret_key):
        url_builder = []
        url_end = []

        url_builder.append(action)
        url_builder.append(self.SLASH)
        url_builder.append(application_api_key)
        url_builder.append(self.SLASH)

        if is_private:
            url_builder.append(username)
            url_builder.append(self.SLASH)

        url_builder.append(self.APIVersion)
        url_builder.append(self.SLASH)
        url_builder.append(self.SignatureVersion)
        url_builder.append(self.SLASH)
        url_builder.append(self.SignatureMethod)
        url_builder.append(self.SLASH)

        # Signature

        url_end.append(self.get_timestamp())
        url_end.append(self.SLASH)
        url_end.append(self.ResponseFormat)

        src = "".join(url_builder) + "".join(url_end)

        if is_private:
            signature = self.make_signature(src, application_secret_key + secret_key)
        else:
            signature = self.make_signature(src, application_secret_key)

        url_builder.append(signature)
        url_builder.append(self.SLASH)
        url_builder.append("".join(url_end))

        return "".join(url_builder)

    def get_timestamp(self):
        return time.strftime("%y%m%d%H%M%S%z")

    def make_signature(self, src, secret):
        try:
            sc = secret.encode('utf-8')
            bt = hmac.new(sc, src.encode('utf-8'), hashlib.sha256).digest()
            s = base64.urlsafe_b64encode(bt).rstrip(b'=').decode('utf-8')

            return s.replace('+', '-').replace('/', '_')
        except Exception as e:
            raise RuntimeError(e)
