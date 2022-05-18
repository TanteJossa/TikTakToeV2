mainBoard = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

baseBoard = [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0]

boards = {'main':mainBoard,
          'boards':[
            [[['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0]],
            [[['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],],
            [[['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0],
              [['1','2','3', ], ['4','5','6', ], ['7','8','9', ], 0]]]}

def print_boards(boards):
    for i in range(3):
        print('      ' + boards['main'][i][0] + '|' + boards['main'][i][1] + '|' + boards['main'][i][2])
    
    print('')
    boardNumber = 1
    for boardsRow in range(3):
        print('  ' + str(boardNumber) + '     ' + str(boardNumber + 1) + '     ' + str(boardNumber + 2))
        boardNumber = boardNumber + 3

        for placeY in range(3):
            print(boards['boards'][boardsRow][0][placeY][0] + '|' + boards['boards'][boardsRow][0][placeY][1] + '|' + boards['boards'][boardsRow][0][placeY][2] + ' ' + 
                    boards['boards'][boardsRow][1][placeY][0] + '|' + boards['boards'][boardsRow][1][placeY][1] + '|' + boards['boards'][boardsRow][1][placeY][2] + ' ' + 
                    boards['boards'][boardsRow][2][placeY][0] + '|' + boards['boards'][boardsRow][2][placeY][1] + '|' + boards['boards'][boardsRow][2][placeY][2])
                

def place_piece(x=0, y=0, player='x', board=boards['main']):
    global playerHasPlayed
    if player == 'x':
        player = 'x'
    elif player == 'y':
        player = 'y'
    else:
        print('Incorrect player given!')
        return board

    if board[y][x] != 'x' and board[y][x] != 'y':
        board[y][x] = player
        playerHasPlayed = True

        return board
    else:
        print('Spot already has a piece!')
        return board

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False

def choose_number_to_9():
    number = input('Please input a number from 1-9?: ')
    try:
        if int(number) in range(1, 9):
            return int(number)
        else:
            print('Please input a valid number, droeftoeter!')
            return choose_number_to_9()
    except:
        return choose_number_to_9()
    

def number_to_array(number):
    if number in range(1, 9):
        if number == 1:
            array = [0, 0]
        elif number == 2:
            array = [1, 0]
        elif number == 3:
            array = [2, 0]
        elif number == 4:
            array = [0, 1]
        elif number == 5:
            array = [1, 1]
        elif number == 6:
            array = [2, 1]
        elif number == 7:
            array = [0, 2]
        elif number == 8:
            array = [1, 2]
        elif spot == 9:
            array = [2, 2]

        return array
    else:
        print('not a valid number given: number to array')
        return False

def place_piece_on_spot(spot:int, player, board):
    if spot in range(1, 9):
        movePlayed = place_piece(number_to_array(spot)[0], number_to_array(spot)[1], player, board)

    return movePlayed

hasEnded = False
player = 'x'
totalMoves = 0
print_boards(boards)

print('There are two players (x and y).  ')
print('The goal is to get three in a row in the top board. ')
print('The first player picks a board to play on and chooses a square to play his cross. ')
print('Player two has to play on the board that the other player put his cross on, snappie. ')
print('If you win a "small" game you win that square on the "main board" someone wins if he has three in a row on that board. ')

print('player ' + player.upper() +' please pick a board to play on: ')
currentBoard = choose_number_to_9()


while hasEnded == False:
    playerHasPlayed = False
    while playerHasPlayed == False:
        print_boards(boards)

        if boards['boards'][number_to_array(currentBoard)[1]][number_to_array(currentBoard)[0]][-1] == 9:
            print('That board is full, choose a new board?')
            print('player ' + player.upper() + ' please pick a board to play on: ')
            currentBoard = choose_number_to_9()


        print('Where do you want to place your piece? on board ' + str(currentBoard))
        spot = choose_number_to_9()
        boardArray = number_to_array(currentBoard)
        boards['boards'][boardArray[1]][boardArray[0]] = place_piece_on_spot(spot , player, boards['boards'][boardArray[1]][boardArray[0]])


        boards['boards'][boardArray[1]][boardArray[0]][-1] = boards['boards'][boardArray[1]][boardArray[0]][-1] + 1

        board_won = check_win(boards['boards'][boardArray[1]][boardArray[0]])

        if board_won == True:
            place_piece_on_spot(currentBoard, player, boards['main'])
            print('Well done, player ' + player.upper() + ' won a spot on the main board!')
            boards['boards'][boardArray[1]][boardArray[0]][-1] = 9

            if check_win(boards['main']):
                print('Player ' + player.upper() + ' won!!!')
                exit()

        currentBoard = spot

    if player == 'x':
        player = 'y'
    else:
        player = 'x'


