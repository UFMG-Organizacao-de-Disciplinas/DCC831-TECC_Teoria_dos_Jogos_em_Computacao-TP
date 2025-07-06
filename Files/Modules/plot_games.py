""" Plotting Results of Games
This module provides functionality to plot the results of games played between two players.
It takes a list of game results, where each result is a dictionary containing game details
"""


from .get_payoffs import get_payoffs

import matplotlib.pyplot as plt
import numpy as np


def plot_gamepoints_line_graph_progression(plotting_data):
    """
    Desejo fazer um gráfico em python onde vários jogadores com estratégias
    diferentes vão ganhando pontos ao longo do tempo.
    Cada jogador tem uma estratégia diferente, e os jogadores com mesma
    estratégia devem estar coloridos com a mesma cor.
    """
    games = plotting_data['games']
    strategies = plotting_data['strategies']
    players = plotting_data['players']
    results = plotting_data['results']

    def data_preprocess(players, results):
        """ WIP """

    plt.style.use('_mpl-gallery')

    # make data
    x = np.arange(0, 10, 2)
    ay = [1, 1.25, 2, 2.75, 3]
    by = [1, 1, 1, 1, 1]
    cy = [2, 1, 2, 1, 2]
    y = np.vstack([ay, by, cy])

    # plot
    fig, ax = plt.subplots()

    ax.stackplot(x, y)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


def plot_games(games=None, strategies=None, players: list[tuple[int, int]] = None, results: list[tuple[int, int]] = None) -> None:
    """ Plot the results of the games

    Args:
        results (list): List of game results, where each result is a
            dictionary containing game details.

    Returns:
        None: This function does not return anything; it is intended to
            display the results visually.
    """
    default_players = [(1, 2), (3, 4), (5, 6), (7, 8),
                       (8, 7), (6, 5), (4, 3), (2, 1)]
    default_results = [(0, 1), (2, 1), (3, 4), (5, 4),
                       (4, 3), (2, 1), (1, 0), (0, 1)]
    default_strategies = {
        1: 'minimax_regret',
        2: 'maxmin',
        3: 'maxmin',
        4: 'maxmin',
        5: 'minimax',
        6: 'social_welfare',
        7: 'minimax',
        8: 'minimax_regret',
        # 9: 'social_welfare',
        # 10: 'minimax_regret',
        # 11: 'social_welfare',
        # 12: 'social_welfare',
        # 13: 'social_welfare',
        # 14: 'minimax_regret'
    }
    default_game_names = get_payoffs().keys()

    plotting_data = {
        'players': players if players else default_players,
        'results': results if results else default_results,
        'strategies': strategies if strategies else default_strategies,
        'games': games if games else default_game_names
    }

    plot_gamepoints_line_graph_progression(plotting_data)


# plot_games()
