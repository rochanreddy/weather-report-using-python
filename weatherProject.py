import requests
import json
while True:
    city= input("enter the city or q for exit:")
    if city=="q":
        print("Thank You")
        break
    url=f"https://api.weatherapi.com/v1/current.json?key=5bece88a00e3449e9fa72418241405&q={city}"

    r=requests.get(url)
    Wdic=json.loads(r.text)
    print(f"the temperature in {city} is :",Wdic["current"]["temp_c"])
    print("it feels like:",Wdic["current"]["feelslike_c"])
    print("the wind speed in kph:",Wdic["current"]["wind_kph"])