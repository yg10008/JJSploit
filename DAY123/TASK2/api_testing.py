import requests
from dotenv import load_dotenv
import os
from JSONparsing import JSONparsing


load_dotenv()
api = os.getenv("weather_api")

lat = 28.6139
lon = 77.2090

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

def test_api():
    print("We are going to test the weather API:")
    res = requests.get(url)
    if res.status_code == 200:
        JSONparsing(res)
    else:
        print("API is not working fine")
        print("Status Code:", res.status_code)
        print("Response:", res.json())

print("We are going to call test_api function...")
test_api()
