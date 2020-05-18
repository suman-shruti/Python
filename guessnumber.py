import random

GUESS_NUMBER=99

def main():
    guess=random.randint(0, GUESS_NUMBER)
    num=int(input("Enter a guess: "))
    while num != guess:
        if num<guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        num = int(input("Enter a guess: "))
    print("Congrats! The number was: " + str(guess))



if __name__ == '__main__':
    main()