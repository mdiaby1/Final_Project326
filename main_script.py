'''Our app will tell user about the weather of a city specified by user
'''
import json
import requests

class City:
    '''Holds information about the city that the user enters
    Attributes - City that user wants the weather information of
    '''
    def __init__(self, name):
        #you need to perform input validation on the name of the city the user provides
        self.name = name
        
        self.current_temp = access_api(self.name, 'current_temp')
        self.feels_like_temp = access_api(self.name, 'feels_like_temp')
        self.max_temp = access_api(self.name, 'max_temp')
        self.min_temp = access_api(self.name, 'min_temp')
        self.air_pressure = access_api(self.name, 'air_pressure')
        self.humidity = access_api(self.name, 'humidity')
        self.cloudiness = access_api(self.name, 'cloudiness')
        self.wind_speed = access_api(self.name, 'wind_speed')
        self.wind_direction = access_api(self.name, 'wind_direction')
        
def Trend():
    '''function that analyzes the weather data of the city entered
    Args:
        City entered by user fron city class
    Returns:
        Returns weather from city
        
    '''
    pass

def access_api(city_name, weather_phenomena):
    '''works with the openweather api
    Args:
        The name of the city entered and teh weather associated with that city
    Side Effects:
        gets weather data from open weather api
    '''    
    
    api_key = "0cc0e4d9235938991e58db115667109b"
    base_url =  "https://api.openweathermap.org/data/2.5/weather?"
    updated_url = base_url + api_key + city_name #this is incorrect
    api_response = requests.get(updated_url)
    weather_data = api_response.json()
    
    main_weather_measures = weather_data['main']
    clouds_data = weather_data['clouds']
    wind_data = weather_data['wind']
    
    if weather_phenomena == "current_temp":
        current_temp_kelvin_to_fahr = (main_weather_measures["temp"] - 273.15) * 9/5 + 32
        return current_temp_kelvin_to_fahr
    elif weather_phenomena == "feels_like_temp":
        feels_like_temp_kelvin_to_fahr = (main_weather_measures["feels_like"] - 273.15) * 9/5 + 32
        return feels_like_temp_kelvin_to_fahr
    elif weather_phenomena == "max_temp":
        max_temp_kelvin_to_fahr = (main_weather_measures["temp_max"] - 273.15) * 9/5 + 32
        return max_temp_kelvin_to_fahr
    elif weather_phenomena == "min_temp":
        min_temp_kelvin_to_fahr = (main_weather_measures["temp_min"] - 273.15) * 9/5 + 32
        return min_temp_kelvin_to_fahr
    elif weather_phenomena == "air_pressure":
        air_pressure_hpa_to_inHg = (main_weather_measures["pressure"]) * 0.03
        return air_pressure_hpa_to_inHg
    elif weather_phenomena == "humidity":
        humidity_percentage_data = main_weather_measures["humidity"]
        return humidity_percentage_data
    elif weather_phenomena == "cloudiness":
        cloudiness_percentage_data = clouds_data["all"]
        return cloudiness_percentage_data
    elif weather_phenomena == "wind_speed":
        wind_speed_ms_to_mph = wind_data["speed"] * 2.237
        return wind_speed_ms_to_mph
    elif weather_phenomena == "wind_direction":
        wind_direction_data = wind_data["deg"]
        return wind_direction_data