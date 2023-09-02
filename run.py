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
    Creates the dice mania ASCII art.
    """
    for line in range(8):
        for tuple in range(1, 3):
            print(colored(DICE_MANIA.get(tuple)[line], "red"), end="  ")
        print()


def charging_tokens():
    """
    Asks the player to charge the account with tokens.
    """
    while True:
        tokens = input("\n Charge your account (max 500): ")
        if verify_tokens(tokens):
            print(" Tokens accepted.\n")
            time.sleep(1.5)
        else:
            continue
        return int(tokens)


def verify_tokens(num):
    """
    Verifies if the tokens were correctly submitted.
    """
    try:
        if int(num) < 1:
            print(f' Value has to be as `least 1, you entered {num}')
            return False
        elif int(num) > 500:
            print(f" Maximum value reached, you entered {num}")
            return False
        else:
            return True
    except ValueError as e:
            print(f" Invalid data: {e}. Please try again.")
            return False    


def place_bet(tokens, mania_nr):
    """
    Collects the bet from the player.
    """
    print(f' You have {tokens} tokens and your Mania Number is {mania_nr}.\n')
    while True:
        token_bets = (input(' How many tokens would you like to bet? '))
        if verify_bet(tokens, token_bets):
            a, new_tokens = verify_bet(tokens, token_bets)
            print(f' Bet accepted. You have {new_tokens} tokens left.\n')
            time.sleep(1.5)
        else:
            continue
        return [int(token_bets), new_tokens]


def verify_bet(tokens, bet):
    """
    Verifies if the bet was correctly submitted.
    """
    try:
        if int(bet) > tokens:
            print(f' Bet surpassed allowed amount, maximum {tokens} are permitted, please try again.\n')
            return False
        elif int(bet) < 1:
            print(f" Bet has to be as least 1, you entered {bet}, please try again.\n")
            return False
        else:
            new_tokens = update_tokens(tokens, bet)
            return [True, new_tokens]
    except ValueError as e:
        print(f" Invalid data: {e}. Please try again.\n")
        return False
    

def update_tokens(tokens, bet):
    """
    Updates the tokens when player submits a new bet.
    """
    new_tokens = tokens - int(bet)
    return new_tokens


def how_many_dice():
    """
    Asks the player how many dice will be rolled.
    """
    while True:
        try:
            print(colored('\n Tip: win 4x by rolling 4 dice and playing "Same"!', 'green'))
            x = int(input('How many dice? (2-4): '))
            if (x < 2) or (x > 4):
                print(' The number has to be between 2 and 4, please try again.\n')
                continue
            if (x >= 2) and (x <= 4):
                print(f' You chose {x} dice.')
                time.sleep(1.5)
                break
        except ValueError as e:
            print(f" Invalid data: {e}. Please try again.\n")
            continue
    return x



def choose_play(mania_nr):
    """
    Asks the player to choose their play: more, less or same.
    """
    while True:
        opt = input(f'\n Guess the next Mania Number!\nMore than {mania_nr} (press "M"), Less than {mania_nr} (press "L"), Same as {mania_nr} (press "S"): ').lower()
        if opt == 'm':
            print(' you have chosen "More".\n')
            break
        elif opt == 'l':
            print(' you have chosen "Less".\n')
            break
        elif opt == 's':
            print(' you have chosen "Same".\n')
            break
        else:
            print(f' {opt} is not valid, please try again.\n')
            continue
    return opt


def roll_dice(dice_nr):
    """
    Rolls the number of dice chosen.
    """
    print(f'\n Rolling {dice_nr} dice on the table...')
    time.sleep(1)
    dice = []
    total = 0
    for die in range(dice_nr):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(DICE_ART.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f" Total: {total}")
    return total


def new_play(tokens, bet, play, nr_mania, dice_nr, loop):
    """
    Creates a new play with collected data:
    tokens, bet, play option, mania number.

    Creates three options at the end of each play:
    Continue, top up or quit.
    """
    if loop == 0:
        new_dice_nr = dice_nr
        new_mania_nr = nr_mania
    
    if loop == 1:
        new_dice_nr = how_many_dice()
        new_mania_nr = roll_dice(new_dice_nr)

    if (play == 'm') and (new_mania_nr < nr_mania):
        print(f'\n You lost. You chose "More".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens - bet
        print(f'\n Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print('this feature is under development...')
                break
            elif y == 'q':
                print(f'you quit! Your total balance is {new_tokens}')
                break
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'm') and (new_mania_nr == nr_mania):
        print(f'\nYou lost. You chose "More".\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print('this feature is under development...')
                break
            elif y == 'q':
                print(f'you quit! Your total balance is {new_tokens}')
                break
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'm') and (new_mania_nr > nr_mania):
        print(f'\nYou Won! You chose "More".\n{new_mania_nr} > {nr_mania}')
        new_tokens = tokens + (bet * 2)
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print('this feature is under development...')
                break
            elif y == 'q':
                print(f'you quit! Your total balance is {new_tokens}')
                break
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr > nr_mania):
        print(f'\nYou lost. You chose "Less".\n{new_mania_nr} > {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print('this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr == nr_mania):
        print(f'\nYou lost. You chose "Less".\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr < nr_mania):
        print(f'\n You won! You chose "Less".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens + (bet * 2)
        print(f' Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr > nr_mania):
        print(f'\n You lost. You chose "Same".\n{new_mania_nr} > {nr_mania}')
        new_tokens = tokens - bet
        print(f' Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr < nr_mania):
        print(f'\nYou lost. YOu chose "Same".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr == nr_mania) and (new_dice_nr == 3 or new_dice_nr == 4):
        print(f'\n Congratulations, you won double! You chose "Same" with {new_dice_nr} dice!\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens + (bet * 4)
        print(f' Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' this feature is under development...')
                break
            elif y == 'q':
                print(f' you quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue
    
    elif (play == 's') and (new_mania_nr == nr_mania):
        print(f'\nYou won! You chose "Same".\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens + (bet * 2)
        print(f' Your token balance: {new_tokens}')

        while True:
            y = input('\n Would you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(new_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'r':
                print(' This feature is under development...')
                break
            elif y == 'q':
                print(f' You quit! Your total balance is {new_tokens}')
                break
            else:
                print(' This input is not valid, please try again.')
                continue


def main():
    """
    Prints the rules of the game.
    Runs the functions of the app.
    """
    print("\n")
    create_title()
    print("\n\n Welcome! Bet your tokens to guess the tendency of the next play.\n Are you ready?\n")

    print(" Rules: To win, you need to guess the sum of the next dice play.")
    print("       --------------------------------------------------------")

    print("       Charge your balance with tokens.")
    print(colored("       Place your bet, only whole tokens are accepted.", 'cyan'))
    print("       You start with a Mania Number of 12.")
    print(colored('       Choose the number of dice you want to play from 2 to 4.', "cyan"))
    print('       A single die cannot be played.')
    print(colored("       The sum of the dice you roll will be your new Mania Number (MN).", 'cyan'))
    print('       You must now guess the tendency of the new MN against the old MN.')
    print(colored('       Choose one of three plays: "More", "Less" or "Same".', 'cyan'))
    print('       If you bet "More", "Less" or "Same" and win, you get 2x the bet value.')
    print(colored('       If you bet "same" with 4 dice and win, you get 4x the bet value.', 'cyan'))
    print('       The dice are rolled in, good luck!')
    print(colored("       You can always continue, top up or quit.", 'cyan'))
    print("       You lose when your balance reaches 0.")

    mania_nr = 12
    loop = 0
    tokens = charging_tokens()
    bet, new_tokens = place_bet(tokens, mania_nr)
    dice_nr = how_many_dice()
    play_option = choose_play(mania_nr)
    new_play(new_tokens, bet, play_option, mania_nr, dice_nr, loop)


main()