import base64
import hashlib
import hmac
import json
import os
import time
import uuid

import requests
from dotenv import load_dotenv

load_dotenv()

apiHeader = {}
token = os.getenv("TOKEN")
secretStr = os.getenv("SECRET")
if token is None or secretStr is None:
    print("Please set TOKEN and SECRET in .env file")
    exit(1)
nonce = uuid.uuid4()
t = int(round(time.time() * 1000))

string_to_sign = "{}{}{}".format(token, t, nonce)
secret = bytes(secretStr, "utf-8")

sign = base64.b64encode(
    hmac.new(
        secret, msg=bytes(string_to_sign, "utf-8"), digestmod=hashlib.sha256
    ).digest()
)

# Build api header JSON
apiHeader["Authorization"] = token
apiHeader["Content-Type"] = "application/json"
apiHeader["charset"] = "utf8"
apiHeader["t"] = str(t)
apiHeader["sign"] = str(sign, "utf-8")
apiHeader["nonce"] = str(nonce)

# # https://api.switch-bot.com/v1.1/devices
# url = 'https://api.switch-bot.com/v1.0/devices'
# response = requests.get(url, headers=apiHeader)
# print(response.json())

device_id = os.getenv("DEVICE_ID")
if device_id is None:
    print("Please set DEVICE_ID in .env file")
    exit(1)
# https://api.switch-bot.com/v1.0/devices/{device_id}/commands
url = "https://api.switch-bot.com/v1.0/devices/{}/commands".format(device_id)
data = {"command": "brightnessDown"}
response = requests.post(url, headers=apiHeader, data=json.dumps(data))
print(response.json())
