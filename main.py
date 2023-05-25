import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,    
}
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,    
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
    return winnings
                
    


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns = []
    
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
    
        
        columns.append(column)
    return columns    
   
def print_slot_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" |")
            else:
                print(column[row])
             
    print()   
    
    
    
     

def deposit():
    while True:
        amount = input("Enter the Deposit amount in Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must me greater than Rs.0.00")
        else:
            print("please enter a number.")
    return amount 


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines that u wanna bet.(1-" + str(MAX_LINES) + "?)")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of line")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("Enter the bet that u want? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must me between Rs.{MIN_BET}.00 - {MAX_BET}.00")
        else:
            print("please enter a number.")
    return amount 
    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough balance to bet, Your account balance is Rs.{balance}.00")
        else:
            break
    
    print(f"You are betting Rs.{bet} on {lines} lines. The total bet is equal to {total_bet}.00")
    
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_spin(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won Rs.{winnings}")
    
     
main()
     
def game() :
    while True:
        playAgain = input("Do you want to play again?(y/n) :")
        if playAgain == 'y':
            main()
        else:
            break
    
    
game()





 




   
             