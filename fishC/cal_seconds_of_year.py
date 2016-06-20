#!/bin/env python
#Give a year ,then return the all seconds of that year

#global DaysPerYear = 365

HoursPerDay = 24
MinutesPerHour = 60
SecondsPerMinute = 60


def is_leap_year(year):
    if ( year % 4 == 0 and year % 100 !=0 ) or year % 400 == 0 :
	DaysPerYear = 366
	return DaysPerYear
    else:
	DaysPerYear = 365
	return DaysPerYear

def cal_seconds_year(year):
    DaysPerYear = is_leap_year(year)
    return SecondsPerMinute * MinutesPerHour * HoursPerDay * DaysPerYear

if __name__ == '__main__':
    temp = input("Please enter a year: ")
    year = int(temp)
    seconds = cal_seconds_year(year)
    print "%d has %d seconds" % (year,seconds)
