#! /Users/macl2/anaconda/bin/python -tt
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is 
divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

import numpy as np

'''
The first thing I will do is find out how many Sundays fell on the first of 
the month in 1901

I need to check for a leap year
'''

def IsLeapYear(year): # check if a year is a leap year or not
    
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False


def main():
    
    days = np.array(["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]) #Setup an array with the days
    
    DaysInMonth_NonLeapYear = np.array([31,28,31,30,31,30,31,31,30,31,30,31]) #Setup an array with the days for no leap years
    DaysInMonth_LeapYear = np.array([31,29,31,30,31,30,31,31,30,31,30,31]) #Setup an array with the days in leap years
    
    day = 2 # start correctly on a Tuesday
    
    countSun = 0
    
    for year in range(1901,2001):
        decision = IsLeapYear(year)  # check to see if it is a leap year or not
        
        if decision:
            DaysInMonth = DaysInMonth_LeapYear  # assign the correct value of the days in the month
        else:
            DaysInMonth = DaysInMonth_NonLeapYear
            
        i = 1
        
        for month in DaysInMonth: # iterate over the days in the month
            
            if days[day] == "Sun":
                print "Day of first of month", str(i), "in year", str(year), " =", days[day]
                
                countSun +=1
                
            day = (month+day)%7 # calculate the correct day.  This must be done after the first check 
                                # as we've set up the starting point correctly
                
            i+=1
        
    
    print "Number of Sundays =", countSun

    
    return 
  
  
if __name__ == '__main__':
  main()