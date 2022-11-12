# The cross-zero game
import time
import os


def field_init(field_size, empty_cell):
    field = []
    for i in range(field_size):
        field.append([empty_cell] * field_size)
    return field


def print_field(field):
    for i in range(len(field)):
        print(*field[i])


def acquaintance():
    playerX = input("Имя игрока X: ")
    player0 = input("Имя игрока 0: ")
    time.sleep(1)
    return {"X": playerX, "0": player0}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def turn(player, field, players, empty_cell):
    clear_console()
    print(players.get("X") + " играет крестиками")
    print(players.get("0") + " играет ноликами")
    print("Сейчас ходит " + player)
    print_field(field)
    while True:
        try:
            i = int(input("Введите строку: ")) - 1
        except (ValueError, UnboundLocalError):
            print("Необходимо ввести числа от 1 до 3")
            continue
        try:
            j = int(input("Введите столбец: ")) - 1
        except (ValueError, UnboundLocalError):
            print("Необходимо ввести числа от 1 до 3")
            continue
        if check_cell(i, j, field, empty_cell):
            if player == players.get("X"):
                field[i][j] = "X"
            else:
                field[i][j] = "0"
            break
    return field


def check_cell(i, j, field, empty_cell):
    allowed_list = [0, 1, 2]
    condition1 = i in allowed_list and j in allowed_list
    condition3 = i is None or j is None
    if not condition1 or condition3:
        print("Необходимо ввести числа от 1 до 3")
        return False
    condition2 = field[i][j] == empty_cell
    if not condition2:
        print("Поле уже занято")
        return False
    if condition1 and condition2:
        return True
    return False


def check_rows(field, empty_cell):
    for i in range(len(field)):
        if field[i][0] == field[i][1] == field[i][2] != empty_cell:
            return True
    return False


def check_cols(field, empty_cell):
    for j in range(len(field)):
        if field[0][j] == field[1][j] == field[2][j] != empty_cell:
            return True
    return False


def check_diagonals(field, empty_cell):
    if field[0][0] == field[1][1] == field[2][2] != empty_cell:
        return True
    elif field[0][2] == field[1][1] == field[2][0] != empty_cell:
        return True
    else:
        return False


def is_win(player, field, empty_cell):
    if check_rows(field, empty_cell) or check_cols(field, empty_cell) or check_diagonals(field, empty_cell):
        clear_console()
        print(player + " win!")
        return True
    else:
        return False


def the_game():
    empty_cell = "-"
    field_size = 3
    players = acquaintance()  # create players
    current_player = players.get("X")  # first player
    field = field_init(field_size, empty_cell)  # create field
    count = 0
    while True:
        count += 1
        field = turn(current_player, field, players, empty_cell)
        if is_win(current_player, field, empty_cell):
            print_field(field)
            break
        elif count == 9:
            clear_console()
            print("Ничья")
            print_field(field)
            break
        if current_player == players.get("X"):
            current_player = players.get("0")
        else:
            current_player = players.get("X")


the_game()
