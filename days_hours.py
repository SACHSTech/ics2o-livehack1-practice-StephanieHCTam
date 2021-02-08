"""
-------------------------------------------------------------------------------
Name:     days_hours.py
Purpose:  This program lets user enter number of hours and converts it to days and hours.

Author:   Tam.S

Created:  08/02/2021
------------------------------------------------------------------------------
"""
# get number of hours
hours = float(input("Enter number of hours: "))

# compute hours to days and hours
days = round(hours // 24)
hours = (hours % 24)

# output results
print(str(days) + " days and " + str(hours) + " hours")