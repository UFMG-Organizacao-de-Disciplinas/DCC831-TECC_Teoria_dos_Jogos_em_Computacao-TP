""" Setting up Hyperparameters for Benevolent Gaming

This module defines the global game parameters for the Benevolent Gaming scenario.
"""


def setting_up_hyperparameters(players_num: int = 5, rounds_num: int = 10,
                               initial_score: int = 0, participation_point: int = 1) -> dict:
    """ Defining the global game parameters

    Args:
        players_num (int): Number of players in the game.
        rounds_num (int): Number of rounds in the game.
        initial_score (int): Initial score for each player.
        participation_point (int): Points awarded for participating in the game.

    Returns:
        dict: A dictionary containing the game parameters.
    """

    gaming_parameters = {
        'num_players': players_num,
        'num_rounds': rounds_num,
        'initial_score': initial_score,
        'participation_point': participation_point,
    }

    return gaming_parameters
