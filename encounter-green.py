import requests
import time

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import vlc

# p = vlc.MediaPlayer("file:///test.mp3")

URL = "https://172.28.219.225/api/NA4t9hTylAS7RWzmw4VYXrbSb2VnPpDIA4ctvrWe"
wait = .2

requests.put(URL + "/groups/1/action", "{\"on\": true, \"xy\":[0.675,0.322]}", verify=False)
# requests.put(URL + "/groups/1/action", "{\"xy\":[0.675,0.322]}", verify=False)
# requests.put(URL + "/lights/1/state", "{\"on\": true}", verify=False)
# requests.put(URL + "/lights/1/state", "{\"xy\":[0.675,0.322]}", verify=False)
# requests.put(URL + "/lights/2/state", "{\"on\": true}", verify=False)
# requests.put(URL + "/lights/2/state", "{\"xy\":[0.675,0.322]}", verify=False)
# requests.put(URL + "/lights/3/state", "{\"on\": true}", verify=False)
# requests.put(URL + "/lights/3/state", "{\"xy\":[0.675,0.322]}", verify=False)
# requests.put(URL + "/lights/4/state", "{\"on\": true}", verify=False)
# requests.put(URL + "/lights/4/state", "{\"xy\":[0.675,0.322]}", verify=False)

time.sleep(7)

requests.put(URL + "/groups/1/action", "{\"xy\":[0.300,0.300]}", verify=False)
# requests.put(URL + "/lights/1/state", "{\"xy\":[0.300,0.300]}", verify=False)
# requests.put(URL + "/lights/2/state", "{\"xy\":[0.300,0.300]}", verify=False)
# requests.put(URL + "/lights/3/state", "{\"xy\":[0.300,0.300]}", verify=False)
# requests.put(URL + "/lights/4/state", "{\"xy\":[0.300,0.300]}", verify=False)
