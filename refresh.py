import requests
import time

URL = "https://rohitzerodha.herokuapp.com/welcome"

while True:
    r = requests.get(url = URL)
    time.sleep(25)
