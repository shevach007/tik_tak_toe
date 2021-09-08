board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
is_x_turn = True
is_valid_move = False
is_still_playing = True
def check_row(board, n):
    x_counter = 0
    o_counter = 0
    for i in range(2):
        if board[n][i] == 'x':
            x_counter += 1
            if x_counter == 2:
                print("x's won")
        

print("enter x and y coordinates (1 - 3)")
while is_still_playing:
    for raw in board:
        blank_str = ""
        for item in raw:
            blank_str += item
        print(blank_str)
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
    
    is_valid_move = False
    for n in range(2):
        check_row(board, n)











