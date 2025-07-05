""" Module for drawing unique players for games.

This module provides a function to randomly pair players for games, ensuring that
if the number of players is odd, one player is left to play alone.
It uses the `random` module to shuffle the player list and create pairs.
"""

import random


def draw_unique_players(players: list, alone_player: list | None = None) -> tuple:
    """ Function receives as input the player list, and returns the list of players
    per game ordering

    Args:
        players (list): List of players to be drawn.
        alone_player (list | None): Optional player who will play alone if
            the number of players is odd.

    Returns:
        tuple: A tuple containing:
            - player_sequence (list): A list of tuples, each containing two players
            who will play together.
            - alone_player (list | None): The player who is left alone if the number
            of players is odd.
    """

    # Making the shuffle of the players left to play in class
    players_left = players
    random.shuffle(players_left)
    player_sequence = []

    while len(players_left) >= 2:
        if alone_player:
            player01 = players_left.pop(players.index(alone_player))
            player02 = players_left.pop()
            player_sequence.append((player01, player02))

        else:
            player01 = players_left.pop()
            player02 = players_left.pop()
            player_sequence.append((player01, player02))

    if len(players_left) == 1:
        alone_player = players_left[0]

    return player_sequence, alone_player


all_players = ['Rangel', 'João', 'Hard-Enzo']
selected_players, solo_player = draw_unique_players(all_players)

print(selected_players)
print(solo_player)
