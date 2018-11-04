'''
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move.

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0.
'''
def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here
    if state[row][column] != ' ':
        # Check if location is not empty
        return 0
    # Continue getting move value
    other_player = ''
    if player == 'B':
        other_player = 'W'
    else:
        other_player = 'B'
    flip_temp = 0

    # check row ( - )
    if row == 0:
        for i in range(1, len(state)):
            if state[i][column] == other_player:
                flip_temp += 1
            elif state[i][column] == player:
                flipped += flip_temp
                break
            else:
                break
    elif 0 < row < len(state) - 1:
        for i in range(row - 1, -1, -1):
            if state[i][column] == other_player:
                flip_temp += 1
            elif state[i][column] == player:
                flipped += flip_temp
                break
            else:
                break
        flip_temp = 0
        for i in range(row + 1, len(state)):
            if state[i][column] == other_player:
                flip_temp += 1
            elif state[i][column] == player:
                flipped += flip_temp
                break
            else:
                break
    elif row + 1 == len(state):
        for i in range(row - 1, -1, -1):
            if state[i][column] == other_player:
                flip_temp += 1
            elif state[i][column] == player:
                flipped += flip_temp
                break
            else:
                break
    flip_temp = 0

    # check column ( | )
    if column == 0:
        for j in range(1, len(state[row])):
            if state[row][j] == other_player:
                flip_temp += 1
            elif state[row][j] == player:
                flipped += flip_temp
                break
            else:
                break
    elif 0 < column < len(state[row]) - 1:
        for j in range(column - 1, -1, -1):
            if state[row][j] == other_player:
                flip_temp += 1
            elif state[row][j] == player:
                flipped += flip_temp
                break
            else:
                break
        flip_temp = 0
        for j in range(column + 1, len(state)):
            if state[row][j] == other_player:
                flip_temp += 1
            elif state[row][j] == player:
                flipped += flip_temp
                break
            else:
                break
    elif column + 1 == len(state[row]):
        for j in range(column - 1, -1, -1):
            if state[row][j] == other_player:
                flip_temp += 1
            elif state[row][j] == player:
                flipped += flip_temp
                break
            else:
                break
    flip_temp = 0

    # check upper right diagonal ( / )
    if row == 0 or column == len(state[row]) - 1:
        y = column + 1
        for i in range(row + 1, y):
            if state[i][column - i] == other_player:
                flip_temp += 1
            elif state[i][column - i] == player:
                flipped += flip_temp
                break
            else:
                break
    elif row == len(state) - 1 or column == 0:
        x = row + 1
        for j in range(column + 1, x):
            if state[row - j][j] == other_player:
                flip_temp += 1
            elif state[row - j][j] == player:
                flipped += flip_temp
                break
            else:
                break
    else:
        i = row + 1
        j = column - 1
        while column != -1 or row != len(state):
            if state[i][j] == other_player:
                flip_temp += 1
                i += 1
                j -= 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break
        flip_temp = 0
        i = row - 1
        j = column + 1
        while row != -1 or column != len(state[row]):
            if state[i][j] == other_player:
                flip_temp += 1
                i -= 1
                j += 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break
    flip_temp = 0

    # check upper left diagonal ( \ )
    if row == 0 or column == 0:
        i = row + 1
        j = column + 1
        while i != len(state) and j != len(state[row]):
            if state[i][j] == other_player:
                flip_temp += 1
                i += 1
                j += 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break
    elif row == len(state) - 1 or column == len(state[row]) - 1:
        i = row - 1
        j = column - 1
        while i != -1 or j != -1:
            if state[i][j] == other_player:
                flip_temp += 1
                i -= 1
                j -= 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break
    else:
        i = row - 1
        j = column - 1
        while i != -1 and j != -1:
            if state[i][j] == other_player:
                flip_temp += 1
                i -= 1
                j -= 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break
        flip_temp = 0
        i = row + 1
        j = column + 1
        while row != len(state) or column != len(state[row]):
            if state[i][j] == other_player:
                flip_temp += 1
                i += 1
                j += 1
            elif state[i][j] == player:
                flipped += flip_temp
                break
            else:
                break

    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state.
'''
def execute_move(state, player, row, column):
    #Make new state with applicable number of rows
    #Iterate by row across state and transition

    new_state = []

    for x in range(0, len(state),1):
        new_state.append([])
        for y in range(0, len(state), 1):
            if x == row and y == column:
                new_state[x].append(player)
            else:
                new_state[x].append(state[x][y])

    #Propagate changes caused by move
    #Up
    x = row - 1
    while x >= 0:
        if new_state[x][column] == ' ':
            break
        if new_state[x][column] != player:
            x =  x - 1
            continue
        if new_state[x][column] == player:
            for change in range(row-1, x, -1):
                new_state[change][column] = player
            break

    #Down
    x = row + 1
    while x < len(state):
        if new_state[x][column] == ' ':
            break
        if new_state[x][column] != player:
            x =  x + 1
            continue
        if new_state[x][column] == player:
            for change in range(row+1, x, 1):
                new_state[change][column] = player
            break

    #Left
    y = column + 1
    while y < len(state):
        if new_state[row][y] == ' ':
            break
        if new_state[row][y] != player:
            y =  y + 1
            continue
        if new_state[row][y] == player:
            for change in range(column+1, y, 1):
                new_state[row][change] = player
            break

    #Right
    y = column - 1
    while y >= 0:
        if new_state[row][y] == ' ':
            break
        if new_state[row][y] != player:
            y =  y - 1
            continue
        if new_state[row][y] == player:
            for change in range(column-1, y, -1):
                new_state[row][change] = player
            break


    #Up Left
    x = row - 1
    y = column -1
    while x >= 0 and y >=0:
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            x = x - 1
            y = y - 1
            continue
        if new_state[x][y] == player:
            for chX,chY in zip(range(row-1, x, -1), range(column-1, y,-1)):
                new_state[chX][chY] = player
            break

    #Up Right
    x = row - 1
    y = column + 1
    while x >= 0 and y < len(state):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            x = x - 1
            y = y + 1
            continue
        if new_state[x][y] == player:
            for chX,chY in zip(range(row-1, x, -1), range(column+1, y, 1)):
                new_state[chX][chY] = player
            break

    #Down Left
    x = row + 1
    y = column -1
    while x < len(state) and y >=0:
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            x = x + 1
            y = y - 1
            continue
        if new_state[x][y] == player:
            for chX,chY in zip(range(row+1, x, 1), range(column-1, y,-1)):
                new_state[chX][chY] = player
            break

    #Down Right
    x = row + 1
    y = column + 1
    while x < len(state) and y < len(state):
        if new_state[x][y] == ' ':
            break
        if new_state[x][y] != player:
            x = x + 1
            y = y + 1
            continue
        if new_state[x][y] == player:
            for chX,chY in zip(range(row+1, x, 1), range(column+1, y, 1)):
                new_state[chX][chY] = player
            break

    return new_state

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

'''
def count_pieces(state):
    blackpieces = 0
    whitepieces = 0

    for row in state:
        for item in row:
            if item == 'B':
                blackpieces = blackpieces + 1
            elif item == 'W':
                whitepieces = whitepieces + 1
    return (blackpieces, whitepieces)

'''
Check whether a state is a terminal state.
'''
def is_terminal_state(state, state_list = None):
    terminal = False
    # Your implementation goes here
    for i in len(state):
        for j in len(state[i]):
            if state[i][j] == ' ':
                if get_move_value(state, 'B', i, j) != 0:
                    return terminal
                if get_move_value(state, 'W', i, j) != 0:
                    return terminal
    terminal = True
    return terminal

'''
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player.
'''
def minimax(state, player):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    return (value, row, column)

'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game.
'''
def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)


'''
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player.
'''
def minimax_ab(state, player, alpha = -10000000, beta = 10000000):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here 
    value = count_pieces(state)
    if (is_terminal_state(state)):
        return (value,row,column)

    moves = []
    for x in range(0,len(state),1):
            for y in range(0, len(state),1):
                if (get_move_value(state,player,x,y) != 0):
                    moves.append((x,y))

    #Max
    if player == 'B':
        for ((row,col) in moves:
            temp = max(count_pieces(state), minimax_ab(execute_move(state,player,row,col), 'W',alpha, beta))
            (v, r, c) = temp
            if v > alpha: 
                alpha = v


    #Min
    if player == 'W':
        for ((row,col) in moves:
            temp = min(count_pieces(state), minimax_ab(execute_move(state,player,row,col), 'B',alpha, beta))
            (v,r,c) = temp
            if v < beta:
                beta = v
    return (value, row, column)


'''
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
'''
def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)
