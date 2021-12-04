from os import system, name


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def welcome_print():
    print("-----------------------------------------")
    print("Добро пожаловать в игру 'Крестики-нолики'")
    print("-----------------------------------------")
    print()


def draw_matrix(matrix):
    for i in range(4):
        print(str.join('\t', matrix[i]))
    print()


def make_a_move(current_player):
    row = input_data(f"Игрок {current_player}, сделайте ход. Укажите строку: ")
    col = input_data(f"Теперь укажите столбец: ")
    return row, col


def input_data(message):
    while True:
        try:
            input_value = int(input(message))
            if input_value > 3 or input_value < 1:
                print("Укажите число от 1 до 3.")
            else:
                return input_value
        except ValueError:
            print("Укажите число от 1 до 3.")


def switch_player(current_player):
    if current_player == 'x':
        return 'y'
    return 'x'


def calculate(row, col, matrix, symbol):
    win_arr = [symbol for _ in range(3)]
    # проверка по строке
    if matrix[row] == win_arr:
        return True
    # проверка по столбцу
    if [i[col] for i in matrix] == win_arr:
        return True
    if row == col:
        # главная диагональ
        if primary_diagonal(win_arr, matrix):
            return True
        if row == 1:
            # побочная диагональ
            return secondary_diagonal(win_arr, matrix)
    if abs(row - col) == 2:
        # побочная диагональ
        return secondary_diagonal(win_arr, matrix)
    return False


def primary_diagonal(win_arr, matrix):
    return [row[i] for i, row in enumerate(matrix)] == win_arr


def secondary_diagonal(win_arr, matrix):
    return [row[-i-1] for i, row in enumerate(matrix)] == win_arr


def game_loop():
    template_matrix = [
        ['', '1', '2', '3'],
        ['1', '', '', ''],
        ['2', '', '', ''],
        ['3', '', '', ''],
    ]
    moves = list()
    move_number = 1
    current_player = 'x'
    win_flag, draw_flag = False, False
    while True:
        clear_screen()
        welcome_print()
        draw_matrix(template_matrix)
        for move_record in moves:
            print(move_record)
        if win_flag:
            print(f"\nИгра окончена. Победил игрок '{current_player}'")
            break
        if draw_flag:
            print(f"\nИгра окончена. Ничья!")
            break
        while True:
            # if move_number == 8: do it
            move = make_a_move(current_player)
            if template_matrix[move[0]][move[1]] == '':
                moves.append(f"Ход номер {move_number}: игрок {current_player} походил {move[0]} : {move[1]}")
                template_matrix[move[0]][move[1]] = current_player
                if move_number > 4:
                    matrix = [x[1:4] for x in template_matrix[1:4]]
                    if calculate(move[0] - 1, move[1] - 1, matrix, current_player):
                        win_flag = True
                        break
                if move_number == 9:
                    draw_flag = True
                    break
                current_player = switch_player(current_player)
                move_number += 1
                break
            else:
                print("В указанном поле уже есть значение! Попробуйте ещё раз :)")


game_loop()
