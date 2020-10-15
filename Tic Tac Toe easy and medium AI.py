from random import randint, choice
import sys 
import time  # don't use time module ^^

xo_string = ["_" for i in range(9)]  # генерация пустого поля
symbols = ["X", "O"]  # 
n = 0
XO_dict = {}
count = 0
for i in range(3, 0, -1): # словарь забитый значениями по координатам от 0 до 8
    for j in range(1, 4):
        XO_dict[(j, i)] = xo_string[n]
        n += 1
 
def draw(s):  # генерирует и выводит доску
    global count
    if count == 1:
        print('Making move level "easy"')
    if count == 2:
        print('Making move level "medium"')
    show = [" ".join([s[i] for i in range(j * 3, (j * 3) + 3)]) for j in range(3)]
    print("---------")
    print("\n".join([f"| {x} |" for x in show]))
    print("---------")
 
def update_combo():  # обновляет значения к комбо.
    combo1 = ["".join([xo_string[i] for i in range(j * 3, (j * 3) + 3)]) for j in range(3)]
    combo2 = ["".join([xo_string[i] for i in range(j, 8 + j, 3)]) for j in range(3)]
    combo3 = ["".join([xo_string[i] for i in [0 + j, 4, 8 - j]]) for j in range(0, 3, 2)]
    return combo1, combo2, combo3
 
def combo_check(xo):  # проверка на победу одной из сторон или ничью
    combo1, combo2, combo3 = update_combo()
    return (xo in combo1) or (xo in combo2) or (xo in combo3)
 
def calculate():  # выяснение состояния победы или ничьи и возврат.
    global xo_string
    if combo_check("XXX"):
        draw(xo_string)
        print("X wins\n")
        xo_string = ["_" for i in range(9)]
        return True
    elif combo_check("OOO"):
        draw(xo_string)
        print("O wins\n")
        xo_string = ["_" for i in range(9)]
        return True
    elif (not combo_check("XXX")) and (not combo_check("OOO")) and (not "_" in xo_string):
        draw(xo_string)
        print("Draw\n")
        xo_string = ["_" for i in range(9)]
        return True
    return False
 
def check_coords(coord):  # проверка на верность введеных координат
    global xo_string
    curr_value = XO_dict.get(coord, -1)
    if curr_value == -1 :
        print("Coordinates should be from 1 to 3!\n")
        return  False
    if curr_value == "_":
        XO_dict[coord] = symbols[((xo_string.count("X") + xo_string.count("O")) % 2)]
        xo_string = "".join(XO_dict.values())
        # draw(xo_string)
        return True
    else:
        print("This cell is occupied! Choose another one!\n")
        return False
 
def easy_ai():
    global XO_dict
    n = [1,2,3]
    n2 = [3,2,1]
    # ai_choice = ((choice(n), choice(n2))) good too
    ai_choice = ((randint(1,3), randint(1,3)))
    ai_choice_value = XO_dict.get(ai_choice)
    while ai_choice_value != '_':  # ходит тупо в пустую клетку
        # ai_choice = ((choice(n), choice(n2))) 
        ai_choice = ((randint(1,3), randint(1,3)))
        ai_choice_value = XO_dict.get(ai_choice)
    coords = ai_choice
    return coords

def can_win(a1,a2,a3,smb):  
    global ai_player
    res = False
    if ai_player == 1:
        if a1 == smb and a2 == smb and a3 == '_':
            a3 = 'X'
            res = True
        if a1 == smb and a2 == '_' and a3 == smb:
            a2 = 'X'
            res = True
        if a1 == '_' and a2 == smb and a3 == smb:
            a1 = 'X'
            res = True
    if ai_player == 2:
        if a1 == smb and a2 == smb and a3 == '_':
            a3 = 'O'
            res = True
        if a1 == smb and a2 == '_' and a3 == smb:
            a2 = 'O'
            res = True
        if a1 == '_' and a2 == smb and a3 == smb:
            a1 = 'O'
            res = True
    return res


def stupid_coords(a,b,c):
    for coords in [a,b,c]:
        if XO_dict[coords] == '_':
            return coords


def medium_ai():  # copied
    global XO_dict
    for n in range(1, 4):  # 8 вариантов на 'O' 
        a, b, c = (n, 1), (n, 2), (n, 3)
        if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'O'):  # 3
            coords = stupid_coords(a,b,c)
            return coords

        a, b, c = (1, n), (2, n), (3, n)
        if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'O'):  # 6
            coords = stupid_coords(a,b,c)
            return coords
    a, b, c = (1, 1), (2, 2), (3, 3)
    if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'O'): # 7
        coords = stupid_coords(a,b,c)
        return coords
    a, b, c = (3, 1), (2, 2), (1, 3)
    if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'O'): # 8
        coords = stupid_coords(a,b,c)
        return coords
    
    for n in range(1, 4):  # 8 вариантов на 'X' 
        a, b, c = (n, 1), (n, 2), (n, 3)
        if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'X'):  # 3
            coords = stupid_coords(a,b,c)
            return coords

        a, b, c = (1, n), (2, n), (3, n)
        if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'X'):  # 6
            coords = stupid_coords(a,b,c)
            return coords
    a, b, c = (1, 1), (2, 2), (3, 3)
    if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'X'): # 7
        coords = stupid_coords(a,b,c)
        return coords
    a, b, c = (3, 1), (2, 2), (1, 3)
    if can_win(XO_dict[a], XO_dict[b], XO_dict[c], 'X'): # 8
        coords = stupid_coords(a,b,c)
        return coords

    ai_choice = ((randint(1,3), randint(1,3)))
    ai_choice_value = XO_dict.get(ai_choice)
    while ai_choice_value != '_':  # ходит тупо в пустую клетку из easy_ai
        ai_choice = ((randint(1,3), randint(1,3)))
        ai_choice_value = XO_dict.get(ai_choice)
    coords = ai_choice
    return coords

true_tuple = ('start easy easy', 'start easy user', 'start user easy', 'start user user', 'start medium medium', 'start medium user', 'start user medium', 'start medium easy', 'start easy medium', 'exit')

while True:  # воодим координаты поочередно
    command = input('Input command: ')
    if command not in true_tuple:
        print('Bad parameters!')
        continue
    if command == 'exit':
        sys.exit()
    player = 1
    while True:
        user_ok = False
        draw(xo_string)  # рисует первую пустую таблицу до предпоследней.
        try:
            if command == 'start easy easy':
                count = 1
                coords = easy_ai()  # ИИ изи случайно задает пару верных координат
            
            if command == 'start medium medium':
                count = 2
                if player == 1:
                    ai_player = 1
                    coords = medium_ai()  # ИИ медиум случайно задает пару верных координат и неслучайно пару последних
                    player = 2
                elif player == 2:
                    ai_player = 2
                    coords = medium_ai() 
                    player = 1
            
            if command == 'start medium easy':
                if player == 1:
                    ai_player, count = 1, 2
                    coords = medium_ai()  # ИИ медиум случайно задает пару верных координат и неслучайно пару последних
                    player = 2
                elif player == 2:
                    count = 1
                    coords = easy_ai() 
                    player = 1

            if command == 'start easy medium':
                if player == 1:
                    count = 1
                    coords = easy_ai() 
                    player = 1
                elif player == 2:
                    ai_player, count = 1, 2
                    coords = medium_ai()  # ИИ медиум случайно задает пару верных координат и неслучайно пару последних
                    player = 2
                    
            if command == 'start user medium':
                if player == 1:
                    coords = tuple(map(int, input("Enter the coordinates: ").split()))  # юзер
                    if coords == 'exit':
                        sys.exit()
                    count = 0
                    if check_coords(coords) is False: # если координаты заняты или неверно введены
                        continue  # еще раз введите
                    player = 2
                    user_ok = True
                elif player == 2:
                    ai_player = 2
                    coords = medium_ai()  # ИИ 
                    player, count = 1, 2

            if command == 'start medium user':
                if player == 1:
                    ai_player = 1
                    coords = medium_ai()  # ИИ 
                    player, count = 2, 2
                elif player == 2:
                    coords = tuple(map(int, input("Enter the coordinates: ").split()))  # юзер
                    if coords == 'exit':
                        sys.exit()
                    count = 0
                    if check_coords(coords) is False: # если координаты заняты или неверно введены
                        continue  # еще раз введите
                    player = 1
                    user_ok = True
        
            if command == 'start easy user':  # ИИ ходит первый
                if player == 1:
                    coords = easy_ai()  # ИИ 
                    player, count = 2, 1
                elif player == 2:
                    coords = tuple(map(int, input("Enter the coordinates: ").split()))  # юзер
                    if check_coords(coords) is False:
                        continue
                    player, count = 1, 0 
                    user_ok = True
   
            if command == 'start user easy':  # юзер ходит первый
                if player == 1:
                    coords = tuple(map(int, input("Enter the coordinates: ").split()))  # юзер
                    if coords == 'exit':
                        sys.exit()
                    if check_coords(coords) is False: # если координаты заняты или неверно введены
                        continue  # еще раз введите
                    player, count = 2, 0 
                    user_ok = True
                elif player == 2:
                    coords = easy_ai()  # ИИ 
                    player, count = 1, 1

            if command == 'start user user':
                coords = tuple(map(int, input("Enter the coordinates: ").split())) # юзер
                if coords == 'exit':
                        sys.exit()


            if not user_ok:
                check_coords(coords)
                combo1, combo2, combo3 = update_combo()
            else:
                combo1, combo2, combo3 = update_combo()
        except ValueError:
            print("You should enter numbers!")
                 
        if calculate():
            xo_string = ["_" for i in range(9)]
            n = 0
            count = 0
            XO_dict = {}
            for i in range(3, 0, -1): # словарь забитый значениями по координатам от 0 до 8
                for j in range(1, 4):
                    XO_dict[(j, i)] = xo_string[n]
                    n += 1
            break
