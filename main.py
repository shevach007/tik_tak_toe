board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
is_x_turn = True
is_valid_move = False
is_still_playing = True


def if_raw(board):
    x_won = False
    o_won = False
    for i in range(len(board)):
        x_counter = ''
        o_counter = ''
        for n in range(len(board)):
            if board[i][n] == 'x':
                x_counter += 'x'
            elif board[i][n] == 'o':
                o_counter += 'o'
        if x_counter == 'xxx':
            x_won = True
        elif o_counter == 'ooo':
            o_won = True
    return o_won, x_won


def if_column(board):
    x_won = False
    o_won = False
    for i in range(len(board)):
        x_counter = ''
        o_counter = ''
        for n in range(len(board)):
            if board[n][i] == 'x':
                x_counter += 'x'
            elif board[n][i] == 'o':
                o_counter += 'o'
        if x_counter == 'xxx':
            x_won = True
            print("2")
        elif o_counter == 'ooo':
            o_won = True
    return o_won, x_won


def if_diagonal(board):
    x_won = False
    o_won = False
    if (board[0][0] and board[1][1] and board[2][2] == 'x') or (board[0][2] and board[1][1] and board[2][0] == 'x'):
        x_won = True
    elif(board[0][0] and board[1][1] and board[2][2] == 'x') or (board[0][2] and board[1][1] and board[2][0] == 'o'):
        o_won = True
    return o_won, x_won


def print_board(board):
    for raw in board:
        blank_str = ""
        for item in raw:
            blank_str += item
        print(blank_str)


print("enter x and y coordinates (1 - 3)")
while is_still_playing:
    print_board(board)
    if is_x_turn:
        print("it's x's turn")
    else:
        print("it's o's turn")

    while not is_valid_move:
        move_x = int(input("x coordinate: >")) - 1
        move_y = int(input("y coordinate: >")) - 1
        if board[move_y][move_x] != "_":
            print("spot already taken")
            is_valid_move = False
        else:
            is_valid_move = True
    if is_x_turn:
        board[move_y][move_x] = "x"
        is_x_turn = False
    else:
        board[move_y][move_x] = "o"
        is_x_turn = True
    o_won_row, x_won_row = if_raw(board)
    o_won_column, x_won_column = if_column(board)
    o_won_diagonal, x_won_diagonal = if_diagonal(board)

    if o_won_column or o_won_row or o_won_diagonal:
        print("o won")
        print_board(board)
        break

    elif x_won_row or x_won_column or x_won_diagonal:
        print("x won")
        print_board(board)
        break

    is_valid_move = False




