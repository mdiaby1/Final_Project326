"""
Before we start coding we need to get access to an OpenWeather API key, once we get that key we will be able to access
OpenWeathers API and utilize it for our data.
 Here's the link:https://openweathermap.org/
 I'm not sure if we ALL need it because the free version only has a limited amount of calls, I will make an account 
 and go through the  steps neccessary to call the API

 This is our API key : 0cc0e4d9235938991e58db115667109b
 Login info for the APU website:
 `  user:practicehw237@gmail.com
    pass:terrapinstrong123

"""
from importlib.machinery import WindowsRegistryFinder
import requests # this import helps us request the data from the url I provided
import json # this helps us with the OPEN Weather API json FILES that have the name of every city
from main_script import Trend,City, weather_report, access_api
# we will develop our code more next week, but for this week we need some sort of unit testing
#API accessor goes here/below and b4 the classes:
"""
 This script consists of possible features that we could add or look into adding for our project

"""


def precipitation_trend(first_city,second_city):
    """ set a counter for how many days are in a week and in that week, display the forecast for each
    day weather and temperature only. if the day the weather is being checked is within the middle of a different week
    add 7 days to the counter,  """
    first_city_rainfall_3hr = first_city.rainfall_3hr
    second_city_rainfall_3hr = second_city.rainfall_3hr
    first_city_rainfall_1hr = first_city.rainfall_1hr
    second_city_rainfall_1hr = second_city.rainfall_1hr


# need to think about this one
def snowfall_trend(first_city,second_city):
    first_city_snowfall_3hr = first_city.snowfall_3hr
    second_city_snowfall_3hr = second_city.snowfall_3hr
    first_city_snowfall_1hr = first_city.snowfall_1hr
    second_city_snowfall_1hr = second_city.snowfall_1hr



""" min temp of a certain area """
def min_temp(city_name,state):
    city_name = city_name
    state = state
    heat2  = access_api(weather_phenomena= "min_temp")
    return heat2
""" feels like temp of a certain area """
def feels_like_temp(city_name,state):
    city_name = city_name
    state = state
    feels  = access_api(weather_phenomena= "feels_like")
    return feels

""" what area is hotter"""
def whos_hotter(first_city,first_state, second_city,second_state):
    first_city = first_city
    second_city = second_city
    first_state = first_state
    second_state = second_state
    first_city_heat = access_api(first_city,first_state,weather_phenomena="temp")
    second_city_heat = access_api(second_city,second_state,weather_phenomena="temp")

    if first_city_heat > second_city_heat:
         print(f'{first_city,first_state} is warmer than {second_city,second_state} is cooler')
    elif first_city_heat < second_city_heat:
        print(f'{second_city,second_state} is warmer than {first_city,first_state} is cooler')
    else:
        print(f'{first_city,first_state} are the same tempereature {second_city,second_state}')










