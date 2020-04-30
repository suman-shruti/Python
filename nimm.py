"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    #1. The game starts with a pile of 20 stones between the players
    #2. The two players alternate turns
    #3. On a given turn, a player may take either 1 or 2 stone from the center pile.
    #4. The two players continue until the center pile has run out of stones.
    num_stones = 20
    player = 1
    while num_stones > 0:
        print("There are " + str(num_stones) + " stones left")
        answer = input("Player " + str(player) + " would you like to remove 1 or 2 stones? ")
        answer = int(answer)
        while answer != 1 and answer != 2:
            answer = int(input("Please enter 1 or 2: "))
        else:
            print("")
        num_stones = num_stones - answer
        if player == 1:
            player = 2
        else:
            player = 1
    print("Player " + str(player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
