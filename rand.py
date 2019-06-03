import requests
import random
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

digits = [11, 14, 16, 23, 7, 21, 10, 15, 22]
lastEdit = 0
URL = "https://172.28.219.179/api/rARKEpLebwXuW01cNVvQbnDEkd2bd56Nj-hpTETB"

def gen():
    return "\"bri\": 100, \"hue\": " + str(random.randint(0,65200)) + ", \"sat\": 200"

while 1:
    srt = gen()
    random.shuffle(digits)
    x = 0
    if lastEdit != digits[0]:
        x = digits[0]
        lastEdit = digits[0]
    else:
        x = digits[1]
        lastEdit = digits[1]
    requests.put(URL + "/lights/" + str(x) + "/state", "{" + srt + ", \"transitiontime\": 15}", verify=False)
    time.sleep(1)