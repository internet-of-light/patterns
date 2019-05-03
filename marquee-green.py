import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://172.28.219.225/api/NA4t9hTylAS7RWzmw4VYXrbSb2VnPpDIA4ctvrWe"
sleepTime = .2

# Turns off all lights as a baseline
for i in range(4):
    q = i + 1
    requests.put(URL + "/lights/" + str(q) + "/state", "{\"on\": false}", verify=False)

# Infinite loop; manual stop required
while 1:
    # Turn on 1 and 3 [ |  O  |  O ]
    requests.put(URL + "/lights/1/state", "{\"on\": true}", verify=False)
    requests.put(URL + "/lights/3/state", "{\"on\": true}", verify=False)
    time.sleep(sleepTime)
    # Turn on 2 and 4; turn off 1 and 3 [ O  |  O  | ]
    requests.put(URL + "/lights/1/state", "{\"on\": false}", verify=False)
    requests.put(URL + "/lights/3/state", "{\"on\": false}", verify=False)
    requests.put(URL + "/lights/2/state", "{\"on\": true}", verify=False)
    requests.put(URL + "/lights/4/state", "{\"on\": true}", verify=False)
    time.sleep(sleepTime)
    # Turn off 2 and 4 in prep for loop [ O  O  O  O ]
    requests.put(URL + "/lights/2/state", "{\"on\": false}", verify=False)
    requests.put(URL + "/lights/4/state", "{\"on\": false}", verify=False)