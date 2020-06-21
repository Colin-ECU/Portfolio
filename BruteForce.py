#!/usr/bin/python3

# This script is meant to be able to generate numbers from the Python Random Library (randint)
# There is the initial import of the library followed by a limiting range of up to 100 iterations.
# The number of iterations may be redundant due to the specified maximum of 100. I left this in case I wanted to try a Max range.
# The actual PIN I am trying to break is defined as: 77.
# The while loop is meant to run random interations (up to 100) until it matches the PIN.
# IF the Random generator matches the PIN, it is meant break the loop and print, " The PIN 77 has been cracked!"
# Unfortunately, I was unable to make this work prior to submission of Assignment.

import random

number = random.randint(1, 100)

number_of_iterations = 0

PIN = '77'

while number != PIN:
    PIN = input()
    PIN = int(PIN)

    number = number + 1

    if number == PIN:
        break

print('The PIN ' + PIN + ' has been cracked!')
