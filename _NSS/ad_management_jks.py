import time
import requests
import sys
import io
import simplejson

import signaturehelper


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


BASE_URL = 'https://api.naver.com'
API_KEY = '01000000001d5ca1db71c079ad263b11e935295937bae46b8d3059b8a62dce42f5b4859a08'
SECRET_KEY = 'AQAAAAAdXKHbccB5rSY7Eek1KVk3SO/zdlM9Xe+bFW19EB32LA=='
CUSTOMER_ID = '1609491'


##################
uri = '/keywordstool'
method = 'GET'
r = requests.get(BASE_URL + uri, params={'hintKeywords': '앵글선반'}, headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

print("response status_code = {}".format(r.status_code))

loadData = simplejson.loads(r.content)
keywordData = loadData["keywordList"]

for oneData in keywordData:
    print("oneData >> ", oneData)

# print("response body = {}".format(r.content))
