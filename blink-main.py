import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https:///api/"
wait = 1

# yeahhhhhhh boiiiiiiiiii

def blink(light_id):
    print("blinking " + str(light_id))
    requests.put(URL + "/lights/" + str(light_id) + "/state", "\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/" + str(light_id) + "/state", "\"on\": false}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/" + str(light_id) + "/state", "\"on\": true}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/" + str(light_id) + "/state", "\"on\": false}", verify=False)
    time.sleep(wait)
    requests.put(URL + "/lights/" + str(light_id) + "/state", "\"on\": true}", verify=False)


for i in range(21):
    blink(i + 1)
