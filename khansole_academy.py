"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    result = 1
    while result <= 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = num1 + num2
        print("what is " + str(num1) + "+" + str(num2) + "?")
        answer = int(input("Your answer: "))
        if answer == num3:
            print("Correct! You've gotten " + str(result) + " correct in a row.")
            result += 1
        else:
            print("Incorrect. " + "The expected answer is " + str(num3))
            main()
    else:
        print("Congratulations!  You mastered addition. ")




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
