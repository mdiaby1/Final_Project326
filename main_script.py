'''Our app will tell the user about the weather in two cities they choose.
INST-326 - Final Project
John Landrove
Mory Diaby
James Galvagna
Neha Mathur
'''
import json
import requests

#NEED TO MAKE DOCUMENTATION

class City:
    '''Holds information about the city that the user enters
    
    Attributes:
        city_name (str): contains the name of a city 
            in any of the U.S's 50 states and Puerto Rico and Washington D.C.
        state (str): contains the name of a state belonging to the U.S
            Can also contain DC and Puerto Rico
        current_temp (int): The current temperature in the city, in Fahrenheit
        feels_like_temp (int): Human perception of temperature
            in the city, in Fahrenheit
        max_temp (int): Current max temp in Fahrenheit
        min_temp (int): Current min temp in Fahrenheit
        air_pressure (float): Atmospheric pressure in the city in inHg
        humidity (int): Percentage of humidity in air in the city
        cloudiness (int): Percentage of how cloudy the sky in the city is
        wind_speed (int): The speed of wind in the city, in miles per hour
        wind_direction (int): Direction of the wind in meteorological degrees
        visibility (float): Visibility in the city in miles 
        
    '''
    def __init__(self, city_name, state):
        """Intitializes the variables being used to determine the weather
        
        Args:
            city_name (str): contains the name of a city in any of 
                the U.S's 50 states and Puerto Rico and Washington D.C.
            state (str): contains the name of a state belonging to the U.S
                Can also contain DC and Puerto Rico
        
        Side effects:
            Sets attributes city_name, state, current_temp, feels_like_temp,
                max_temp, min_temp, air_pressure, humidity, cloudiness,
                wind_speed, wind_direction, and visibility
        """
        self.city_name = city_name
        self.state = state
        
        self.current_temp = access_api(self.city_name,
                                       self.state, 'current_temp')
        self.feels_like_temp = access_api(self.city_name,
                                          self.state, 'feels_like_temp')
        self.max_temp = access_api(self.city_name,
                                   self.state, 'max_temp')
        self.min_temp = access_api(self.city_name,
                                   self.state, 'min_temp')
        self.air_pressure = access_api(self.city_name,
                                       self.state, 'air_pressure')
        self.humidity = access_api(self.city_name,
                                   self.state, 'humidity')
        self.cloudiness = access_api(self.city_name,
                                     self.state, 'cloudiness')
        self.wind_speed = access_api(self.city_name,
                                     self.state, 'wind_speed')
        self.wind_direction = access_api(self.city_name,
                                         self.state, 'wind_direction')
        self.visibility = access_api(self.city_name,
                                     self.state, 'visibility')

def dangerous_temps_warning(city):
    """This method warns if the feels like temperature is dangerous
        to human health
        THIS IS NOT MEDICAL ADVICE!
        Extreme heat temperatures info comes from the following website:
        https://www.healthline.com/health/
        extreme-temperature-safety#extreme-heat-temperatures
        Extreme cold temperatures info comes from the following website:
        https://www.theladders.com/career-advice/
        this-is-the-point-when-cold-weather-becomes-dangerous#:~:text
        =While%2032%C2%B0F%20is,regulating%20their%20%5Bbody%5D%20temperature.
    
    Args:
        city (City): A City object
    
    Returns:
        dangerous_temps_warning_str (str): Holds a message depending
            on whether the feels_like_temp is dangerous or not
    """
    dangerous_temps_warning_str = ""
    
    if city.feels_like_temp >= 90 or city.feels_like_temp <= 32:
        dangerous_temps_warning_str += ("Please be careful. "
                                        "The feels like temperature ("
                                        + str(city.feels_like_temp) + 
                                        "°F) for "  + str(city.city_name)
                                        + ", " + str(city.state)
                                        + " indicates that "
                                        "the temperature in the city might be "
                                        "dangerous to your health. "
                                        "Please take proper precautions.")
    else:
        dangerous_temps_warning_str += ("No dangerous feels like temperature"
                                        " in " + str(city.city_name)
                                        + ", " + str(city.state) + ".")
        
    return dangerous_temps_warning_str
    
def hottest_city(first_city, second_city):
    """Compares the current temperatures of two cities and returns
        a string which notifies if the first city is hotter, colder, or the
        same temperature as the second city
        
    Args:
       first_city (City): A City object
       second_city (City): A City object
       
    Returns:
        string: notifies if the first city is hotter, colder, or the
        same temperature as the second city
    """
    if first_city.current_temp > second_city.current_temp:
        return (str(first_city.city_name) + ", " + str(first_city.state) +" is"
                + " hotter than " + str(second_city.city_name) + ", " 
                + str(second_city.state) + " by "
                + str(first_city.current_temp-second_city.current_temp) + "°F")
    elif first_city.current_temp < second_city.current_temp:
        return (str(first_city.city_name) + ", " + str(first_city.state) +" is"
                + " colder than " + str(second_city.city_name) + ", " 
                + str(second_city.state) + " by "
                + str(second_city.current_temp-first_city.current_temp) + "°F")
    else:
        return (str(first_city.city_name) + ", " + str(first_city.state)
                + " has the same current temperature ("
                + str(first_city.current_temp) + "°F) as "
                + str(second_city.city_name) + ", " 
                + str(second_city.state) + ".")

def weather_guess(city):
    """Simple guess of the weather conditions in a city
        Pressure info comes from the following website:
        https://www.livescience.com/39315-atmospheric-pressure.html
        Cloud info comes from the following website:
        https://www.thoughtco.com/overcast-sky-definition-3444114#:~:
        text=That%20is%20why%20a%20weather,or%20five%20to%20seven%20oktas.
        Windspeed info comes from the following website:
        https://spectrumlocalnews.com/tx/south-texas-el-paso/weather/
        2021/03/17/is-it-breezy--is-it-windy--the-difference-explained--
    
    Args:
        city (City): A City object
        
    Returns:
        weather_guess_str (str): A guess of the weather conditions in a city
    """
    weather_guess_str = ""
    if city.air_pressure >= 29.3:
        if city.cloudiness <= 60:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a nice, sunny day with a "
                                      "small breeze in " + str(city.city_name)
                                      + ", " + str(city.state) + "!")
            else:
                weather_guess_str += ("It's probably a sunny, but windy day in"
                                      " " + str(city.city_name) + ", "
                                      + str(city.state) + ".")
        elif city.cloudiness > 60 and city.cloudiness < 90:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a mostly cloudy day with"
                                      " a small breeze in "
                                      + str(city.city_name)
                                      + ", " + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, mostly cloudy"
                                      " day in " + str(city.city_name)
                                      + ", " + str(city.state) + ".")
        else:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably an overcast day, with a "
                                      "small breeze, but no rain in "
                                      + str(city.city_name) + ", " 
                                      + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, overcast day, "
                                      "with no rain in "
                                      + str(city.city_name) + ", "
                                      + str(city.state) + ".")           
    else:
        if city.cloudiness <= 60:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a nice, sunny day with a "
                                      "small breeze in " + str(city.city_name) 
                                      + ", " + str(city.state) + "!")
            else:
                weather_guess_str += ("It's probably a sunny, but windy day in"
                                      " " + str(city.city_name)
                                      + ", " + str(city.state) + ".")
        elif city.cloudiness > 60 and city.cloudiness < 90:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a stormy, mostly cloudy"
                                      " day with a small breeze in "
                                      + str(city.city_name) + ", "
                                      + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, mostly cloudy,"
                                      " and stormy day in "
                                      + str(city.city_name)
                                      + ", " + str(city.state) + ".")
        else:
            if city.wind_speed <= 20:
                weather_guess_str += ("It's probably a stormy, overcast"
                                      " day, with a small breeze in "
                                      + str(city.city_name) + ", "
                                      + str(city.state) + ".")
            else:
                weather_guess_str += ("It's probably a windy, overcast,"
                                      " stormy day in " + str(city.city_name)
                                      + ", " + str(city.state) + ".")
            
    return weather_guess_str

def meteorological_degrees_direction(city):
    """Determines cardinal direction from meteorological degrees data
        This info comes from the following website:
        http://snowfence.umn.edu/Components/winddirectionanddegrees.htm 
    
    Args:
        city (City): A City object
        
    Returns:
        wind_cardinal_direction_str (str): stores the wind's cardinal direction
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
    """This method notifies a user if the visibility is low in the city
        Low visibility could make driving very difficult
        This info comes from the following website:
        https://spectrumlocalnews.com/nys/capital-region/
        weather/2021/04/08/as-far-as-the-eye-can-see
    
    Args:
         city (City): A City object
         
    Returns:
        low_visibility_warning_str (str): notifies a user if the visibility 
            in the city is low or is fine
    """
    low_visibility_warning_str = ""
    
    if city.visibility <= 0.25:
        low_visibility_warning_str += ("There is low visibility ("
                                       + str(city.visibility) + " mi) in "
                                       + str(city.city_name) + ", "
                                       + str(city.state)
                                       + ". Please take caution when driving.")
    else:
        low_visibility_warning_str += ("No low visibility in "
                                       + str(city.city_name) + ", "
                                       + str(city.state) + ".\n")
    
    return low_visibility_warning_str

def access_api(city_name, state, weather_phenomena):
    '''Obtains data from OpenWeatherMap's API
    
    Args:
        city_name (str): name of the city the user entered
        state (str): state the city is located in, two letter abbreviation
        weather_phenomena (str): the weather phenomena we want data for
        
    Returns:
        Depending on the weather_phenomena argument passed in, the function
        returns the following:
            current_temp_fahr (int): The current temperature in the city
                in Fahrenheit
            feels_like_temp_fahr (int): Human perception of temperature
                in the city in Fahrenheit
            max_temp_fahr (int): Current max temp in Fahrenheit
            min_temp_fahr (int): Current min temp in Fahrenheit
            air_pressure_inHg (float): Atmospheric pressure in the city in inHg
            humidity_percentage_data (int): Percentage of humidity
                in air in the city
            cloudiness_percentage_data (int): Percentage of how cloudy
                the sky in the city is
            wind_speed_mph (int): The speed of wind in the city,
                in miles per hour
            wind_direction_data (int): Direction of the wind in
                meteorological degrees
            visibility_data_miles (float): Visibility in the city in miles 
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
    
    if weather_phenomena == "current_temp":
        current_temp_fahr = round(
            (main_weather_measures["temp"] - 273.15) * 9/5 + 32)
        return current_temp_fahr
    elif weather_phenomena == "feels_like_temp":
        feels_like_temp_fahr = round(
            (main_weather_measures["feels_like"] - 273.15) * 9/5 + 32)
        return feels_like_temp_fahr
    elif weather_phenomena == "max_temp":
        max_temp_fahr = round(
            (main_weather_measures["temp_max"] - 273.15) * 9/5 + 32)
        return max_temp_fahr
    elif weather_phenomena == "min_temp":
        min_temp_fahr = round(
            (main_weather_measures["temp_min"] - 273.15) * 9/5 + 32)
        return min_temp_fahr
    elif weather_phenomena == "air_pressure":
        air_pressure_inHg = round(
            (main_weather_measures["pressure"]) * 0.03, 2)
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
    """Verifies that the user provides a legitimate city and state 
        in the United States
        CITY AND STATE DATA FROM https://simplemaps.com/data/us-cities
        The .txt files are in the repository; they were created from the data
            obtained from the previously mentioned website
            
        Args:
            city_name (str): name of the city the user entered
            state (str): state the city is located in, two letter abbreviation
            
        Returns:
            True or False: True if both the city and state are found in the
                .txt files, otherwise False is returned
            
        Side effects:
            Prints information to the console
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
    """This method creates a polished weather report using all the data from
        the two City objects and calls the multiple insight/highlight methods
        
    Args:
        first_city (City): A City object
        second_city (City): A City object
        
    Side effects:
        Prints information to the console
    """
    city_list = [first_city, second_city]
    
    for city in city_list:
        print("\nWeather details for "
              + str(city.city_name) + ", " + str(city.state))
        print("Current Temperature: " + str(city.current_temp) + "°F")
        print("Feels Like Temperature: " + str(city.feels_like_temp) + "°F")
        print("Max Temperature: " + str(city.max_temp) + "°F")
        print("Min Temperature: " + str(city.min_temp) + "°F")
        print("Air Pressure: " + str(city.air_pressure) + " inHg")
        print("Humidity: " + str(city.humidity) + "%")
        print("Cloudiness: " + str(city.cloudiness) + "%")
        print("Wind Speed: " + str(city.wind_speed) + " miles per hour")
        print("Wind Direction: " + str(city.wind_direction) + " degrees "
              + str(meteorological_degrees_direction(city)))
        print("Visibility: " + str(city.visibility) + " miles *Max API value "
              "is 10 km, so visibility may be greater than 6.22 miles*\n")
    
    
    print("\n\n******INSIGHTS AND HIGHLIGHTS******")
    print("\n" + hottest_city(first_city, second_city) + "\n")
    for city in city_list:
        print(weather_guess(city))
        print(dangerous_temps_warning(city))
        print(low_visibility_warning(city))
    
if __name__ == "__main__":
    first_city_name = str(input("Please enter the name of the first city you'd"
                                " like to know the weather for: "))
    first_city_state = str(input("Please enter the state in which the first"
                                 " city is located: "))

    while city_and_state_verification(first_city_name, first_city_state) == False:
        first_city_name = str(input("\nPlease enter the name of the first"
                                    " city you'd like to know "
                                    "the weather for: "))
        first_city_state = str(input("Please enter the state in which"
                                     " the first city is located: "))

    second_city_name = str(input("\nPlease enter the name of the second city"
                                 " you'd like to know the weather for: "))
    second_city_state = str(input("Please enter the state in which the"
                                  " second city is located: "))

    while city_and_state_verification(second_city_name, second_city_state) == False:
        second_city_name = str(input("\nPlease enter the name of the second"
                                     " city you'd like to know the"
                                     " weather for: "))
        second_city_state = str(input("Please enter the state in which the"
                                      " second city is located: "))
        
    first_city = City(first_city_name, first_city_state)
    second_city = City(second_city_name, second_city_state)

    weather_report(first_city, second_city)
    