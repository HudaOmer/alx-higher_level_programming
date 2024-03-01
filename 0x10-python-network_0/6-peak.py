#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted  integers
"""


def find_peak(numbers):
    '''
        Finds the peak in a   list of numbers
    '''
   if numbers:
      numbers.sort(reverse=True)
   return numbers[0]
