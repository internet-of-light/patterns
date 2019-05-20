import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://172.28.219.179/api/rARKEpLebwXuW01cNVvQbnDEkd2bd56Nj-hpTETB"
sleepTime = 1

white_seq = "\"bri\": 100, \"hue\": 9000, \"sat\": 200"
red = "[0.675,0.322]"

requests.put(URL + "/groups/1/action", "{\"on\": true, " + white_seq + "}", verify=False)