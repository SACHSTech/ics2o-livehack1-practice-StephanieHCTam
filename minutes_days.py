"""
-------------------------------------------------------------------------------
Name:     minutes_days.py
Purpose:  This program lets user enter a number of minutes and that will calculate the number of days, hours and minutes that represents.

Author:   Tam.S

Created:  08/02/2021
------------------------------------------------------------------------------
"""

# get number of minutes
minutes = int(input("Enter number of minutes: "))

# compute minutes to days, hours, and minutes
days = int(minutes // 1440)
hours = int(minutes // 60 - (days * 24))
minutes_remaining = int(minutes - (days * 1440) - (hours * 60))

# output results
print(str(days) + " days " + str(hours) + " hours and " + str(minutes_remaining) + " minutes.")