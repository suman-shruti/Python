"""
File: moon_weight.py
--------------------
Add your comments here.
"""

MOON_WEIGHT_MULTIPLIER=0.165
def main():
    #1. Get an input weight from user and store it.
    earth_weight_str=input("Enter an Earth weight:")
    #convert earth weight into float
    earth_weight=float(earth_weight_str)
    #Calculate their weight on moon.
    moon_weight=MOON_WEIGHT_MULTIPLIER * earth_weight
    #print the moon weight to the user.
    print("Weight on the moon is:" + str(moon_weight))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
