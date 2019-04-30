# Causes a repeated flow of lights from left to right
import requests
import time

URL = "https://172.28.219.225/api/NA4t9hTylAS7RWzmw4VYXrbSb2VnPpDIA4ctvrWe"
wait = .2

while 1:
    requests.put(URL + "/lights/1/state", "{\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/2/state", "{\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/3/state", "{\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/4/state", "{\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/1/state", "{\"on\": false}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/2/state", "{\"on\": false}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/3/state", "{\"on\": false}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/4/state", "{\"on\": false}", verify=False)
    # time.sleep(wait)
