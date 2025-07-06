""" Module for drawing unique players for games.

This module provides a function to randomly pair players for games, ensuring that
if the number of players is odd, one player is left to play alone.
It uses the `random` module to shuffle the player list and create pairs.
"""

from .get_payoffs import get_payoffs
from .get_players import get_players
from .get_strategies import get_strategies

def draw_unique_players(strat_count: dict, alone_player: list[str] | None = None) -> list:
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
    players_left = list(get_players(strat_count).keys()).copy()
    # Shuffling the players_left list to be drawn
    random.shuffle(players_left)
    # Defining as empty the player sequence
    player_sequence = []

    # Draw considering the player left behind in the i-1 round
    if alone_player in players_left:
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


def lets_play_the_game(strat_count) -> tuple[int, int]:
    """ Function that runs the game for the players in the player_sequence
    Args:
        player_sequence (list): List of tuples with the players to play the game.
        strategies (dict): Dictionary with the strategies of each player.
        game_name (str): Name of the game to be played.
    Returns:
        tuple: Payoffs for player 1 and player 2.
    """
    players = get_players(strat_count)
    alone_player = None
    (player_sequence, alone_player) = draw_unique_players(strat_count, alone_player)
    
    num_games = min(len(get_payoffs()), len(player_sequence))
    
    print(f'Class composition: {max(list(players.keys()))} students')
    print()
    for i, key in enumerate(strat_count):
        total_players = sum(strat_count.values())
        print(f'{key}: {strat_count[key]} players, approximately {strat_count[key] / total_players * 100:.2f}% of the class')
    print('-' * 40)
    for i in range(num_games):
        
        game_name = list(get_payoffs().keys())[i]
        
        # Assigning the label of each player to p1 and p2
        p1 = player_sequence[i][0]
        p2 = player_sequence[i][1]

        # Run of the game for the players based on their strategies
        action_1 = get_strategies()[players[p1]](game_name, 1)
        action_2 = get_strategies()[players[p2]](game_name, 2)

        # Payoffs for the players at (action_1, action_2) profile
        payoff_1 = get_payoffs(game_name)[1][action_1][action_2]
        payoff_2 = get_payoffs(game_name)[2][action_1][action_2]
        
        # Print the results of the game
        print(f'Game {i + 1}: {game_name}')
        print(f'Players: {p1} vs {p2}')
        print(f'Actions: {p1} -> {action_1}, {p2} -> {action_2}')
        print(f'Payoffs: {p1} -> {payoff_1}, {p2} -> {payoff_2}')
        print('-' * 40)
        if i == len(get_payoffs()) - 1 and alone_player is not None:
            print(f'Player left behind: {alone_player}')
            
        
    return (payoff_1, payoff_2)