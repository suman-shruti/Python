#Constant

INCHES_IN_FOOT=12

def main():
    feet= float(input("Enter the number of feet:"))
    Inches= feet * INCHES_IN_FOOT
    print("The number of feet is " + str(Inches) + ".")


if __name__ == '__main__':
    main()