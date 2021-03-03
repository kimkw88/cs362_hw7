# CS362_Winter21
# HW7
# Program: hw7_q2_leap_year.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that calculates whether the year is a leap year or not.
# From homework 1, rewrite the leap year program using the test-first approach.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw7_q2_leap_year.py
###########################################################################

def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True    
    return leap

cont = '1'
while (cont == '1'):
    print("Enter a year: ", end="")
    year = int(input())
    if is_leap(year) == True:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
    print("\nContinue(1) or exit(anykey): ", end="")
    cont = input()
    print()