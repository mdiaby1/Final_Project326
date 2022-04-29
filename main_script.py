'''Our app will tell user about the weather of a city specified by user
'''
import json
import requests

class City:
    '''Holds information about the city that the user enters
    Attributes - City that user wants the weather information of
    '''
    def __init__(self, name):
        self.name = name
        #you will pass in the name of the city into the api_access function
        #then you will get all of this weather data from the api
        
        
        
        #self.current_temp =call to api access function for json data
        #self.feels_like_temp =call to api access function for json data
        #self.max_temp
        #self.min_temp
        #self.air_pressure
        #self.humidity
        #self.cloudiness
        #self.wind_speed
        #self.wind_direction = call to api acccess functio
        
def Trend():
    '''function that analyzes the weather data of the city entered
    Args:
        City entered by user fron city class
    Returns:
        Returns weather from city
        
    '''
    pass

def api_access(city_name, weather_phenomena):
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
    weather_data = api_response,json()
    main_weather_measures = weather_data['main']
    clouds_data = weather_data['clouds']
    wind_data = weather_data['wind']
    
    #if weather_phenomena == "current_temp":
        #return current_temp by using a call to the api function