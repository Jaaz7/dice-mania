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
        tokens = input("\nCharge your account (max 500): ")
        if verify_tokens(tokens):
            print("Tokens accepted.\n")
            time.sleep(1.5)
        else:
            continue
        return int(tokens)


def verify_tokens(num):
    """
    Verify if tokens were correctly submitted
    """
    try:
        if int(num) < 1:
            print(f'Value has to be as least 1, you entered {num}')
            return False
        elif int(num) > 500:
            print(f"Maximum value reached, you entered {num}")
            return False
        else:
            return True
    except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False


def starting_throw():
    """
    Creates the sum of 4 randomized dice and returns the value
    """
    print("Rolling 4 dice on the table...")
    time.sleep(1.5)
    dice = []
    total = 0
    for die in range(4):
        dice.append(random.randint(1, 6))

    """
    Prints the 4 dice art randomized
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
        token_bets = (input('How many tokens would you like to bet for the next play? '))
        if verify_bet(tk, token_bets):
            a, b = verify_bet(tk, token_bets)
            print(f'Bet accepted. You have {b} tokens left.\n')
            time.sleep(1.5)
        else:
            continue
        return [int(token_bets), b]


def verify_bet(tokens, bet):
    """
    Verify if the tokens were correctly submitted
    """
    try:
        if int(bet) > tokens:
            print(f'Bet surpassed allowed amount, maximum {tokens} are permitted, please try again.\n')
            return False
        elif int(bet) < 1:
            print(f"Bet has to be as least 1, you entered {bet}, please try again.\n")
            return False
        else:
            new_tokens = update_tokens(tokens, bet)
            return [True, new_tokens]
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False
    

def update_tokens(tk, bet):
    """
    return new tokens value when the player has betted
    """
    new_tokens = tk - int(bet)
    return new_tokens


def choose_option(mania):
    """
    Ask user which of 3 options to choose: more, less or same.
    """
    while True:
        opt = input(f'Choose your Mania Number play.\nMore than {mania} (press "M"), Less than {mania} (press "L"), Same as {mania} (press "S"): ').lower()
        if opt == 'm':
            print('you have chosen "More".\n')
            break
        elif opt == 'l':
            print('you have chosen "Less".\n')
            break
        elif opt == 's':
            print('you have chosen "Same".\n')
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
        try:
            x = int(input('How many dice? (2-4): '))
            if (x < 2) or (x > 4):
                print('The number has to be between 2 and 4, please try again.\n')
                continue
            if (x >= 2) and (x <= 4):
                print(f'\nRolling {x} dice on the table...')
                time.sleep(1.5)
                break
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.\n")
            continue
    return x

def roll_dice(x):
    """
    Throwing the number of dice chosen
    """
    dice = []
    total = 0
    for die in range(x):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(DICE_ART.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f"Total: {total}")
    return total


def new_play(tokens, bet, play, nr_mania):
    """
    Process a new play with collected data:
    tokens, bet, play option, number of dice and mania number
    """
    new_dice_nr = how_many_dice()
    new_mania_nr = roll_dice(new_dice_nr)
    print(f'voce escolheu {new_dice_nr} dados e o seu numero mania é {new_mania_nr}')
    


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
            '       You then have three guesses towards this number: "more", "less" or "same".',
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
    bet, new_tokens = place_bet(tkns, mania_nr)
    play_option = choose_option(mania_nr)
    new_play(new_tokens, bet, play_option, mania_nr)


main()