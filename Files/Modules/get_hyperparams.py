""" Setting up Hyperparameters for Benevolent Gaming

This module defines the global game parameters for the Benevolent Gaming scenario.
"""


def setting_up_hyperparameters(
        strat_count: dict[str, int],
        num_rounds: int = 10,
        initial_score: float = 0.0,
        participation_point: float = 1.0) -> dict[str, int]:
    """ Defining the global game parameters

    Args:
        strat_count (dict): Number of players in class per strategy.
        num_rounds (int): Number of rounds in the game.
        initial_score (int): Initial score for each player.
        participation_point (int): Points awarded for participating in the game.

    Returns:
        dict: A dictionary containing the game parameters.
            1. `strat_count`: Number of players in class per strategy.
            2. `num_rounds`: Number of rounds in the game.
            3. `initial_score`: Initial score for each player.
            4. `participation_point`: Points awarded for participating in the game.
    """

    gaming_parameters = {
        'strat_count': strat_count,
        'num_rounds': num_rounds,
        'initial_score': initial_score,
        'participation_point': participation_point,
    }

    return gaming_parameters
