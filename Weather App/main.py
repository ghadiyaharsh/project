import requests #used for take things from internet
import json

city = input("Enter the  name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=a29e3994898d4a19a0131414252503&q={city}"

data = requests.get(url) #get the data from the url
print(data.text)  #print the data
weatherdic = json.loads(data.text) #convert the data into dictionary
print(weatherdic["current"]["temp_c"])
print(weatherdic["current"]["temp_f"])
print(weatherdic["current"]["condition"]["text"])
