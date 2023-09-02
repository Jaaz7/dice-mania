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
    Ask the player to charge with tokens so the game can start
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
            print(f'Value has to be as `least 1, you entered {num}')
            return False
        elif int(num) > 500:
            print(f"Maximum value reached, you entered {num}")
            return False
        else:
            return True
    except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False    


def place_bet(tokens, mania_nr):
    """
    Collect the bet from user and return it
    """
    print(f'\nYou have {tokens} tokens and your Mania Number is {mania_nr}.\n')
    while True:
        token_bets = (input('How many tokens would you like to bet for the next play? '))
        if verify_bet(tk, token_bets):
            a, new_tokens = verify_bet(tokens, token_bets)
            print(f'Bet accepted. You have {new_tokens} tokens left.\n')
            time.sleep(1.5)
        else:
            continue
        return [int(token_bets), new_tokens]


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


def choose_play(mania):
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
            x = int(input('\nHow many dice? (2-4): '))
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


def new_play(tokens, bet, play, nr_mania, loop):
    """
    Process a new play with collected data:
    tokens, bet, play option, mania number and looping when needed
    to continue the game
    """
    print('You can win double by betting "Same" on 3 or 4 dice.')
    if loop == 0:
        new_dice_nr = how_many_dice()
        new_mania_nr = roll_dice(new_dice_nr)
    
    if loop == 1:
        new_dice_nr = how_many_dice()
        new_mania_nr = roll_dice(new_dice_nr)

    if (play == 'm') and (new_mania_nr < nr_mania):
        print(f'\nYou lost. You chose "More".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens - bet
        print(f'\nYour token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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

    elif (play == 'l') and (new_mania_nr == nr_mania):
        print(f'\nYou lost. You chose "Less".\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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

    elif (play == 'l') and (new_mania_nr < nr_mania):
        print(f'\nYou won! You chose "Less".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens + (bet * 2)
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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

    elif (play == 's') and (new_mania_nr > nr_mania):
        print(f'\nYou lost. You chose "Same".\n{new_mania_nr} > {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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

    elif (play == 's') and (new_mania_nr < nr_mania):
        print(f'\nYou lost. YOu chose "Same".\n{new_mania_nr} < {nr_mania}')
        new_tokens = tokens - bet
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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

    elif (play == 's') and (new_mania_nr == nr_mania) and (new_dice_nr == 3 or new_dice_nr == 4):
        print(f'\nCongratulations, you won double! You chose "Same" with {new_dice_nr} dice!\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens + (bet * 4)
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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
    
    elif (play == 's') and (new_mania_nr == nr_mania):
        print(f'\nYou won! You chose "Same".\n{new_mania_nr} = {nr_mania}')
        new_tokens = tokens + (bet * 2)
        print(f'Your token balance: {new_tokens}')

        while True:
            y = input('\nWould you like to continue? (press "C");\nRecharge? (press "R")\nQuit? (Press "Q"): ').lower()
            if y == 'c':
                x = how_many_dice()
                mn = roll_dice(x)
                bet_nr, updated_tokens = place_bet(new_tokens, mn)
                play_name = choose_play(mn)
                lp = 1
                new_play(updated_tokens, bet_nr, play_name, mn, lp)
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
    print("       Charge your balance with tokens.")
    print(colored("       Place your bet, only whole tokens are accepted.", "magenta"))
    print(
        "       You start with a Mania Number of 12."
    )
    print(
        colored(
            '       Choose the number of dice you want to play from 2 to 4. A single die cannot be played.',
            "black",
        )
    )
    print('       The sum of the dice you roll will be your new Mania Number.')
    print('       You then have three play options towards the number 12, will the new Mania Number be: "More", "Less" or "Same"')
    print('       If you bet "More", "Less" or "Same" and win, you win.')
    print(colored('       If you bet "same" with 3 or 4 dice and win, you win DOUBLE.', "black"))
    print('       The dice are rolled in.')
    print(colored("       You can always continue, top up or quit.", "black"))
    print("       You lose when your balance reaches 0.")

    tokens = charging_tokens()
    bet, new_tokens = place_bet(tokens)
    mania_nr = 12
    play_option = choose_play(mania_nr)
    loop = 0
    new_play(new_tokens, bet, play_option, mania_nr, loop)


main()