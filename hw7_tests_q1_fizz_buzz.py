# CS362_Winter21
# HW7
# Program: hw7_tests_q1_fizz_buzz.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw4_tests_q1_volume_cube.py
###########################################################################

import sys
import unittest
import hw7_q1_fizz_buzz as q1

class FizzBuzzTests(unittest.TestCase):

    def test_less_equal1(self):
        self.assertLessEqual(len(q1.fizz_buzz()), 101)
    def test_less_equal2(self):
        self.assertLessEqual(len(q1.fizz_buzz()), 100)

if __name__ == '__main__':
    unittest.main(verbosity=2)