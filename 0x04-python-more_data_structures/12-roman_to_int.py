#!/usr/bin/python3
def roman_to_int(roman_string):
  sum = 0
  num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  if not roman_string or type(roman_string) != str:
    return 0
  for roman in reversed(roman_string):
    i = roman_string[roman]
    sum += i if sum < i * 5 else sum -= i
  return sum
