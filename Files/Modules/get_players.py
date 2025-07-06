""" Handling Players and strategies functions """


def get_players(strat_count: dict[str, int]) -> dict[int, str]:
    """ Create a list of players based on the number of players per strategy.

    Args:
        strat_count (dict[str, int]): The strategies and how many players have this strat

    Returns:
        players_strat_dict (dict[int, str]): A dict of all the players and their strategies names
    """

    strategies = []
    for strategy in strat_count:
        quantity = strat_count[strategy]
        strategies += [strategy] * quantity

    players_strat_dict = {}

    for i, strategy in enumerate(strategies):
        players_strat_dict[i+1] = strategy

    return players_strat_dict


# print(get_players({'minimax': 2, 'maxmin': 3, 'minimax_regret': 4, 'social_welfare': 5}))
