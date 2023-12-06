import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_design = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    reels = []
    for _ in range(cols):
        random.shuffle(all_symbols)
        reels.append(all_symbols[0:rows])

    return reels


def print_slot_machine(reels):
    for row in range(len(reels[0])):
        print("|".join(reels[row]))


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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    wager = get_bet(lines, balance)
    print(f"You are betting ${wager} on {lines} lines. Your total bet is ${lines * wager}.")

    reels = get_slot_machine_spin(ROWS, COLS, symbol_design)
    print_slot_machine(reels)


main()
