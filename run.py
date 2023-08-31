import random
from termcolor import colored
import time


DICE_MANIA = {
    1: (
        " /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$",
        "| $$__  $$|_  $$_/ /$$__  $$| $$_____/",
        "| $$  \ $$  | $$  | $$  \__/| $$      ",
        "| $$  | $$  | $$  | $$      | $$$$$   ",
        "| $$  | $$  | $$  | $$      | $$__/   ",
        "| $$  | $$  | $$  | $$    $$| $$      ",
        "| $$$$$$$/ /$$$$$$|  $$$$$$/| $$$$$$$$",
        "|_______/ |______/ \______/ |________/",
    ),
    2: (
        " /$$      /$$  /$$$$$$  /$$   /$$ /$$$$$$  /$$$$$$ ",
        "| $$$    /$$$ /$$__  $$| $$$ | $$|_  $$_/ /$$__  $$",
        "| $$$$  /$$$$| $$  \ $$| $$$$| $$  | $$  | $$  \ $$",
        "| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$  | $$  | $$$$$$$$",
        "| $$  $$$| $$| $$__  $$| $$  $$$$  | $$  | $$__  $$",
        "| $$\  $ | $$| $$  | $$| $$\  $$$  | $$  | $$  | $$",
        "| $$ \/  | $$| $$  | $$| $$ \  $$ /$$$$$$| $$  | $$",
        "|__/     |__/|__/  |__/|__/  \__/|______/|__/  |__/",
    ),
}


DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}


def create_title():
    """
    Creates the dice mania ASCII art
    """
    for line in range(8):
        for tuple in range(1, 3):
            print(colored(DICE_MANIA.get(tuple)[line], "magenta"), end="      ")
        print()


def charging_tokens():
    """
    Ask the player to top up with tokens so the game can start
    """
    while True:
        tokens = int(input("\nCharge your account (max 500): "))
        if verify_tokens(tokens):
            print("Tokens accepted.\n")
            time.sleep(1.5)
            break
    return tokens


def verify_tokens(num):
    """
    
    """
    try:
        if num < 0:
            raise ValueError(f'Negatives values are not allowed, you entered {num}')
        elif num > 500:
            raise ValueError(f"Maximum value reached, you entered {num}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False
    return True


def starting_throw():
    """
    Creates the sum of 4 randomized dice and returns the value
    """
    print("Throwing 4 dice on the table...")
    time.sleep(2)
    dice = []
    total = 0
    for die in range(4):
        dice.append(random.randint(1, 6))

    """
    Prints the 4 dice art randomized in lines 110 and 111
    """
    for line in range(5):
        for die in dice:
            print(DICE_ART.get(die)[line], end="")
        print()

    """
    Prints the sum of the 4 dice
    """
    for die in dice:
        total += die
    print(f"Total: {total}")
    return total