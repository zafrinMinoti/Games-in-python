def make_turn(player, position):
    '''updates each user's turn sets''' 
    if player == player1:
        player1_turns.add(position)
    if player == player2:
        player2_turns.add(position)
    
def visualize():
    pass

def available_positions(init_set, turn_set):
    '''reurns a snipit of empty positions 
    available to a player to make a turn'''
    return init_set.difference(turn_set)

def winner(winning_sets, player_turn_set):
    '''Determine if a user's input set concains a winning combination'''
    win = False
    for winning_set in winning_sets:
        if winning_set == winning_set.intersection(player_turn_set):
            win = True
    return win
        
def winning_statement(player):
    '''prints out the winner'''
    print('\nCongratulations!!!',player.upper() + '\nYOU WON!!!')

# All the avainable positions to make turns
init_positions = set(range(1,10))

# Keep tracks of the turns each user made
player1_turns = set()
player2_turns = set()

# Take names of the players
player1 = input('Enter the name of Player 1: ')
player2 = input('Enter the name of Player 2: ')

# Combination of all winning sets
winning_sets = [{1,2,3}, {4,5,6}, {7,8,9}, 
                {1,4,7}, {2,5,8}, {3,6,9}, 
                {1,5,9}, {3,5,7}]

# Let's paly
turn = 1
positions = init_positions
while turn <= 9:
    for player, player_turn_set in zip([player1, player2], [player1_turns, player2_turns]):
        print('\nAvailable Positions:', positions)
        input_pos = int(input('{} make your turn: '.format(player)))
        if input_pos not in positions:
            print('\nThat is not a valid turn!')
            continue
        make_turn(player, input_pos)
        turn +=1
        
        if winner(winning_sets, player_turn_set):
            winning_statement(player)
            turn = 10
        positions = available_positions(positions,player_turn_set)
 
