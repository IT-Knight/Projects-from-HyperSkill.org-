import random as r
 
default_options = ['rock', 'scissors', 'paper']
 
options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf',
           'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'lizard', 'spock', '!exit', '!rating']          
            
options_5 = ['rock','paper','scissors','lizard','spock']
           
win_3 = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
 
win_5 = {'rock': ['lizard', 'scissors'], 
        'paper': ['rock', 'spock'],
        'scissors': ['lizard', 'paper'], 
        'lizard': ['paper', 'spock'], 
        'spock': ['scissors', 'rock']}
 
win_15 = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
           'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
           'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
           'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
           'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
           'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
           'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
           'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
           'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
           'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
           'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
           'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
           'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
           'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
           'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
 
name_of_looser = input()
print('Hello, %s' % name_of_looser)
rating_of_looser = 0
 
def game_on_3(user):
    AI = r.choice(default_options)
    if AI == user:
        return f'There is a draw ({user})'
    if AI in win_3[user]:
        return f'Well done. Computer chose {AI} and failed'
    else:
        return f'Sorry, but computer chose {AI}'
 
def game_on_5(user):
    AI = r.choice(options_5)
    if AI == user:
        return f'There is a draw ({user})'
    if AI in win_5[user]:
        return f'Well done. Computer chose {AI} and failed'
    else:
        return f'Sorry, but computer chose {AI}'
    
def game_on_15(user):
    AI = r.choice(options[:15])
    if AI == user:
        return f'There is a draw ({user})'
    if AI in win_15[user]:
        return f'Well done. Computer chose {AI} and failed'
    else:
        return f'Sorry, but computer chose {AI}'
 
while True:
    rules = input()
    if rules:
        rules = rules.split(',')
        len_rules = len(rules)
        if len_rules == 5:
            t = 5
            break
        elif len_rules == 15:
            t = 15
            break
    if not rules:
        t = 3
        break
    else:
        print('Invalid input')
        continue
print("Okay, let's start")
 
user = None
while user != '!exit':
    user = input()
    if user not in options:
        print('Invalid input')
        continue
    elif user in '!rating':
        count = 0
        if count == 0:
            with open('rating.txt', 'r') as f:
                for line in f:
                    temp = line.split()
                    if name_of_looser in temp[0]:
                        rating_of_looser = temp[1]
                        print(f'Your rating: {rating_of_looser}')
                        count += 1
                else:
                    print(f'Your rating: {rating_of_looser}')
            continue
        else:
            print(f'Your rating: {rating_of_looser}')
            continue                    
    elif user in '!exit':
        break
    else:
        if t == 3:        
            result = game_on_3(user)
            print(result)
        elif t == 5:
            result = game_on_5(user)
            print(result)
        elif t == 15:
            result = game_on_15(user)
            print(result)
        if result.startswith('Well done'):
            rating_of_looser += 100
        elif result.startswith('There is a draw'):
            rating_of_looser += 50
        else:
            rating_of_looser += 0
        
print('Bye!')
