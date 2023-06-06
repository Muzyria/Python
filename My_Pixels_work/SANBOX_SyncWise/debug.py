
action_code = "UserAccountLogin"
app_api_key = "FVyzsVqr-BmP280"
api_version = "1.0"
signature_version = "2.0"
signature_method = "HmacSHA256"
signature = "pGPDLc-pJFXFOe7ztfRInVCTxm6lS3V_U1YIPZrpXUo"
timestamp = __import__('datetime').datetime.now().strftime('%y%m%d%H%M%S%z') #+ '+0300'

response_format = "JSON"

base_url = "https://dev-api.syncwise360.com/rest/action/"


print(timestamp)
