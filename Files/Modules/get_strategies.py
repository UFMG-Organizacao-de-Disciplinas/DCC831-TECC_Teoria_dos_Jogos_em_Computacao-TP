""" Setting the strategies functions """

from Files.Modules.get_payoffs import get_payoffs


def strat_minimax(game_name: str, player: int) -> int:
    """ Function receives as input the game name and the player label,
        and returns the minimax pure strategy

    Args:
        game_name (str): Name of the game played.
        player (str): The player label, either 1 or 2.

    Returns:
        int: The index of the action that corresponds to the minimax strategy for the player.
    """

    # Fix the get_payoffs kinda over typed return
    payoffs = get_payoffs(game_name)[player]

    if player == 1:
        # Initializing the vector as empty
        max_column = []

        # Taking the max value from each column i and creating a vector of max per column
        for i in range(len(payoffs[0])):
            max_value = max(row[i] for row in payoffs)
            max_column.append(max_value)

        # Analyzing which action contains the minimax payoff
        for i in range(len(payoffs)):
            worst_case = max(row[i] for row in payoffs)
            if worst_case == min(max_column):
                minmax_action = i
    else:
        # Analyzing which action contains the minimax payoff (p2)
        max_row = [max(action) for action in payoffs]
        minmax_action = max_row.index(min(max_row))

    return minmax_action


def strat_maxmin(game_name: str, player: int) -> int:
    """ Function receives as input the game name and the player label,
        and returns the maxmin pure strategy

    Args:
        game_name (str): Name of the game played.
        player (str): The player label, either 1 or 2.

    Returns:
        int: The index of the action that corresponds to the maxmin strategy for the player.
    """

    payoffs = get_payoffs(game_name)[player]

    if player == 1:
        # Analyzing which action contains the maxmin payoff
        min_row = [min(action) for action in payoffs]
        maxmin_action = min_row.index(max(min_row))

    else:
       # Initializing the vector as empty
        min_column = []

        # Taking the min value from each column i and creating a vector of min per column
        for i in range(len(payoffs[0])):
            min_value = min(row[i] for row in payoffs)
            min_column.append(min_value)

        # Analyzing which action contains the maxmin payoff (p2)
        for i in range(len(payoffs)):
            worst_case = min(row[i] for row in payoffs)
            if worst_case == max(min_column):
                maxmin_action = i

    return maxmin_action


def strat_minimax_regret(game_name: str, player: int) -> int:
    """ Function receives as input the game name and the player label,
        and returns the minimax regret pure strategy

    Args:
        game_name (str): Name of the game played.
        player (str): The player label, either 1 or 2.

    Returns:
        int: The index of the action that corresponds to the minimax regret strategy for the player.
    """

    payoffs = get_payoffs(game_name)[player]

    if player == 1:
        # Initializing the vectors as empty
        max_column = []
        regret_matrix = []

        # Taking the max value from each column i and creating a vector of max per column
        for i in range(len(payoffs[0])):
            max_value = max(row[i] for row in payoffs)
            max_column.append(max_value)

        # Creating the regret matrix
        regret_matrix = [[max_column[i] - row[i]
                          for i in range(len(row))] for row in payoffs]

        # Analyzing which action minimizes the regret
        max_regret = [max(action) for action in regret_matrix]
        minimax_regret_action = max_regret.index(min(max_regret))

    return minimax_regret_action


def strat_social_welfare(game_name: str, player: int) -> int:
    """ Function receives as input the game number and the player label,
        and returns the social welfare pure strategy

    Args:
        game_name (str): Name of the game played.
        player (str): The player label, either 1 or 2.

    Returns:
        int: The index of the action that corresponds to the social welfare strategy for the player.
    """

    # Collecting the payoff matrices from both players
    if player == 1:
        other_player = 2
    else:
        other_player = 1
    payoffs_player = get_payoffs(game_name)[player]
    payoffs_other = get_payoffs(game_name)[other_player]

    # Calculating the social welfare for each possible outcome
    social_welfare_matrix = [[payoffs_player[i][j] + payoffs_other[i][j] for j in range(len(payoffs_player[0]))]
                             for i in range(len(payoffs_player))]

    # Taking the player's action as the highest social welfare one
    social_welfare_action = social_welfare_matrix.index(
        max(social_welfare_matrix))

    return social_welfare_action


def get_strategies() -> dict:
    """ Get the strategies available for the games.

    Returns:
        strategies (dict): A dictionary containing the strategies and their respective functions.
    """

    strategies = {
        'minimax': strat_minimax,
        'maxmin': strat_maxmin,
        'minimax_regret': strat_minimax_regret,
        'social_welfare': strat_social_welfare,
    }

    return strategies
