import requests
import json

data = requests.get("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCj_bAQA7Rmxebtgaq08ykLXl1cxA03o0c").text


print(data)