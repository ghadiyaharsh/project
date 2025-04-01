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
print(weatherdic["current"]["condition"]["icon"])
print(weatherdic["current"]["wind_kph"])
print(weatherdic["current"]["wind_degree"])
print(weatherdic["current"]["wind_dir"])
print(weatherdic["current"]["pressure_mb"])
print(weatherdic["current"]["pressure_in"])
print(weatherdic["current"]["precip_mm"])
print(weatherdic["current"]["precip_in"])
#if we ant to listen the temperature of the city we use the text to speech
import pyttsx3
harshg = pyttsx3.init()
harshg.say(f"Temperature in {city} is {weatherdic['current']['temp_c']} degree celsius") 
harshg.say(f"Temperature in {city} is {weatherdic['current']['temp_f']} degree fahrenheit")
harshg.say(f"Condition in {city} is {weatherdic['current']['condition']['text']}")
harshg.say(f"Wind speed in {city} is {weatherdic['current']['wind_kph']} kilometer per hour")    
harshg.say(f"Wind direction in {city} is {weatherdic['current']['wind_dir']}")
harshg.say(f"Pressure in {city} is {weatherdic['current']['pressure_mb']} millibar")
harshg.say(f"Precipitation in {city} is {weatherdic['current']['precip_mm']} millimeter")
harshg.say(f"Pressure in {city} is {weatherdic['current']['pressure_in']} inch")
harshg.say(f"Precipitation in {city} is {weatherdic['current']['precip_in']} inch")

harshg.runAndWait()
