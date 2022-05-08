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
        self.city_name = city_name
        self.state = state
        
        self.current_temp = access_api(self.city_name, self.state, 'current_temp')
        self.feels_like_temp = access_api(self.city_name, self.state, 'feels_like_temp')
        self.max_temp = access_api(self.city_name, self.state, 'max_temp')
        self.min_temp = access_api(self.city_name, self.state, 'min_temp')
        self.air_pressure = access_api(self.city_name, self.state, 'air_pressure')
        self.humidity = access_api(self.city_name, self.state, 'humidity')
        self.cloudiness = access_api(self.city_name, self.state, 'cloudiness')
        self.wind_speed = access_api(self.city_name, self.state, 'wind_speed')
        self.wind_direction = access_api(self.city_name, self.state, 'wind_direction')
        self.visibility = access_api(self.city_name, self.state, 'visibility')

#PUT THE NEW TREND FUNCTIONS HERE

def hottest_city(first_city, second_city):
    if first_city.current_temp > second_city.current_temp:
        return (str(first_city.city_name) + ", " + str(first_city.state) +" is"
                + " hotter than " + str(second_city.city_name) + ", " 
                + str(second_city.state) + " by " + str(first_city.current_temp-second_city.current_temp) + "°F")
    elif first_city.current_temp < second_city.current_temp:
        return (str(first_city.city_name) + ", " + str(first_city.state) +" is"
                + " colder than " + str(second_city.city_name) + ", " 
                + str(second_city.state) + " by " + str(second_city.current_temp-first_city.current_temp) + "°F")
    else:
        return (str(first_city.city_name) + ", " + str(first_city.state)
                + " has the same current temperature (" + str(first_city.current_temp) + "°F) as " + str(second_city.city_name) + ", " 
                + str(second_city.state) + ".")
        
def bad_weather_guess(city):
    if city.air_pressure
    

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
    visibility_data = weather_data['visibility']
    #cannot get rain or snow data: According to OpenWeatherMap, 'If you do not see some of the parameters in your API response it means that these weather phenomena 
    #are just not happened for the time of measurement for the city or location chosen. Only really measured or calculated data is 
    #displayed in API response.'
    
    if weather_phenomena == "current_temp":
        current_temp_fahr = round((main_weather_measures["temp"] - 273.15) * 9/5 + 32)
        return current_temp_fahr
    elif weather_phenomena == "feels_like_temp":
        feels_like_temp_fahr = round((main_weather_measures["feels_like"] - 273.15) * 9/5 + 32)
        return feels_like_temp_fahr
    elif weather_phenomena == "max_temp":
        max_temp_fahr = round((main_weather_measures["temp_max"] - 273.15) * 9/5 + 32)
        return max_temp_fahr
    elif weather_phenomena == "min_temp":
        min_temp_fahr = round((main_weather_measures["temp_min"] - 273.15) * 9/5 + 32)
        return min_temp_fahr
    elif weather_phenomena == "air_pressure":
        air_pressure_inHg = round((main_weather_measures["pressure"]) * 0.03, 2)
        return air_pressure_inHg
    elif weather_phenomena == "humidity":
        humidity_percentage_data = main_weather_measures["humidity"]
        return humidity_percentage_data
    elif weather_phenomena == "cloudiness":
        cloudiness_percentage_data = clouds_data["all"]
        return cloudiness_percentage_data
    elif weather_phenomena == "wind_speed":
        wind_speed_mph = round(wind_data["speed"] * 2.237)
        return wind_speed_mph
    elif weather_phenomena == "wind_direction":
        wind_direction_data = wind_data["deg"]
        return wind_direction_data
    elif weather_phenomena == "visibility":
        visibility_data_miles = round(visibility_data / 1609, 2)
        return visibility_data_miles
        
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
        print("\nThe city you have provided is invalid.")

    if is_state_in_states_file == False:
        print("\nThe state you have provided is invalid.")

    if is_city_in_cities_file == True and is_state_in_states_file == True:
        return True
    else:
        return False

#this function will return a polished weather report using all the data from the two city objects and the multiple trend functions   
def weather_report(first_city, second_city):
    city_list = [first_city, second_city]
    
    for city in city_list:
        print("\nWeather details for " + str(city.city_name) + ", " + str(city.state))
        print("Current Temperature: " + str(city.current_temp) + "°F")
        print("Feels Like Temperature: " + str(city.feels_like_temp) + "°F")
        print("Max Temperature: " + str(city.max_temp) + "°F")
        print("Min Temperature: " + str(city.min_temp) + "°F")
        print("Air Pressure: " + str(city.air_pressure) + " inHg")
        print("Humidity: " + str(city.humidity) + "%")
        print("Cloudiness: " + str(city.cloudiness) + "%")
        print("Wind Speed: " + str(city.wind_speed) + " miles per hour")
        print("Wind Direction: " + str(city.wind_direction) + " degrees")
        print("Visibility: " + str(city.visibility) + " miles *Max API value "
              "is 10 km, so visibility may be greater than 6.22 miles*\n")
    
    print("*HIGHLIGHTS*")
    print(hottest_city(first_city, second_city))
    #call all trend functions here and print what they say
    
if __name__ == "__main__":
    first_city_name = str(input("Please enter the name of the first city you'd like to know the weather for: "))
    first_city_state = str(input("Please enter the state in which the first city is located: "))

    while city_and_state_verification(first_city_name, first_city_state) == False:
        first_city_name = str(input("\nPlease enter the name of the first city you'd like to know the weather for: "))
        first_city_state = str(input("Please enter the state in which the first city is located: "))

    second_city_name = str(input("\nPlease enter the name of the second city you'd like to know the weather for: "))
    second_city_state = str(input("Please enter the state in which the second city is located: "))

    while city_and_state_verification(second_city_name, second_city_state) == False:
        second_city_name = str(input("\nPlease enter the name of the second city you'd like to know the weather for: "))
        second_city_state = str(input("Please enter the state in which the second city is located: "))
        
    first_city = City(first_city_name, first_city_state)
    second_city = City(second_city_name, second_city_state)

    weather_report(first_city, second_city)
    