'''Our app will tell the user about the weather of a city they have selected
'''
import json
import requests

#NEED 6 MORE ORIGINAL FUNCTIONS - MORY & OTHER MEMBERS WILL DO THIS 
#NEED TO DOCUMENT CODE
#NEED TO INCLUDE UNIT TESTS (creating a city object, testing each function like city_and_state_validation)

class City:
    '''Holds information about the city that the user enters
    Attributes - City that user wants the weather information of
    '''
    def __init__(self, city_name, state):
        #you need to perform input validation on the name of the city and state the user provides; probably in the main?
        self.city_name = city_name
        self.state = state
        
        self.current_temp = access_api(self.name, self.state, 'current_temp')
        self.feels_like_temp = access_api(self.name, self.state, 'feels_like_temp')
        self.max_temp = access_api(self.name, self.state, 'max_temp')
        self.min_temp = access_api(self.name, self.state, 'min_temp')
        self.air_pressure = access_api(self.name, self.state, 'air_pressure')
        self.humidity = access_api(self.name, self.state, 'humidity')
        self.cloudiness = access_api(self.name, self.state, 'cloudiness')
        self.wind_speed = access_api(self.name, self.state, 'wind_speed')
        self.wind_direction = access_api(self.name, self.state, 'wind_direction')
        self.rain_volume_past_1hr_mm(self.name, self.state, "rain_1hr")
        self.rain_volume_past_3hr_mm(self.name, self.state, "rain_3hr")
        self.snow_volume_past_1hr_mm(self.name, self.state, "snow_1hr")
        self.snow_volume_past_3hr_mm(self.name, self.state, "snow_3hr")

#THIS Trend() FUNCTION IS OBSOLETE; WE WILL MAKE SEPARATE TREND FUNCTIONS FOR EFFICIENCY'S SAKE      
def Trend():
    '''function that analyzes the weather data of the city entered
    Args:
        City entered by user fron city class
    Returns:
        Returns weather from city
        
    '''
    pass

def access_api(city_name, state, weather_phenomena):
    '''works with the openweather api
    Args:
        The name of the city entered and teh weather associated with that city
    Side Effects:
        gets weather data from open weather api
    '''    
    api_key = "0cc0e4d9235938991e58db115667109b"
    base_url =  "https://api.openweathermap.org/data/2.5/weather?q="
    updated_url = base_url + city_name + ",US-" + state + "&appid=" + api_key 
    api_response = requests.get(updated_url)
    weather_data = api_response.json()
    
    main_weather_measures = weather_data['main']
    clouds_data = weather_data['clouds']
    wind_data = weather_data['wind']
    rain_data = weather_data['rain']
    snow_data = weather_data['snow']
    
    
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
    elif weather_phenomena == "rain_1hr":
        rain_1hr_data = rain_data["1hr"]
        return rain_1hr_data
    elif weather_phenomena == "rain_3hr":
        rain_3hr_data = rain_data["3hr"]
        return rain_3hr_data
    elif weather_phenomena == "snow_1hr":
        snow_1hr_data = snow_data["1hr"]
        return snow_1hr_data
    elif weather_phenomena == "snow_3hr":
        snow_3hr_data = snow_data["3hr"]
        return snow_3hr_data
        


#if city and state not in files, while loop until the user provides a correct city or state
#CITY AND STATE DATA FROM https://simplemaps.com/data/us-cities
def city_and_state_verification(city_name, state):
    cities_fh = open("cities.txt", "r")
    cities_fh = cities_fh.read()
    is_city_in_cities_file = None

    states_fh = open("states.txt", "r")
    states_fh = states_fh.read()
    is_state_in_states_file = None

    if city_name in cities_fh:
        is_city_in_cities_file = True
    else:
        is_city_in_cities_file = False

    if state in states_fh:
        is_state_in_states_file = True
    else:
        is_state_in_states_file = False

    if is_city_in_cities_file == False:
        print("The city you have provided is invalid.")

    if is_state_in_states_file == False:
        print("\nThe state you have provided is invalid.")

    if is_city_in_cities_file == True and is_state_in_states_file == True:
        return True
    else:
        return False

#this function will return a polished weather report using all the data from the two city objects and the multiple trend functions   
#this function will be used in the main? after the cities have been created?
def weather_report(first_city, second_city):
    #print out all the attributes of both city objects
    #call all trend functions here and print what they say
    
    