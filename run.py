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
    Verify if tokens were correctly submitted
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


def place_bet(tk, mn):
    """
    Collect the bet from user and return it
    """
    print(f'\nYou have {tk} tokens and your Mania Number is {mn}.\n')
    while True:
        token_bets = int(input('How many tokens would you like to bet for the next play? '))
        if verify_bet(tk, token_bets):
            print('Bet accepted.\n')
            time.sleep(2)
            break
    token_bets


def verify_bet(tokens, bet):
    """
    Verify if the tokens were correctly submitted
    """
    try:
        if bet > tokens:
            raise ValueError(f'Bet surpassed allowed amount, maximum {tokens} are permitted')
        elif bet < 0:
            raise ValueError(f"Negative numbers are not allowed, you entered {bet}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False
    return True


def choose_option():
    """
    Ask user which of 3 options to choose: more, less or same.
    """
    while True:
        opt = input('Enter what happens to your Mania Number on the next play.\nMore (m), Less(l), Same(s): ').lower()
        if opt == 'm':
            print('you have chosen More.\n')
            break
        elif opt == 'l':
            print('you have chosen Less.\n')
            break
        elif opt == 's':
            print('you have chosen Same.\n')
            break
        else:
            print(f'{opt} is not valid, please try again.\n')
            continue
    return opt


def how_many_dice():
    """
    Ask user how many dice will be played in the next play
    """
    while True:
        d = (input('How many dice will you play with? (2-4): '))
        if (int(d) > 2) and (int(d) < 4):
            print(f'Rolling {int(d)} dice...')
            break
        elif (int(d) < 2) or (int(d) > 4):
            print('The number has to be between 2 and 4, please try again.\n')
            continue
        else:
            print(f'{d} is not valid, try again.')
            continue

    """
    Throwing the number of dice chosen in line 184
    """
    dice = []
    total = 0
    for die in range(d):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(DICE_ART.get(die)[line], end="")
        print()


def new_play():
    """
    Process a new play with collected data: tokens, bet, number of dice and option
    """
    print(f"You're ready to play!\nTokens: {tokens}\n")


def main():
    """
    Prints rules of the game
    Runs the functions of the program
    """
    print("\n")
    create_title()
    print(
        colored(
            "\n\nWelcome! Bet your tokens to guess the tendency of the next play.\nAre you ready?\n",
            "cyan",
        )
    )

    print("Rules: To win, you need to guess the sum of the next dice play.")
    print("       --------------------------------------------------------")
    print("       First, charge your balance with tokens.")
    print(colored("       Place your bet, only whole tokens are accepted.", "black"))
    print(
        "       You roll 4 dice to get a starting Mania Number, it will be the total sum of the 4 dice."
    )
    print(
        colored(
            '       You then have three guess options towards this number: "more", "less" or "same".',
            "black",
        )
    )
    print('       If you bet "more", "less" or "same" and win, you win your bet.')
    print(colored('       If you bet "same" with 3 or 4 dice and win, your bet is doubled up.', "black"))
    print("       Choose the number of dice you want to play from 2 to 4. A single die cannot be played.")
    print(colored("       You can always recharge, continue or quit.", "black"))
    print("       You lose when your balance reaches 0.")

    tkns = charging_tokens()
    mania_nr = starting_throw()
    bet = place_bet(tkns, mania_nr)
    option = choose_option()
    how_many_dice()


main()