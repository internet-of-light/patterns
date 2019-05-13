# test animation for red player winning a game in the lower lobby

import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://172.28.219.179/api/NA4t9hTylAS7RWzmw4VYXrbSb2VnPpDIA4ctvrWe"
sleepTime = .2

white = "[0.400,0.400]"
red = "[0.675,0.322]"

#requests.put(URL + "/groups/1/action", "{\"on\": true, \"transitiontime\": 1}", verify=False)

time.sleep(sleepTime)

requests.put(URL + "/lights/11/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/14/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/16/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/23/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/7/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/21/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/10/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/15/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/22/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)

# flash here

requests.put(URL + "/groups/1/action", "{\"on\": false, \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/groups/1/action", "{\"on\": true, \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/groups/1/action", "{\"on\": false, \"transitiontime\": 1}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/groups/1/action", "{\"on\": true, \"transitiontime\": 1}", verify=False)

# Transition back

time.sleep(4)
requests.put(URL + "/groups/1/action", "{\"xy\": " + white + ", \"transitiontime\": 40}", verify=False)