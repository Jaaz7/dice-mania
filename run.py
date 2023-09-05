import random
from termcolor import colored
import time
import sys


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


class bold:
   BOLD = '\033[1m'
   YELLOW = '\033[93m'
   END = '\033[0m'


def create_title():
    """
    Creates the dice mania ASCII art.
    """
    for line in range(8):
        for tuple in range(1, 3):
            print(colored(bold.BOLD +
                          DICE_MANIA.get(tuple)[line], "yellow"), end="  ")
        print()


def charging_tokens():
    """
    Asks the player to charge the account with tokens.
    """
    while True:
        tokens = input("\n Charge your account (max 500): ")
        if verify_tokens(tokens):
            print(" Number accepted.\n")
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
            print(f' Value has to be as least 1, you entered {num}')
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
    string1 = '\n You have'
    string2 = 'tokens and your Mania Number is'
    print(string1, bold.BOLD + colored(tokens, 'cyan'),
          string2, bold.BOLD + colored(mania_nr, 'yellow'), '\n')
    while True:
        bet = (input(' How many tokens would you like to bet? '))
        if verify_bet(tokens, bet):
            truth_statement, new_tokens = verify_bet(tokens, bet)
            if new_tokens == 0:
                string1 = ' Bet accepted. You have'
                string2 = '0'
                string3 = 'tokens left. Brave one!\n'
                print(string1, bold.BOLD + colored(string2, 'red'), string3)
                time.sleep(1.5)
            else:
                string1 = ' Bet accepted. You have'
                string2 = 'tokens left.\n'
                print(string1, bold.BOLD +
                      colored(new_tokens, 'cyan'), string2)
                time.sleep(1.5)
        else:
            continue
        return [int(bet), new_tokens]


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
            print(bold.BOLD + colored('\n Tip: win 4x by rolling 4 dice and playing "Same"!', 'yellow'))
            x = int(input(' How many dice do you want to play this round? (2-4 possible): '))
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
        opt = input(f'\n Guess the next Mania Number!\n     It will be more than {mania_nr} (press {bold.BOLD + bold.YELLOW + "M" + bold.END})\n     It will be less than {mania_nr} (press {bold.BOLD + bold.YELLOW + "L" + bold.END})\n     It will be the same as {mania_nr} (press {bold.BOLD + bold.YELLOW + "S" + bold.END}): ').lower()
        if (opt == 'm') or (opt == 'l') or (opt == 's'):
            print('')
            break
        else:
            print(f' {opt} is not valid, please try again.\n')
            continue
    return opt


def roll_dice(dice_nr):
    """
    Rolls the number of dice chosen.
    """
    print(bold.BOLD + colored(f' Rolling {dice_nr} dice on the table...', 'yellow'))
    time.sleep(1)
    dice = []
    total = 0
    for die in range(dice_nr):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(bold.BOLD + colored(bold.BOLD + DICE_ART.get(die)[line], 'yellow'), end="")
        print()

    for die in dice:
        total += die
    print(f" Total: {total}")
    return total


def new_play(tokens, bet, play, old_mania, nr_mania, dice_nr, loop):
    """
    Creates a new play with collected data:
    tokens, bet, play option, old mania number, new mania number, dice number and loop.

    Creates three options at the end of each play:
    Continue, top up or quit.
    """

    if loop == 0:
        new_mania_nr = roll_dice(dice_nr)

    elif loop == 1:
        new_mania_nr = nr_mania

    if (play == 'm') and (new_mania_nr < old_mania):
        print(bold.BOLD + colored(f'\n You lose', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "More" + bold.END}.\n {new_mania_nr} < {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f"\n\n You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'm') and (new_mania_nr == old_mania):
        print(bold.BOLD + colored(f'\n You lose.', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "More" + bold.END}.\n {new_mania_nr} = {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'm') and (new_mania_nr > old_mania):
        print(bold.BOLD + colored(f'\n You win {bet * 2} tokens!', 'cyan'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "More" + bold.END}.\n {new_mania_nr} > {old_mania}')
        new_tokens = tokens + (bet * 2)
        if new_tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(new_tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(new_tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(new_tokens, 'cyan'), string2)
                sys.exit()
            else:
                print('This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr > old_mania):
        print(bold.BOLD + colored(f'\n You lose.', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Less" + bold.END}.\n {new_mania_nr} > {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr == old_mania):
        print(bold.BOLD + colored(f'\n You lose.', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Less" + bold.END}.\n {new_mania_nr} = {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 'l') and (new_mania_nr < old_mania):
        print(bold.BOLD + colored(f'\n You win {bet * 2} tokens!', 'cyan'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Less" + bold.END}.\n {new_mania_nr} < {old_mania}')
        new_tokens = tokens + (bet * 2)
        string1 = '\n Your token balance:'
        if new_tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(new_tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(new_tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(new_tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr > old_mania):
        print(bold.BOLD + colored(f'\n You lose.', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Same" + bold.END}.\n {new_mania_nr} > {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr < old_mania):
        print(bold.BOLD + colored(f'\n You lose.', 'red'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Same" + bold.END}.\n {new_mania_nr} < {old_mania}')
        string1 = '\n Your token balance:'
        if tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(tokens):
                break
            else:
                print(f" You're out of tokens. Game over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr == old_mania) and (dice_nr == 4):
        print(bold.BOLD + colored(f'\n Congratulations, you won a Jackpot! {bet * 4} tokens!', 'yellow'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Same" + bold.END}.\n {new_mania_nr} = {old_mania}')
        new_tokens = tokens + (bet * 4)
        string1 = '\n Your token balance:'
        if new_tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(new_tokens):
                break
            else:
                print(f" You're out of tokens. Game Over!")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(new_tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(new_tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue

    elif (play == 's') and (new_mania_nr == old_mania):
        print(bold.BOLD + colored(f'\n You win {bet * 2} tokens!', 'cyan'))
        print(f' You chose {bold.BOLD + bold.YELLOW + "Same" + bold.END}.\n {new_mania_nr} = {old_mania}')
        new_tokens = tokens + (bet * 2)
        string1 = '\n Your token balance:'
        if new_tokens == 0:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'red'))
        else:
            string1 = '\n Your token balance:'
            print(string1, bold.BOLD + colored(new_tokens, 'cyan'))
        print('---------------------------------------------------')
        while True:
            if verify_balance(new_tokens):
                break
            else:
                print(f"\n You're out of tokens. Game Over.")
                sys.exit()

        while True:
            y = input(f'\n Would you like to continue? (press {bold.BOLD + bold.YELLOW + "C" + bold.END});\n Top up & continue? (press {bold.BOLD + bold.YELLOW + "T" + bold.END})\n Quit? (Press {bold.BOLD + bold.YELLOW + "Q" + bold.END}): ').lower()
            if y == 'c':
                bet_nr, updated_tokens = place_bet(new_tokens, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 't':
                new_balance = top_up(new_tokens)
                bet_nr, updated_tokens = place_bet(new_balance, new_mania_nr)
                updated_dice_nr = how_many_dice()
                play_name = choose_play(new_mania_nr)
                updated_mania_nr = roll_dice(updated_dice_nr)
                loop = 1
                new_play(updated_tokens, bet_nr, play_name, new_mania_nr, updated_mania_nr, updated_dice_nr, loop)
                break
            elif y == 'q':
                string1 = '\n Thanks for playing! You redeemed'
                string2 = 'tokens.'
                print(string1, bold.BOLD + colored(new_tokens, 'cyan'), string2)
                sys.exit()
            else:
                print(' This input is not valid, please try again.')
                continue


def verify_balance(balance):
    """
    Check if the token balance is still postiive so the game can keep running
    """
    if balance == 0:
        return False
    else:
        return True


def top_up(balance):
    """
    Add more tokens to the current balance
    """
    while True:
        top_up = input("\n Top up amount (max 500): ")
        if verify_tokens(top_up):
            print(" Number accepted.\n")
            new_balance = balance + int(top_up)
            time.sleep(1.5)
        else:
            continue
        return int(new_balance)


def main():
    """
    Prints the rules of the game.
    Runs the functions of the app.
    """
    print("\n")
    create_title()
    print("\n\n Welcome! Bet your tokens and guess the sum of the next dice play.\n Are you ready?\n")
    print(bold.YELLOW + bold.BOLD + ' Tip: Press "Enter" after entering a value/number to play.' + bold.END)
    print(bold.BOLD + colored(' This game window needs to be clicked to be interacted with.', "cyan"))
    print(bold.YELLOW + bold.BOLD + ' If you enjoy the game, you can share it with a friend!\n' + bold.END)
    while True:
        answer = input('\n Would you like to display the rules? (y/n): ').lower()
        if answer == 'y':
            print(bold.YELLOW + bold.BOLD + "\n       Rules below:" + bold.END)
            print("       --------------------------------------------------------")

            print("       1 Charge your balance with tokens.")
            print(bold.BOLD + colored("       2. Place your bet, only whole tokens are accepted.", 'cyan'))
            print("       You start with a Mania Number of 12.")
            print(bold.BOLD + colored('       3. Choose the number of dice you want to play from 2 to 4.', "cyan"))
            print('       A single die cannot be played.')
            print(bold.BOLD + colored("       The sum of the dice rolled will be your new Mania Number (let's call it MN).", 'cyan'))
            print('       You must now guess the sum of new MN against the old MN.')
            print(bold.BOLD + colored('       4. Choose one of three plays: "More", "Less" or "Same".', 'cyan'))
            print('       If you bet "More", "Less" or "Same" and win, you get 2x the bet value.')
            print(bold.BOLD + colored('       If you bet "Same" with 4 dice and win, you get a 4x Jackpot!', 'cyan'))
            print('       The dice are rolled in, good luck!')
            print(bold.BOLD + colored("       You can always continue, top up or quit.", 'cyan'))
            print("       You lose when your balance reaches 0.")
            break
        elif answer == 'n':
            break
        else:
            print(' Input not valid, please try again.')
            continue
    """
    The useless_var has no use here but it still has to be called for the function
    to work because it's an argument on the function itself.
    The player already has a mania number of 12 the first time playing.
    From the second time on, the system needs to compare the new mania number against the old one.

    This is the reason there's a loop var, the dice are not being rolled here in this function
    because we already have 12 as "old mania number". When the loop is 1, the old mania will be assigned
    at the new_play function.
    """
    mania_nr = 12
    tokens = charging_tokens()
    bet, new_tokens = place_bet(tokens, mania_nr)
    dice_nr = how_many_dice()
    play_option = choose_play(mania_nr)
    loop = 0
    useless_var = 0
    new_play(new_tokens, bet, play_option, mania_nr, useless_var, dice_nr, loop)


main()
