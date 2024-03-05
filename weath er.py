import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == '404':
        print("City not found.")
    else:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
