""" Plotting Results of Games
This module provides functionality to plot the results of games played between two players.
It takes a list of game results, where each result is a dictionary containing game details
"""


def plot_games(results: list) -> None:
    """ Plot the results of the games
    Args:
        results (list): List of game results, where each result is a
        dictionary containing game details.
    Returns:
        None: This function does not return anything; it is intended to
        display the results visually.
    """
    print("Plotting game results...")
    for result in results:
        msg = f"Game: {result['game_name']}, "
        msg += "Player 1 Strategy: {result['p1_strategy']}, "
        msg += "Player 2 Strategy: {result['p2_strategy']}"
        print(msg)
        print(f"Payoffs: P1: {result['payoff_p1']}, P2: {result['payoff_p2']}")
    # Here you would typically use a plotting library like matplotlib to visualize the results.
    # For example:
    # import matplotlib.pyplot as plt
    # plt.plot(...)
    # plt.show()
