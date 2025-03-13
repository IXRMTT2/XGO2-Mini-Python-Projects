import requests
from xgoedu import XGOEDU
import time

# Initialize the XGOEDU module
XGO_edu = XGOEDU()

# Replace with your OpenWeatherMap API key
API_KEY = 'your_api_key_here'
CITY = 'your_city_here'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        return temperature, humidity, description
    else:
        print("Error fetching weather data")
        return None, None, None

def display_weather():
    while True:
        temperature, humidity, description = fetch_weather()
        if temperature is not None:
            XGO_edu.lcd_clear()
            XGO_edu.lcd_text(10, 10, f"Temp: {temperature} C", 2)
            XGO_edu.lcd_text(10, 40, f"Humidity: {humidity}%", 2)
            XGO_edu.lcd_text(10, 70, f"Desc: {description}", 2)
            print(f"Temp: {temperature} C, Humidity: {humidity}%, Desc: {description}")
        else:
            XGO_edu.lcd_clear()
            XGO_edu.lcd_text(10, 10, "Error fetching weather", 2)
            print("Error fetching weather data")

        time.sleep(600)  # Update every 10 minutes

if __name__ == "__main__":
    display_weather()