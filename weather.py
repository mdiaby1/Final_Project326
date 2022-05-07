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
import requests # this import helps us request the data from the url I provided
import json # this helps us with the OPEN Weather API json FILES that have the name of every city

# we will develop our code more next week, but for this week we need some sort of unit testing
#API accessor goes here/below and b4 the classes:





class City: "Used to hold information about the city the user asked for"





class Trend:
    """Used to perform data analysis on weather data (i.e., differences in certain aspects of the weather between two cities, or over a certain period of time)"""  
    def how_windy(city_name,state):
        '''Tells how windy certain area is'''
        city_name = city_name
        state = state
        windy = access_api(weather_phenomena = "wind_direction"), access_api(weather_phenomena = "wind_speed")
        return windy
    
    def max_temp(city_name,state):
        '''max temp of certain area'''
        city_name = city_name
        state = state
        heat = access_api(weather_phenomena = "max_temp")
        return heat
    
    
    
    
    
    