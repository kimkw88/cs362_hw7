# CS362_Winter21
# HW7
# Program: hw7_q1_fizz_buzz.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that prints the numbers from 1 to 100. But for multiples 
# of three print “Fizz” instead of the number and for the multiples of five 
# print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw7_q1_fizz_buzz.py
###########################################################################

def fizz_buzz():
    arr = list(range(1, 101))
    for i in range(len(arr)):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            arr[i] = "FizzBuzz"
        elif arr[i] % 3 == 0:
            arr[i] = "Fizz"
        elif arr[i] % 5 == 0:
            arr[i] = "Buzz"
        if i % 3 == 0 and i % 5 == 0:
            print()
        print(arr[i], end=" ")
    print()
    return arr

fizz_buzz()
