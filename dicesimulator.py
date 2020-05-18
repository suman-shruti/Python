import random

NUMBER_DICE=6

def dice_role():
    die1=random.randint(1, NUMBER_DICE)
    die2=random.randint(1, NUMBER_DICE)
    total= die1 + die2
    print("The total number of die roll is " + str(total) + ".")


def main():
    dice_num=10
    print("die1 in main is started as " + str(dice_num))
    dice_role()
    dice_role()
    dice_role()
    print("die1 in main() is " + str(dice_num))

if __name__ == '__main__':
    main()