"""This script will perform unit tests
INST-326 - Final Project Unit test
John Landrove
Mory Diaby
James Galvagna
Neha Mathur
"""
import unittest
import main_script

class test_main_script(unittest.TestCase):
    """Testing the various methods in main_script using unit tests.
    """
    def test_dangerous_temps_hot(self):
        """Tests to see if dangerous_temps_warning method will warn
        when a city's feels like temperature is dangerously hot 
        
        Side effects:
            Creates a new City object and alters its feels_like_temp attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.feels_like_temp = 100
        warning_str = main_script.dangerous_temps_warning(test_city)
        self.assertEqual(warning_str, "Please be careful. "
                                        "The feels like temperature ("
                                        + str(test_city.feels_like_temp) + 
                                        "°F) for "  + str(test_city.city_name)
                                        + ", " + str(test_city.state)
                                        + " indicates that "
                                        "the temperature in the city might be "
                                        "dangerous to your health. "
                                        "Please take proper precautions.")
        
    def test_dangerous_temps_cold(self):
        """Tests to see if dangerous_temps_warning method will warn
        when a city's feels like temperature is dangerously cold 
        
        Side effects:
            Creates a new City object and alters its feels_like_temp attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.feels_like_temp = 30
        warning_str = main_script.dangerous_temps_warning(test_city)
        self.assertEqual(warning_str, "Please be careful. "
                                        "The feels like temperature ("
                                        + str(test_city.feels_like_temp) + 
                                        "°F) for "  + str(test_city.city_name)
                                        + ", " + str(test_city.state)
                                        + " indicates that "
                                        "the temperature in the city might be "
                                        "dangerous to your health. "
                                        "Please take proper precautions.")
        
    def test_dangerous_temps_not_dangerous(self):
        """Tests to see if dangerous_temps_warning method will notify that
            the feels like temperature doesn't appear to be dangerous
        
        Side effects:
            Creates a new City object and alters its feels_like_temp attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.feels_like_temp = 70
        warning_str = main_script.dangerous_temps_warning(test_city)
        self.assertEqual(warning_str,("No dangerous feels like temperature"
                                        " in " + str(test_city.city_name)
                                        + ", " + str(test_city.state) + "."))
        
    def test_hottest_city_hot(self):
        """Tests to see if hottest_city method will properly notify
            if the first city is hotter than the second city
        
        Side effects:
            Creates two new City objects and alters both their current_temp
                attributes
        """
        first_test_city_hot = main_script.City("College Park", "MD")
        second_test_city_hot = main_script.City("Laurel", "MD")
        first_test_city_hot.current_temp = 100
        second_test_city_hot.current_temp = 30
        hottest_city_str = main_script.hottest_city(first_test_city_hot,
                                                    second_test_city_hot)
        self.assertEqual(hottest_city_str, str(first_test_city_hot.city_name)
                         + ", "
                         + str(first_test_city_hot.state) + " is"
                         + " hotter than "
                         + str(second_test_city_hot.city_name)
                         + ", " + str(second_test_city_hot.state) + " by "
                         + str(first_test_city_hot.current_temp
                               -second_test_city_hot.current_temp)
                         + "°F")
        
    def test_hottest_city_cold(self):
        """Tests to see if hottest_city method will properly notify
            if the first city is colder than the second city
        
        Side effects:
            Creates two new City objects and alters both their current_temp
                attributes
        """
        first_test_city_cold = main_script.City("College Park", "MD")
        second_test_city_cold = main_script.City("Laurel", "MD")
        first_test_city_cold.current_temp = 50
        second_test_city_cold.current_temp = 60
        coldest_city_str = main_script.hottest_city(first_test_city_cold,
                                                    second_test_city_cold)
        self.assertEqual(coldest_city_str,
                         str(first_test_city_cold.city_name)
                         + ", " + str(first_test_city_cold.state) +" is"
                         + " colder than "
                         + str(second_test_city_cold.city_name) + ", "
                         + str(second_test_city_cold.state) + " by "
                         + str(second_test_city_cold.current_temp
                               -first_test_city_cold.current_temp)
                         + "°F")

    def test_hottest_city_same_temp(self):
        """Tests to see if hottest_city method will properly notify
            that the first city and second city both share the same current
            temperature
        
        Side effects:
            Creates two new City objects and alters both their current_temp
                attributes
        """
        first_test_city_same_temp = main_script.City("College Park", "MD")
        second_test_city_same_temp = main_script.City("Laurel", "MD")
        first_test_city_same_temp.current_temp = 50
        second_test_city_same_temp.current_temp = 50
        same_temp_city_str = (
            main_script.hottest_city(first_test_city_same_temp,
                                     second_test_city_same_temp))
        self.assertEqual(same_temp_city_str,
                         str(first_test_city_same_temp.city_name)
                         + ", " + str(first_test_city_same_temp.state)
                         + " has the same current temperature ("
                         + str(first_test_city_same_temp.current_temp)
                         + "°F) as "
                         + str(second_test_city_same_temp.city_name)
                         + ", " + str(second_test_city_same_temp.state) 
                         + ".")
        
    def test_meteorological_degrees_direction_N(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 350
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "N")
    
    def test_meteorological_degrees_direction_NNE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 20
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "NNE")
    
    def test_meteorological_degrees_direction_NE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 50
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "NE")
    
    def test_meteorological_degrees_direction_ENE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 70
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "ENE")
    
    def test_meteorological_degrees_direction_E(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 100
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "E")
        
    def test_meteorological_degrees_direction_ESE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 110
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "ESE")
        
    def test_meteorological_degrees_direction_SE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 130
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "SE")
            
    def test_meteorological_degrees_direction_SSE(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 168.75
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "SSE")
    
    def test_meteorological_degrees_direction_S(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 168.76
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "S")
        
    def test_meteorological_degrees_direction_SSW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 200
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "SSW")
        
    def test_meteorological_degrees_direction_SW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 220
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "SW")
        
    def test_meteorological_degrees_direction_WSW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 250.5
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "WSW")
        
    def test_meteorological_degrees_direction_W(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 260
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "W")
        
    def test_meteorological_degrees_direction_WNW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 300
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "WNW")
        
    def test_meteorological_degrees_direction_NW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 310
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "NW")
        
    def test_meteorological_degrees_direction_NNW(self):
        """Tests to see if meteorological_degrees_direction method returns the
            correct cardinal direction of the wind
        
        Side effects:
            Creates a new City object and alters its wind_direction attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.wind_direction = 330
        direction_str = main_script.meteorological_degrees_direction(test_city)
        self.assertEqual(direction_str, "NNW")
        
    def test_low_visibility_warning_true(self):
        """Tests to see if low_visibility_warning method will warn
        when a city's visibility is very low
        
        Side effects:
            Creates a new City object and alters its visibility attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.visibility = 0.01
        warning_str = main_script.low_visibility_warning(test_city)
        self.assertEqual(warning_str, "There is low visibility ("
                                       + str(test_city.visibility) + " mi) in "
                                       + str(test_city.city_name) + ", "
                                       + str(test_city.state)
                                       + ". Please take caution when driving.")
        
    def test_low_visibility_warning_false(self):
        """Tests to see if low_visibility_warning method will notify
        that the visibility in a city appears to be normal
        
        Side effects:
            Creates a new City object and alters its visibility attribute
        """
        test_city = main_script.City("College Park", "MD")
        test_city.visibility = 10
        warning_str = main_script.low_visibility_warning(test_city)
        self.assertEqual(warning_str, "No low visibility in "
                                       + str(test_city.city_name) + ", "
                                       + str(test_city.state) + ".\n")
        
    def test_access_api(self):
        """Tests to see if access_api method works properly by seeing if
        it returns the current temperature of a city.
        """
        current_temp_test = main_script.access_api("College Park"
                                                   ,"MD"
                                                   ,"current_temp")
        self.assertIs(type(current_temp_test), int)
    
    def test_city_and_state_verification_both_valid(self):
        """Tests to see if True is returned by city_and_state_verification
        method when a valid city and valid state is entered
        """
        test_city_name = "College Park"
        test_state = "MD"
        method_output = main_script.city_and_state_verification(test_city_name,
                                                                test_state)
        self.assertTrue(method_output)
     
    def test_city_and_state_verification_city_false(self):
        """Tests to see if False is returned by city_and_state_verification
        method when an invalid city and valid state is entered
        """
        test_city_name = "Krypton"
        test_state = "MD"
        method_output = main_script.city_and_state_verification(test_city_name,
                                                                test_state)
        self.assertFalse(method_output)
        
    def test_city_and_state_verification_state_false(self):
        """Tests to see if False is returned by city_and_state_verification
        method when a valid city and invalid state is entered
        """
        test_city_name = "College Park"
        test_state = "AB"
        method_output = main_script.city_and_state_verification(test_city_name,
                                                                test_state)
        self.assertFalse(method_output)
        
    def test_city_and_state_verification_city_both_false(self):
        """Tests to see if False is returned by city_and_state_verification
        method when an invalid city and invalid state is entered
        """
        test_city_name = "Krypton"
        test_state = "AB"
        method_output = main_script.city_and_state_verification(test_city_name,
                                                                test_state)
        self.assertFalse(method_output)      
    
if __name__ == "__main__":
    unittest.main()
    