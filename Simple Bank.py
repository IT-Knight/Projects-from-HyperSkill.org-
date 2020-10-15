
import random as HeavyMetal  # a joke
import sys as matrix         # same
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS card (
    id INTEGER,
    number TEXT,
    pin TEXT, 
    balance INTEGER DEFAULT 0, 
    PRIMARY KEY("id")
)''')

conn.commit()

# To get data returned by SELECT query you can user fetchone(), fetchall() methods:
# cur.execute('SOME SELECT QUERY')
# cur.fetchone()  # Returns the first row from the response
# cur.fetchall()  # Returns all rows from the response
# conn.commit() 

emety = ''


def insert_details(a, b, c=None):
    global input_id, input_pin
    if b is None:  # это трансфер
        cur.execute(f"UPDATE card SET balance = balance - {c} WHERE number = '{input_id}'")  # отняли у отправителя
        conn.commit()  # страх.
        cur.execute(f"UPDATE card SET balance = balance + {c} WHERE number = '{a}'")  # добавили получателю
    elif c is not None:  # это Income
        cur.execute(f"UPDATE card SET balance = balance + {c} WHERE number = '{a}' and pin = '{b}'")
    else:  # это создание нового аккаунта с 0-ым балансом.
        cur.execute(f"INSERT INTO card (number, pin) VALUES ({a}, {b})")
    conn.commit()


input_id, input_pin = None, None
balance = 0

def card_check(): # сразу тут считываем и баланс на будущее
    global input_id, input_pin, balance
    input_id = input('Enter your card number:\n')
    input_pin = input('Enter your PIN:\n')
    for i, row in enumerate(cur.execute('SELECT number, pin, balance FROM card')):
        if input_id in row and input_pin in row:
            balance = row[-1]
            print('\nYou have successfully logged in!\n')
            return True
    return False

def lunh_controling(string):
    if str(string).isdigit():
        # Count control string.
        number = str(string)[:-1]
        total_count = number_sum(number)
        value = int(total_count) + int(str(string)[-1])
        # Control multiplicity 10
        return (value % 10 == 0)
    else:
        return False

def login_cycle():
    global balance, input_id, input_pin
    while True:
        login_option = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
        if login_option == '1':
            current_balance = balance
            print(f'Balance: {current_balance}\n')
            continue
        if login_option == '2':
            income = int(input('\nEnter income:\n'))
            insert_details(input_id, input_pin, c=income)
            balance += income
            print('Income was added!\n')
            continue
        if login_option == '3':
            transfer_id = input('\nTransfer\nEnter card number:\n')
            if lunh_controling(transfer_id) is False:
                print('Probably you made mistake in the card number. Please try again!\n')
                continue
            temp_transfer_id = (f'{transfer_id}',)
            cur.execute('SELECT number FROM card')
            if temp_transfer_id not in cur.fetchall():
                print('Such a card does not exist.\n')
                continue
            else:  # она есть в базе и работаем
                money_to_transfer = int(input('Enter how much money you want to transfer:\n'))
                if money_to_transfer > balance:
                    print('Not enough money!\n')
                    continue
                else:
                    insert_details(transfer_id, b=None, c=money_to_transfer)
                    balance -= money_to_transfer
                    print('Success!\n')
                    continue
        if login_option == '4':  # Close account == Log out + DELETE FOREVER
            cur.execute(f'DELETE FROM card WHERE number = {input_id}')
            conn.commit()
            print('The account has been closed!')
            return True
        if login_option == '5':
            print('You have successfully logged out!\n')
            return True
        if login_option == '0':
            _exit()
            matrix.exit()


def _exit():
    print('\nBye!')


def generate_id():
    global emety
    while True:
        part_1 = '400000'
        part_2_str_list = [str(HeavyMetal.randint(0, 9)) for x in range(9)]
        unique_id1 = str(part_1) + str(emety.join(part_2_str_list))
        unique_id = to_lunh(unique_id1)
        break_count = 0
        for i, row in enumerate(cur.execute('SELECT number, pin, balance FROM card')):
            if unique_id in row:
                break_count += 1
                break  # stops the for cycle ^^ not while
        if break_count == 1:
             continue
        return unique_id


def number_sum(string):
    # find sum to all digits without ECC number
    numbers = list(str(string))
    number_sum = 0
    lenght = len(numbers)
    for x in range(0, lenght):
        if x % 2 == 0:
            number = (int(numbers[x]) * 2)
            if int(number) > 9:
                double_numbers = list(str(number))
                number = int(double_numbers[0]) + int(double_numbers[1])
        else:
            number = (numbers[x])
        number_sum += int(number)
    return(number_sum)


def to_lunh(string):
    # Add control number.
    if str(string).isdigit():
        total_count = int(number_sum(string))
        # Find control number
        control = 0
        while control < 10:
            value = total_count + control
            if (value % 10 == 0):
                break
            else:
                control += 1
        #Make new number
        lunh_number = str(string) + str(control)
        return(lunh_number)


def new_card():
    luhn_card_num = generate_id()
    pin_code = str(HeavyMetal.randint(1000, 9999))
    insert_details(luhn_card_num, pin_code)  # БЛОК ДАННЫХ ОТПРАВЛЯЕТЬСЯ В БД!
    return luhn_card_num, int(pin_code)


while True:
    selection = input('1. Create an account\n2. Log into account\n0. Exit\n')
    check_list1 = ['0', '1', '2']
    if selection == '1':
        NEW_CARD_NUMBER, NEW_PIN = new_card()
        print(f"""Your card has been created
Your card number:
{NEW_CARD_NUMBER}
Your card PIN:
{NEW_PIN}\n""")
        continue
    if selection == '2':
        if card_check():
            pass
        else:
             print('Wrong card number or PIN!\n')
        if login_cycle():
            continue
    if selection == '0':
        matrix.exit()
