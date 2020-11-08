"""
Name:  IsFactor.py
Author:  Lee Brown
Created:  10/26/2020
Last Updated:  11/03/2020
Purpose:  Check to see if a number is a factor of another number.
Description:  This will take in a number and its potential factor, divide them,
            and check for a decimal point to see if the given number is a
            factor of the other number.
"""


def is_factor(base, potential_factor):
    try:
        divide = str(float(base)/float(potential_factor))
        if divide[len(divide)-1] == '0' and divide[len(divide)-2] == '.':
            return True
        else:
            return False
    except:
        #if the division is not possible, one piece of input is not a number
        raise Exception("Incorrect input.  Input must be in integer or float form.")
