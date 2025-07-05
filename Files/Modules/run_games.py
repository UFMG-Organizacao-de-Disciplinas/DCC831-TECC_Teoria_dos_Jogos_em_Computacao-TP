""" Module for drawing unique players for games.

This module provides a function to randomly pair players for games, ensuring that
if the number of players is odd, one player is left to play alone.
It uses the `random` module to shuffle the player list and create pairs.
"""

def draw_unique_players(players: list, alone_player: list | None = None) -> list:
    """ Function receives as input the player list, and returns the list of players
    per game ordering

    Args:
        players (list): List of players to be drawn.
        alone_player (list | None): Optional player who will stay for next round if
            the number of players is odd.

    Returns:
        player_sequence (list): List with a tuple of the players drawn.
        alone_player (list | None): Optional player who will stay for next round if
            the number of players is odd.
    """

    import random

    # Copying the players list so it will not be modified
    players_left = players.copy()
    # Shuffling the players_left list to be drawn
    random.shuffle(players_left)
    # Defining as empty the player sequence
    player_sequence = []

    # Draw considering the player left behind in the i-1 round  
    if alone_player is not None and alone_player in players_left:
        players_left.remove(alone_player)
        player01 = alone_player
        player02 = players_left.pop()
        player_sequence.append((player01, player02))

    # Draw considering the normal case when there are more than 2 player left
    while len(players_left) >= 2:
        player01 = players_left.pop()
        player02 = players_left.pop()
        player_sequence.append((player01, player02))

    # Special case when there is one player left to be the first priority on the next round
    if len(players_left) == 1:
        alone_player = players_left[0]
    else:
        alone_player = None

    return player_sequence, alone_player






def lets_play_the_game(player_sequence,strategies,game_name):

  # Assigning the label of each player to p1 and p2
  p1 = player_sequence[0][0]
  p2 = player_sequence[0][1]


  #Run of the game for player 1 based on his strategy
  action_1 = get_strategies()[strategies[p1]](game_name, 1)

  #Run of the game for player 2 based on his strategy
  action_2 = get_strategies()[strategies[p2]](game_name, 2)

  #Payoff for player 1 at (action_1, action_2) profile
  payoff_1 = get_payoffs(game_name)[1][action_1][action_2]

  #Run of the game for player 2 based on his strategy
  payoff_2 = get_payoffs(game_name)[2][action_1][action_2]

  return payoff_1, payoff_2







# Testing of the game (not necessarily in the final module)
game_name = 'prisoners_dilemma'
num_games = 1
players = ['Rangel', 'João']
strategies = {players[0]: 'maxmin', players[1]: 'maxmin'}

# Testing of the game (not necessarily in the final module)
#for i in range(num_games):
player_sequence, alone_player = draw_unique_players(players, alone_player)
game = get_payoffs(game_name)
Payoff_1, Payoff_2 = lets_play_the_game(player_sequence,strategies,game_name)
print(f"Round {i+1}:")
print("Player sequence:", player_sequence)
print("Game played: ", game_name)
print("Payoff for player 1: ", Payoff_1)
print("Payoff for player 2: ", Payoff_2)
print("Player left to the next round:", alone_player)
print()


