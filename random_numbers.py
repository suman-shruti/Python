"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random
MIN_RANDOM=0
MAX_RANDOM=100
NUM_RANDOM=10

def main():
    #Generate 10 random number between 0 and 100
    for i in range(0,10):
        NUM_RANDOM=random.randint(MIN_RANDOM,MAX_RANDOM)
        print(NUM_RANDOM)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
