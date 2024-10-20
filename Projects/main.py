MAX_BET = 3
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount < 0:
                print("Amount must be greater than 0.")
            else: 
                break
        else:
            print("Invalid! Please enter digit.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines bet on (1-" + str(MAX_BET) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_BET:
                break
            else: 
                print("Please enter a valid number of lines.")
        else:
            print("Invalid! Please enter digit.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Please enter amount between ${MIN_BET} - {MAX_BET}")
        else:
            print("Invalid! Please enter digit.")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet, your current balance is {balance} and you bet for {total_bet}.")
            break

    # print(f"You are betting on ${bet} on {lines}. Total bet is is equal to: {total_bet}$")

main()