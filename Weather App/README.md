This is a simple Python-based weather application that fetches real-time weather data for any city using the WeatherAPI and optionally speaks the results using text-to-speech (TTS).

🚀 Features
Get current weather conditions for any city.

Displays temperature (°C and °F), wind speed and direction, pressure, and precipitation.

Uses WeatherAPI for accurate, real-time data.

Converts weather report to speech using pyttsx3.

🛠️ Requirements
Install the required Python libraries using pip:
bash
Copy
Edit
pip install requests pyttsx3

🔑 API Key
This app uses WeatherAPI to fetch weather data.
You will need to sign up on their website and get a free API key.

Replace this line in the code with your own API key:
url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"


📄 How to Use
Clone the repository or copy the script.
Install the dependencies.
Run the script:

python weather.py
Enter the name of the city when prompted.

The app will display weather data and speak the results using text-to-speech.


🔉 Text-to-Speech Output
Temperature in London is 15 degree Celsius
Condition in London is Partly cloudy
Wind speed in London is 13 kilometers per hour
