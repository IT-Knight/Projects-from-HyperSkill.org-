from sys import argv
import sys
import math
 
 
def credit_principal(payment, periods, interest):
    return (payment / ((interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1)))
 
def credit_interest(interest):
    return interest / 12 / 100
 
def annuity_payment(principal, periods, interest):
    annuity_payment = math.ceil(principal * (interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    print(f'Your annuity payment = {annuity_payment}!')
    print(f'Overpayment = {annuity_payment * periods - principal}')
 
def credit_principal(payment, periods, interest):
    principal = int(payment / ((interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1)))
    print(f'Your credit principal = {principal}!')
    print(f'Overpaiment = {payment * periods - principal}')
 
def time_to_repay(principal, payment, interest):
    repay = math.ceil(math.log((payment / (payment - interest * principal)), 1 + interest))
    if repay % 12 != 0:
        print(f'You need {int(repay // 12)} years and {math.ceil(repay % 12)} months to repay this credit!')
    else:
        print(f'You need {int(repay // 12)} years to return this credit!')
    print(f'Overpayment = {int(payment * repay - principal)}')
 
 
def diff(principal, periods, interest):
    sum_D = 0
    for i in range(1, int(periods) + 1):
        D = math.ceil(principal/periods + interest * (principal - ((principal * (i - 1))/periods)))
        sum_D += D 
        print(f'Month {i}: paid out {D}')  
    print(f'Overpayment = {sum_D - principal}')  
 
 
def executer(arg):
    if (len(sys.argv) != 5) or (argv[1].split('=')[1] not in ('annuity', 'diff')): # исключили неверную длину аргументов и неверный тип.
        return print('Incorrect parameters1')
    if 'diff' not in arg[1]:
        type_ = 0 
    else: 
        type_ = 1 
    annuity_vars = ['type', 'principal','payment','periods','interest']
    diff_vars = ['type', 'principal','periods','interest']
    list_of_vars = []
    list_of_value = []
    for i in range(1,5):
        var, value = argv[i].split("=")
        var = var.replace('--', '') # форматнули '--'
        if (isinstance(value, float) or isinstance(value, int)) and value != abs(value): # исключили невреные - отрицательные значения
            return print('Incorrect parameters2')
        if type_ == 0 and var not in annuity_vars: # исключили неверные переменные по annuity
            return print('Incorrect parameters3')
        if type_ == 1 and var not in diff_vars:  # исключили неверные переменные по diff
            return print('Incorrect parameters4')
        list_of_vars.append(var)
        list_of_value.append(value)
    for _ in range(1,3):
            list_of_value[_] = int(list_of_value[_])
    list_of_value[3] = float(list_of_value[3])
    io = dict(zip(list_of_vars, list_of_value)) # идеально io['principal'], io['payment'], io['periods'], io['interest'], io['type']
    
    # дальше вызываем соответствующие функции + принты
    
    interest = credit_interest(io['interest'])
 
    if io['type'] == 'annuity' and io.get('principal') and io.get('payment') and io['interest']:
        time_to_repay(io['principal'], io['payment'], interest)
 
    elif io['type'] == 'annuity' and io.get('payment') and io.get('periods') and io['interest']: 
        credit_principal(io['payment'], io['periods'], interest)
 
    elif io['type'] == 'annuity' and io.get('principal') and io.get('periods') and io['interest']:
        annuity_payment(io['principal'], io['periods'], interest)
 
    if io['type'] == 'diff' and io.get('principal') and io.get('periods') and io['interest']:
        diff(io['principal'], io['periods'], interest)
        
        
executer(sys.argv)
