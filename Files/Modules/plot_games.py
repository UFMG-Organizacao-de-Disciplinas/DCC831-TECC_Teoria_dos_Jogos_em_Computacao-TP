""" Running games and plotting results """

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from .gaming_math import preprocess_data


def get_colors() -> list[str]:
    """ Returns a list of color names from matplotlib colormaps.

    Returns:
        colors (list[str]): A list of color names that can be used for plotting.
    """
    colors = [
        'Blues',
        'Grays',
        'Greens',
        'Greys',
        'Oranges',
        'Purples',
        'Reds',
        'cividis',
        'viridis',
        'Accent',
        'Spectral',
        'Spectral_r',
        'Wistia',
        'Wistia_r',
        'cividis_r',
        'cool',
        'coolwarm',
        'copper',
        'cubehelix',
        'flag',
        'gist_earth',
        'gist_gray',
        'gist_grey',
        'gist_heat',
        'gist_ncar',
        'gist_stern',
        'gist_yarg',
        'gist_yerg',
        'gnuplot',
        'gnuplot2',
        'gray',
        'grey',
        'hot',
        'hsv',
        'inferno',
        'jet',
        'magma',
        'managua',
        'nipy_spectral',
        'ocean',
        'pink',
        'plasma',
        'prism',
        'rainbow',
        'seismic',
        'spring',
        'summer',
        'tab10',
        'tab20',
        'tab20b',
        'tab20c',
        'terrain',
        'turbo',
        'twilight',
        'twilight_shifted',
        'vanimo',
        'winter'
    ]
    return colors


def generate_strategy_colors(
    players: dict[int, str],
    strategy_palette_map: dict[str, str]
) -> dict[int, str]:
    """ Generates a color map for players based on their strategies.

    Args:
        players (dict[int, str]): Dictionary mapping player IDs to their strategies.
        strategy_palette_map (dict[str, str]): Dictionary mapping strategies to matplotlib
            colormaps.

    Returns:
        dict[int, str]: A dictionary mapping player IDs to their corresponding colors.
    """

    # Group players by their strategies
    grouped = {}
    for player_id, strategy in players.items():
        if strategy not in grouped:
            grouped[strategy] = []
        grouped[strategy].append(player_id)

    color_map = {}
    for strategy, player_ids in grouped.items():
        base_cmap = plt.colormaps[strategy_palette_map[strategy]]

        # Avoids very light tones: uses a range from 0.3 to 1.0
        color_positions = np.linspace(0.3, 1.0, len(player_ids))

        for i, pid in enumerate(player_ids):
            rgb = base_cmap(color_positions[i])
            color_map[pid] = mcolors.to_hex(rgb)

    return color_map


def plot_gamepoints_stackline_graph_progression(
        pre_processed_dataframe: pd.DataFrame,
        players: dict[int, str],
        strategies: list[str]
) -> None:
    """ Plot the game points progression as a stacked line graph.
    Args:
        pre_processed_dataframe (pd.DataFrame): DataFrame containing game points data.
        players (dict[int, str]): Dictionary mapping player IDs to their strategies.
        strategies (list[str]): List of strategies used by the players.
    Returns:
        None: This function does not return anything; it is intended to
            display the results visually.
    """

    # print(len(pre_processed_dataframe))
    # X labels should be the game names
    # get all the game names at the df rows
    x_game_labels = pre_processed_dataframe['game'].values

    # The stacked data should be the game points for each player in the dataframe
    numeric_df = pre_processed_dataframe.drop(columns='game')
    y_payoffs = numeric_df.T.values

    # Coloring
    player_ids = players.keys()

    strategy_palette_map = {}
    colors = get_colors()  # Get a list of colors from the colormaps
    for strategy in strategies:
        strategy_palette_map[strategy] = colors.pop(0)
        # Pop the first color from the list

    player_colors = generate_strategy_colors(players, strategy_palette_map)
    color_list = [player_colors[pid] for pid in player_ids]

    plt.style.use('_mpl-gallery')
    _, ax = plt.subplots(figsize=(10, 6))

    x_labeless = np.arange(len(x_game_labels))  # X values for the x-axis
    ax.stackplot(x_labeless, y_payoffs, colors=color_list, labels=[
                 f'{pid}: {players[pid]}' for pid in player_ids])

    ax.set(
        title='Game Points Progression',
        xlabel='Games',
        xlim=(x_labeless[0], x_labeless[-1]),
        xticks=x_labeless,
        xticklabels=x_game_labels,

        ylim=(0, np.max(y_payoffs.sum(axis=0)) + 1),
        # yticks=np.arange(0, np.max(y_payoffs.sum(axis=0)) + 2)
        ylabel='Game Points',
    )

    # Styling
    ax.legend(loc='upper left')
    plt.xticks(rotation=45, ha='right')  # Rotates the game names
    plt.tight_layout()

    plt.show()


def plot_gamepoints_line_graph_progression(
        pre_processed_dataframe: pd.DataFrame,
        players: dict[int, str],
        strategies: list[str]
) -> None:
    """ Plot the game points progression as a line graph.
    Args:
        pre_processed_dataframe (pd.DataFrame): DataFrame containing game points data.
        players (dict[int, str]): Dictionary mapping player IDs to their strategies.
        strategies (list[str]): List of strategies used by the players.
    Returns:
        None: This function does not return anything; it is intended to
            display the results visually.
    """

    x_labels = pre_processed_dataframe['game'].values
    numeric_df = pre_processed_dataframe.drop(columns='game')
    player_ids = list(map(int, numeric_df.columns))
    y_data = numeric_df.values.T

    colors = get_colors()
    strat_palette = {s: colors.pop(0) for s in strategies}
    player_colors = generate_strategy_colors(players, strat_palette)
    color_list = [player_colors[pid] for pid in player_ids]
    labels = [f'{pid}: {players[pid]}' for pid in player_ids]

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(x_labels))

    for i, y in enumerate(y_data):
        ax.plot(x, y, label=labels[i], color=color_list[i])

    ax.set(title='Game Points Progression', xlabel='Games', ylabel='Game Points',
           xlim=(x[0], x[-1]), xticks=x, xticklabels=x_labels,
           ylim=(0, np.max(y_data) + 1))

    plt.xticks(rotation=45, ha='right')
    ax.legend(loc='best', fontsize='small', ncol=2)
    plt.tight_layout()
    plt.show()


def plot_games(
    games,
    players: dict[int, str],
    results: list[list[dict[int, float]]],
    hyperparams: dict[str, int | dict[str, int]],
    strategies: list[str],
) -> None:
    """ Plot the results of the games

    Args:
        results (list): List of game results, where each result is a
            dictionary containing game details.

    Returns:
        None: This function does not return anything; it is intended to
            display the results visually.
    """
    for gen_result in results:
        pre_processed_dataframe = preprocess_data(
            games, players, gen_result, hyperparams)
        plot_gamepoints_stackline_graph_progression(
            pre_processed_dataframe, players, strategies)
        # plot_gamepoints_line_graph_progression(
        #     pre_processed_dataframe, players, strategies)
