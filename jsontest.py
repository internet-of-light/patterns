# Example of json parsing for the color of light eleven (11) in the lobby


import json
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "http://172.28.219.179/api/rARKEpLebwXuW01cNVvQbnDEkd2bd56Nj-hpTETB"
sleepTime = .2


r = requests.get(URL + "/lights/11")

j = json.loads(r.text)

print j["state"]["xy"]
