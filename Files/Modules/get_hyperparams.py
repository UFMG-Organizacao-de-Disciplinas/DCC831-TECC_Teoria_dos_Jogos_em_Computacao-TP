""" Setting up Hyperparameters for Benevolent Gaming

This module defines the global game parameters for the Benevolent Gaming scenario.
"""


def setting_up_hyperparameters(
        num_players: int = 5,
        num_rounds: int = 10,
        initial_score: int = 0,
        participation_point: int = 1) -> dict[str, int]:
    """ Defining the global game parameters

    Args:
        players_num (int): Number of players in the game.
        rounds_num (int): Number of rounds in the game.
        initial_score (int): Initial score for each player.
        participation_point (int): Points awarded for participating in the game.

    Returns:
        dict: A dictionary containing the game parameters.
            1. `players_num`: Number of players in the game.
            2. `rounds_num`: Number of rounds in the game.
            3. `initial_score`: Initial score for each player.
            4. `participation_point`: Points awarded for participating in the game.
    """

    gaming_parameters = {
        'num_players': num_players,
        'num_rounds': num_rounds,
        'initial_score': initial_score,
        'participation_point': participation_point,
    }

    return gaming_parameters
