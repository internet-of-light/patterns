# test animation for red player winning a game in the lower lobby

import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://172.28.219.179/api/rARKEpLebwXuW01cNVvQbnDEkd2bd56Nj-hpTETB"
sleepTime = .5

white = "[0.486,0.460]"
red = "[0.675,0.322]"

#requests.put(URL + "/groups/1/action", "{\"on\": true, \"transitiontime\": 1}", verify=False)

print('sequence start')

time.sleep(sleepTime)

requests.put(URL + "/lights/11/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/14/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/16/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/23/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/7/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/21/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/10/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/15/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)
requests.put(URL + "/lights/22/state", "{\"on\": true, \"xy\":" + red + ", \"transitiontime\": 5}", verify=False)
time.sleep(sleepTime)

# flash here

print('flash')

requests.put(URL + "/groups/1/action", "{\"bri\": 100, \"transitiontime\": 20}", verify=False)
time.sleep(sleepTime * 5)
requests.put(URL + "/groups/1/action", "{\"bri\": 254, \"transitiontime\": 20}", verify=False)
time.sleep(sleepTime * 5)
requests.put(URL + "/groups/1/action", "{\"bri\": 100, \"transitiontime\": 20}", verify=False)
time.sleep(sleepTime * 5)
requests.put(URL + "/groups/1/action", "{\"bri\": 254, \"transitiontime\": 20}", verify=False)

# Transition back
# This is where a handoff back to the main system would go, too

print('return')

time.sleep(5)
requests.put(URL + "/groups/1/action", "{\"on\": true, \"xy\": " + white + ", \"transitiontime\": 40, \"bri\": 254}", verify=False)

print('sequence finish')