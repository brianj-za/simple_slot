import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_design = {
    ("A", 2, 10),
    ("B", 4, 4),
    ("C", 6, 2),
    ("D", 8, 1)
}


def check_winnings(reels, lines, wager):
    winnings = 0
    slot = [list(x) for x in zip(*reels)][:lines]
    for row in slot:
        symbol = row[0]
        win = True
        for col in row[1:]:
            if col != symbol:
                win = False
                break
        if win:
            for symbol_set in symbol_design:
                if symbol_set[0] == symbol:
                    value = symbol_set[2]
                    winnings += wager * value
        print(row)
    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol in symbols:
        for _ in range(symbol[1]):
            all_symbols.append(symbol[0])

    reels = []
    for _ in range(cols):
        random.shuffle(all_symbols)
        reels.append(all_symbols[0:rows])

    return reels


def print_slot_machine(reels):
    slot = [list(x) for x in zip(*reels)]
    for row in slot:
        print("|".join(row))


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Amount must be greater than 0.")
        else:
            print("Please enter a valid, positive number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How lines would you like to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f"Nmber of lines must be within 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid, positive number.")
    return lines


def get_bet(lines, balance):
    while True:
        wager = input(f"How much would you like to bet per line (${MIN_BET}-${MAX_BET}? ")
        if wager.isdigit():
            wager = int(wager)
            if wager * lines > balance:
                print(f"You do not have a big enough balance. Please try again")
            elif MIN_BET <= wager <= MAX_BET:
                break
            else:
                print(f"Wager must be within ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid, positive number.")
    return wager


def play_game(balance):
    lines = get_number_of_lines()
    wager = get_bet(lines, balance)
    total_wager = lines * wager
    print(f"You are betting ${wager} on {lines} lines. Your total bet is ${total_wager}.")

    reels = get_slot_machine_spin(ROWS, COLS, symbol_design)
    print_slot_machine(reels)

    winnings = check_winnings(reels, lines, wager)
    if winnings > 0:
        print(f"You won ${winnings}!")
    else:
        print("You won NOTHING loser!")

    return winnings - total_wager


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        spin = input("Press enter to spin (q to quit).")
        if spin == "q":
            break
        balance += play_game(balance)


main()
