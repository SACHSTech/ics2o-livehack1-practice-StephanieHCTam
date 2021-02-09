"""
-------------------------------------------------------------------------------
Name:     windchill.py
Purpose:  This program lets gets the temperature (celsius) and wind speed (km/h) then computes and outputs the windchill factor.

Author:   Tam.S

Created:  08/02/2021
------------------------------------------------------------------------------
"""

# get information
temperature = float(input("Enter the temperature in celsius: "))
wind_speed = float(input("Enter the wind speed in km/h: "))

# compute windchill factor
wind_chill = 13.12 + (0.6215 * temperature) - (11.37 * wind_speed ** 0.16) + (0.3965 * temperature * wind_speed ** 0.16)

# output result
print("The wind chill is", str(wind_chill), "degrees celsius.")