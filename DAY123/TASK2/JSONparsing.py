def JSONparsing(jsonString) :
        data= jsonString.json()
        city = data.get('name')
        country = data['sys'].get('country')
        weather = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Location: {city}, {country}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temp_celsius} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")