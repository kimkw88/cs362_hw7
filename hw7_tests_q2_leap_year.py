# CS362_Winter21
# HW7
# Program: hw7_tests_q2_leap_year.py
# Author: Kwanghyuk Kim

###########################################################################
# Program Description
# : An application that demonstrates pass and fail conditions for the program.
#
# To compile and run this code, please just enter the command as below: 
#
# python3 hw7_tests_q2_leap_year.py
###########################################################################

import unittest
import hw7_q2_leap_year as q2

class LeapYearTests(unittest.TestCase):

    def test_equal1(self):
        self.assertEqual(q2, True)
    def test_equal2(self):
        self.assertEqual(q2, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)