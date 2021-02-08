"""
-------------------------------------------------------------------------------
Name:     f_to_c.py
Purpose:  This program lets user enter a Fahrenheit degree and convert to celsius degree.

Author:   Tam.S

Created:  08/02/2021
------------------------------------------------------------------------------
"""

# get Fahrenheit degree
fahrenheit = float(input("Enter degree measure in Fahrenheit: "))

# compute Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

# output result
print("Celsius degree measure is: " + str(celsius))
