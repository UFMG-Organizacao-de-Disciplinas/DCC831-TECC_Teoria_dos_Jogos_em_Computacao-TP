""" Auxiliary functions for processing game data and results. """

# import numpy as np
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
