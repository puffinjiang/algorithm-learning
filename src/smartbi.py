import json
from urllib.parse import urlencode

import requests

session = requests.Session()
url = "http://192.168.1.100:18080/smartbi/vision/RMIServlet"
params = "className=UserService&methodName=login&params=%5B%22admin%22%2C%22CHgnPZvgsQwVVY7%22%5D"
header = {"Content-type": "application/x-www-form-urlencoded;charset=UTF-8"}
params = ["admin", "CHgnPZvgsQwVVY7"]

data = urlencode(
    {"className": "UserService", "methodName": "login", "params": json.dumps(params, separators=(',', ':'))})
print(data)
# res = session.post(url, data=data, headers=header, timeout=10)
# print(res.json())
# result = res.json().get('result')
# session.cookies = res.cookies
# print(res.cookies)
c = requests.cookies.RequestsCookieJar()
cookie = {"JSESSIONID":"35F70212ED899FBC2231395F4A81F041"}
for key,value in cookie.items():
    c.set(key,value)
session.cookies.update(c)
# if result:
data = urlencode(
    {"className": "LoginTokenModule", "methodName": "generateLoginToken",
     "params": json.dumps(["pengfei.jiang-a1805@aqara.com"], separators=(',', ':'))})
res = session.post(url, data=data, headers=header)
print(res.json())
