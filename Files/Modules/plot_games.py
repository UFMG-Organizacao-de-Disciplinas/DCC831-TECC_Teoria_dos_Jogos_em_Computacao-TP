""" Running games and plotting results """


import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def preprocess_data(
        games,
        players: dict[int, str],
        results: list[dict[int, float]],
        hyperparams: dict[str, int | dict[str, int]]) -> pd.DataFrame:
    """ Converts the results of the games into a Pandas DataFrame of their accumulated scores.
    Args:
        games (dict): Dictionary containing game names and their details.
        players (dict[int, str]): Dictionary mapping player IDs to their strategies.
        results (list[dict[int, float]]): List of game results, where each result
            is a dictionary containing player IDs and their scores.
        hyperparams (dict[str, int | dict[str, int]]): Dictionary containing hyperparameters

    Returns:
        pd.DataFrame: A DataFrame with the accumulated scores of players across games.
    """

    pd.set_option('display.expand_frame_repr', False)

    rows_size = min(len(results), len(games)) + 1  # +1 for the initial row

    # Create an zeroed DataFrame
    headers = list(players.keys())
    df = pd.DataFrame(0.0, columns=headers, index=range(rows_size))

    # Fill first row with initial values
    df.loc[0, headers] = [hyperparams['initial_score']] * len(headers)
    # print(df)

    # Distribute the results across the DataFrame
    for i, game_result in enumerate(results, 1):
        # print(i, game_result)
        for player_id, score in game_result.items():
            new_score = score + hyperparams['participation_point']
            # print(new_score)
            df.at[i, player_id] = new_score
    # print(df)

    # Sum the accumulated values for each player, only if the columns are numeric
    df = df.cumsum()

    # print(df)

    # Adding the games column
    games_column = list(games.keys())[:rows_size-1]
    df.insert(0, 'game', ['initial scores'] + games_column)
    # print(df)

    return df


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


def plot_gamepoints_line_graph_progression(
        pre_processed_dataframe: pd.DataFrame,
        players: dict[int, str],
        strategies: list[str]
) -> None:
    """
    Desejo fazer um gráfico em python onde vários jogadores com estratégias
    diferentes vão ganhando pontos ao longo do tempo.
    Cada jogador tem uma estratégia diferente, e os jogadores com mesma
    estratégia devem estar coloridos com a mesma cor.
    """

    # print(pre_processed_dataframe)
    # print(100*"-")
    # print(players)

    # print(len(pre_processed_dataframe))
    # X should vary from 0 to the quantity of games + 1 (initial row); X labels should be the game names
    # get all the game names at the df rows
    x_game_labels = pre_processed_dataframe['game'].values

    # The stacked data should be the game points for each player in the dataframe
    numeric_df = pre_processed_dataframe.drop(columns='game')
    y_payoffs = numeric_df.T.values

    # Coloring
    player_ids = players.keys()

    strategy_palette_map = {}
    colors = [
        'Accent', 'Blues', 'Grays', 'Greens', 'Oranges', 'Purples',
        'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'cividis',
        'cividis_r', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag',
        'gist_earth', 'gist_gray', 'gist_grey', 'gist_heat', 'gist_ncar',
        'gist_stern', 'gist_yarg', 'gist_yerg', 'gnuplot',
        'gnuplot2', 'gray', 'grey', 'hot', 'hsv', 'inferno',
        'jet', 'magma', 'managua', 'nipy_spectral', 'ocean',
        'pink', 'plasma', 'prism', 'rainbow', 'seismic', 'spring',
        'summer', 'tab10', 'tab20', 'tab20b', 'tab20c', 'terrain',
        'turbo', 'twilight', 'twilight_shifted', 'vanimo', 'viridis', 'winter'
    ]
    for strategy in strategies:
        strategy_palette_map[strategy] = colors.pop(0)
        # Pop the first color from the list

    player_colors = generate_strategy_colors(players, strategy_palette_map)
    color_list = [player_colors[pid] for pid in player_ids]

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots(figsize=(10, 6))

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

    # Estética
    ax.legend(loc='upper left')
    plt.xticks(rotation=45, ha='right')  # <-- rotaciona os nomes dos jogos
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
        plot_gamepoints_line_graph_progression(
            pre_processed_dataframe, players, strategies)
