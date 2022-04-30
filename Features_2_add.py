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
from main_script import api_access,Trend,City
# we will develop our code more next week, but for this week we need some sort of unit testing
#API accessor goes here/below and b4 the classes:
"""
 This script consists of possible features that we could add or look into adding for our project

"""



def Temp_in_area(self,city,state):
    self.city = city
    self.state = {state: city}
    
    for key in state:
        if city in state:
            print('Temperature: ',temp)
        if longitude in city > state:
            print('Temperature: ',temp)
            " have the for loop return the weather for each major city within that state"
        # probably wrong needs more implementation and practice


def sevenday_forecast(self,date,):
    """ set a counter for how many days are in a week and in that week, display the forecast for each
    day weather and temperature only. if the day the weather is being checked is within the middle of a different week
    add 7 days to the counter,  """
