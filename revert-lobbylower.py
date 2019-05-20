import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://172.28.219.179/api/rARKEpLebwXuW01cNVvQbnDEkd2bd56Nj-hpTETB"
sleepTime = 1

white = "[0.486,0.460]"
red = "[0.675,0.322]"

requests.put(URL + "/groups/1/action", "{\"on\": true, \"xy\":" + white + ", \"bri\": 254}", verify=False)