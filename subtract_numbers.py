"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    print("This program subtracts one number from another.")
    a=float(input("Enter first number: "));
    b=float(input("Enter second number: "));
    Result=(a-b);
    print("The result is "+str(Result))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
