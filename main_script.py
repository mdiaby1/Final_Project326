'''Our app will tell the user about the weather of a city they have selected
'''
import json
import requests

#NEED TO CHECK CODE DOCSTRINGS, 80 COLUMNS
#NEED TO INCLUDE UNIT TESTS (creating a city object, testing each function like city_and_state_validation)
#NEED TO MAKE DOCUMENTATION

class City:
    '''Holds information about the city that the user enters
    Attributes - City that user wants the weather information of 
    '''
    def __init__(self, city_name, state):
        """
        Intitializes the variables being used to determine the weather
    Args:
        city_name(str): a string that contains the name of a city in any of the U.S' 50 states
        state(str): a string that contains the name of a state belonging to the U.S
        """
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

def dangerous_temps_warning(city):
    """ Informs the user about the feels like temperature and warns them about anything that could affect their health(mainly
    for people with allergies) based on their city or any city
    #THIS IS NOT MEDICAL ADVICE!
    #EXTREME HEAT TEMPERATURES INFO COMES FROM THE FOLLOWING WEBSITE: https://www.healthline.com/health/extreme-temperature-safety#extreme-heat-temperatures
    #EXTREME COLD TEMPERATURES INFO COMES FROM THE FOLLOWING WEBSITE: https://www.theladders.com/career-advice/this-is-the-point-when-cold-weather-becomes-dangerous#:~:text=While%2032%C2%B0F%20is,regulating%20their%20%5Bbody%5D%20temperature.
    Args:
        city(str): a string that contains the name of a city in any of the U.S' 50 states
    Returns:
         dangerous_temps_warning_str(str): information that provides a warning to the user based on the feels like temp
     """
    dangerous_temps_warning_str = ""
    
    if city.feels_like_temp >= 90 or city.feels_like_temp <= 32:
        dangerous_temps_warning_str += ("Please be careful. The feels like temperature (" + str(city.feels_like_temp) + "°F) for "  + str(city.city_name) + ", " + str(city.state) + " indicates that "
                                        "the temperature in the city might be dangerous to your health. Please take proper precautions.")
    else:
        dangerous_temps_warning_str += ("No dangerous feels like temperature in " + str(city.city_name) + ", " + str(city.state) + ".")
        
    return dangerous_temps_warning_str
    
def hottest_city(first_city, second_city):
    """ Compares the temperatures between two cities and returns a string to determine which one is hotter,cooler or the same
    Args:
       first_city(str): first U.S city being compared
       second_city(str): second U.S city being compared
    Returns:
        returns a string that determines which one is hotter,cooler or the same
        """
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

def weather_guess(city):
    """ Simple guess of the weather conditions in a city
        PRESSURE INFO COMES FROM THE FOLLOWING WEBSITE: https://www.livescience.com/39315-atmospheric-pressure.html
        CLOUD INFO COMES FROM THE FOLLOWING WEBSITE: https://www.thoughtco.com/overcast-sky-definition-3444114#:~:text=That%20is%20why%20a%20weather,or%20five%20to%20seven%20oktas.
        WINDSPEED INFO COMES FROM THE FOLLOWING WEBSITE: https://spectrumlocalnews.com/tx/south-texas-el-paso/weather/2021/03/17/is-it-breezy--is-it-windy--the-difference-explained--
    Args:
        city(str): a string that contains the name of a city in any of the U.S' 50 states
    Returns:
        weather_guess_str(str):  a guess of the weather conditions in a city
     """
    weather_guess_str = ""
    if city.air_pressure >= 29.3:
        if city.cloudiness <= 60:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a nice, sunny day with a small breeze in " + str(city.city_name) + ", " + str(city.state) + "!")
            else:
                weather_guess_str += ("It's probably a sunny, but windy day in " + str(city.city_name) + ", " + str(city.state) + ".")
        elif city.cloudiness > 60 and city.cloudiness < 90:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a mostly cloudy day with a small breeze in " + str(city.city_name) + ", " + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, mostly cloudy day in " + str(city.city_name) + ", " + str(city.state) + ".")
        else:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably an overcast day, with a small breeze, but no rain in " + str(city.city_name) + ", " + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, overcast day, with no rain in " + str(city.city_name) + ", " + str(city.state) + ".")           
    else:
        if city.cloudiness <= 60:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a nice, sunny day with a small breeze in " + str(city.city_name) + ", " + str(city.state) + "!")
            else:
                weather_guess_str += ("It's probably a sunny, but windy day in " + str(city.city_name) + ", " + str(city.state) + ".")
        elif city.cloudiness > 60 and city.cloudiness < 90:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a stormy, mostly cloudy day with a small breeze in " + str(city.city_name) + ", " + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, mostly cloudy, and stormy day in " + str(city.city_name) + ", " + str(city.state) + ".")
        else:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a stormy, overcast day, with a small breeze in " + str(city.city_name) + ", " + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, overcast, stormy day in " + str(city.city_name) + ", " + str(city.state) + ".")
            
    return weather_guess_str

def meteorological_degrees_direction(city):
    """Determines cardinal direction from meteorological degrees data
    THIS INFO COMES FROM THE FOLLOWING WEBSITE: http://snowfence.umn.edu/Components/winddirectionanddegrees.htm 
    Args:
        city(str): a string that contains the name of a city in any of the U.S' 50 states
    Returns:
        wind_cardinal_direction_str(str): a string that returns the wind cardinal direction
    """
    wind_cardinal_direction_str = ""
    
    if city.wind_direction >= 348.75 or city.wind_direction <= 11.25:
        wind_cardinal_direction_str += "N"
    elif city.wind_direction > 11.25 and city.wind_direction <= 33.75:
        wind_cardinal_direction_str += "NNE"
    elif city.wind_direction > 33.75 and city.wind_direction <= 56.25:
        wind_cardinal_direction_str += "NE"
    elif city.wind_direction > 56.25 and city.wind_direction <= 78.75:
        wind_cardinal_direction_str += "ENE"
    elif city.wind_direction > 78.75 and city.wind_direction <= 101.25:
        wind_cardinal_direction_str += "E"
    elif city.wind_direction > 101.25 and city.wind_direction <= 123.75:
        wind_cardinal_direction_str += "ESE"       
    elif city.wind_direction > 123.75 and city.wind_direction <= 146.25:
        wind_cardinal_direction_str += "SE"    
    elif city.wind_direction > 146.25 and city.wind_direction <= 168.75:
        wind_cardinal_direction_str += "SSE" 
    elif city.wind_direction > 168.75 and city.wind_direction <= 191.25:
        wind_cardinal_direction_str += "S" 
    elif city.wind_direction > 191.25 and city.wind_direction <= 213.75:
        wind_cardinal_direction_str += "SSW" 
    elif city.wind_direction > 213.75 and city.wind_direction <= 236.25:
        wind_cardinal_direction_str += "SW" 
    elif city.wind_direction > 236.25 and city.wind_direction <= 258.75:
        wind_cardinal_direction_str += "WSW" 
    elif city.wind_direction > 258.75 and city.wind_direction <= 281.25:
        wind_cardinal_direction_str += "W" 
    elif city.wind_direction > 281.25 and city.wind_direction <= 303.75:
        wind_cardinal_direction_str += "WNW" 
    elif city.wind_direction > 303.75 and city.wind_direction <= 326.25:
        wind_cardinal_direction_str += "NW"
    elif city.wind_direction > 326.25 and city.wind_direction < 348.75:
        wind_cardinal_direction_str += "NNW"    
    
    return wind_cardinal_direction_str

def low_visibility_warning(city):
    """
    This method notifies a user if the visibility is low in the city they chose
    Low visibility could make driving very difficult
    THIS INFO COMES FROM THE FOLLOWING WEBSITE: https://spectrumlocalnews.com/nys/capital-region/weather/2021/04/08/as-far-as-the-eye-can-see
    Args:
         city(str): a string that contains the name of a city in any of the U.S' 50 states
    Returns:
        low_visibility_warning_str(str): a string that notifies a user if the visibility is low in the city they chose
    """
    low_visibility_warning_str = ""
    
    if city.visibility <= 0.25:
        low_visibility_warning_str += ("There is low visibility (" + str(city.visibility) + " mi) in " + str(city.city_name) + ", " + str(city.state)
                                       + ". Please take caution when driving.")
    else:
        low_visibility_warning_str += ("No low visibility in " + str(city.city_name) + ", " + str(city.state) + ".\n")
    
    return low_visibility_warning_str

def access_api(city_name, state, weather_phenomena):
    '''works with the openweather api
    Args:
        The name of the city entered,state the city resides in and the weather associated with that city
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
        
def city_and_state_verification(city_name, state):
    """ Verification or verifies that the user provides a city that is in the correcct state or if that city/state exists
        if city and state not in files, while loop until the user provides a correct city or state
        CITY AND STATE DATA FROM https://simplemaps.com/data/us-cities
        The .txt files are in the repository; they were created from the data obtained from the previously mentioned website
        Args:
            city_name(str): a string that contains the name of a city in any of the U.S' 50 states
            state(str): a string that contains the name of a state belonging to the U.S
        Returns:
            a string that tells the user the city/state they've provided is invalid

    """
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

def weather_report(first_city, second_city):
    """this method will return a polished weather report using all the data from the two city objects and the multiple insight/highlight functions   
        Args:
       first_city(str): first U.S city being inputted
       second_city(str): second U.S city being inputted
    Returns:
        returns a polished weather report using all the data from the two city objects 
    """
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
        print("Wind Direction: " + str(city.wind_direction) + " degrees " + str(meteorological_degrees_direction(city)))
        print("Visibility: " + str(city.visibility) + " miles *Max API value "
              "is 10 km, so visibility may be greater than 6.22 miles*\n")
    
    
    print("\n\n******INSIGHTS AND HIGHLIGHTS******")
    print("\n" + hottest_city(first_city, second_city) + "\n")
    for city in city_list:
        print(weather_guess(city))
        print(dangerous_temps_warning(city))
        print(low_visibility_warning(city))
    
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
    