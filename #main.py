import random

MAX_LINES = 3
MIN_LINES = 1
MAX_BET = 500
MIN_BET = 1

ROWS=3
COLS=3

symbol_count= {
    "💎": 4,
    "🍀": 5,
    "🍒": 7,
    "🍋": 10,
}
symbol_values = {
    "💎": 5,
    "🍀": 4,
    "🍒": 3,
    "🍋": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copia dei simboli
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)  

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column [row], end=" | ")
            else:
                print(column [row], end=" ")

        print()



def deposit():
    while True:
        amount = input("Quanto vuoi depositare nel tuo conto PasqualBet? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Deposito di ${amount} effettuato con successo.")
                break
            else:
                print("L'importo deve essere maggiore di zero.")
        else:
            print("Per favore, inserisci un numero valido.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Su quali linee vuoi scommettere? \n 1 = solo la prima \n 2 = la prima e la seconda \n 3 = tutte e {str(MAX_LINES)} le linee \n ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= MIN_LINES and lines <= MAX_LINES:
                break
            else:
                print(f"Puoi scommettere su un numero che va da  {MIN_LINES} a {MAX_LINES} linee.")
        else:
            print("Per favore, inserisci un numero valido.")
    return lines


def get_bet():
    while True:
        bet = input("Quanto vuoi scommettere su ogni linea? : $ ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Puoi scommettere un importo che va da  {MIN_BET} a {MAX_BET} $.")
        else:
            print("Per favore, inserisci un importo numerico valido.")

    return bet

def spin(balance, bet, lines):
    total_bet =  bet * lines
    if total_bet > balance:
        print(f"Non puoi scommettere ${total_bet} con un saldo di ${balance}.")
        return 0
    print(f"Il tuo saldo attuale è di ${balance}, stai scommettendo {bet} $  su {lines} linee. \nLa tua scommessa totale è di ${total_bet}.")
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    if winnings != 0:
        print(f"Hai vinto ${winnings}!")
        print("Linea vincente: ", *winning_lines)
    else:
        print("Non hai vinto nulla, riprova!")
    return winnings - total_bet


def main():
    print("Benvenuto su PasqualBet!")
    print("Per favore, effettua un deposito iniziale per iniziare a scommettere.")
    print("\n")
    
    balance = deposit()
    bet= get_bet()
    lines = get_number_of_lines()

    while True:
        print(f"Il tuo saldo attuale è di ${balance}.La tua scommessa è di ${bet} su {lines} linee.")
        scelta = input("Premi INVIO per spin, 'm' per modificare bet/linee, 'q' per uscire: ")
        if scelta == "q":
            break
        elif scelta == "m":
            bet = get_bet()
            lines = get_number_of_lines()
            continue
        risultato = spin(balance, bet, lines)
        balance += risultato
        if balance <= 0:
            print("Hai finito il saldo! Ricarica per continuare a giocare.")
            break

main()
    

    