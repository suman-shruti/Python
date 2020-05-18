import random

NUMBER_SIDES=40
def main():
    die1= random.randint(1,NUMBER_SIDES)
    die2=random.randint(1,NUMBER_SIDES)
    total =die1+die2

    print("Dice have " + str(NUMBER_SIDES) + " each.")
    print("First die: " + str(die1))
    print("Second die: " + str(die2))
    print("The total number of die " + str(total))


if __name__ == '__main__':
    main()