import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Green Bridge
IP = "172.28.219.225"
uname = "NA4t9hTylAS7RWzmw4VYXrbSb2VnPpDIA4ctvrWe"

URL = "https://" + IP + "/api/" + uname
wait = .2

requests.put(URL + "/groups/1/action", "{\"on\": true, \"xy\":[0.675,0.322], \"transitiontime\": 1}", verify=False)

time.sleep(4)

requests.put(URL + "/groups/1/action", "{\"xy\":[0.300,0.300], \"transitiontime\": 50}", verify=False)
