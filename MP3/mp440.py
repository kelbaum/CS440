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
#Kyle
def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here 
    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
'''
#Nick, WIP
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
    
    #Propagate changes cause by move
    
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
#Kyle
def is_terminal_state(state, state_list = None):
    terminal = False
    # Your implementation goes here 
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


