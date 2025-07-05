""" Setting the strategies functions """


def strat_reasonable_minimax(game_sequence: list, game_number: int, player: str) -> int:
    """ Function receives as input the game number and the player label,
        and returns the minimax pure strategy

    Args:
        game_sequence (list): List of games played.
        game_number (int): The index of the game in the game_sequence.
        player (str): The player label, either 'p1' or 'p2'.

    Returns:
        int: The index of the action that corresponds to the minimax strategy for the player.
    """
    payoffs = game_sequence[game_number]['payoffs'][player]

    if player == 'p1':
        max_column = []                                 # Initializing the vector as empty
        for i in range(len(payoffs[0])):
            # Taking the max value for each row in the column i
            max_value = max(row[i] for row in payoffs)
            # Appending the max values for each column
            max_column.append(max_value)

        for i in range(len(payoffs)):
            # Analyzing which row contains the minmax
            worst_case = max(row[i] for row in payoffs)
            # Testing if the i-row contains the minmax
            if worst_case == min(max_column):
                # Choosing which action defines the minmax for the player
                minmax_action = i
    else:
        # Taking the max value for each row in the column i
        max_row = [max(action) for action in payoffs]
        # Analyzing which column contains the minmax
        minmax_action = max_row.index(min(max_row))

    return minmax_action


def strat_minimax(game_sequence: list, game_number: int, player: str) -> int:
    """ Function receives as input the game number and the player label,
        and returns the minimax pure strategy

    Args:
        game_sequence (list): List of games played.
        game_number (int): The index of the game in the game_sequence.
        player (str): The player label, either 'p1' or 'p2'.

    Returns:
        int: The index of the action that corresponds to the minimax strategy for the player.
    """

    payoffs = game_sequence[game_number]['payoffs'][player]

    if player == 'p1':
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


def strat_maxmin(game_sequence, game_number, player):
    """ Function receives as input the game number and the player label,
        and returns the maxmin pure strategy

    Args:
        game_sequence (list): List of games played.
        game_number (int): The index of the game in the game_sequence.
        player (str): The player label, either 'p1' or 'p2'.

    Returns:
        int: The index of the action that corresponds to the maxmin strategy for the player.
    """

    payoffs = game_sequence[game_number]['payoffs'][player]

    if player == 'p1':
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


def strat_minimax_regret(game_sequence: list, game_number: int, player: str) -> int:
    """ Function receives as input the game number and the player label,
        and returns the minimax regret pure strategy

    Args:
        game_sequence (list): List of games played.
        game_number (int): The index of the game in the game_sequence.
        player (str): The player label, either 'p1' or 'p2'.

    Returns:
        int: The index of the action that corresponds to the minimax regret strategy for the player.
    """

    payoffs = game_sequence[game_number]['payoffs'][player]

    if player == 'p1':
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


def strat_social_welfare(game_sequence, game_number, player):
    """ Function receives as input the game number and the player label,
        and returns the social welfare pure strategy

    Args:
        game_sequence (list): List of games played.
        game_number (int): The index of the game in the game_sequence.
        player (str): The player label, either 'p1' or 'p2'.

    Returns:
        int: The index of the action that corresponds to the social welfare strategy for the player.
    """

    # Collecting the payoff matrices from both players
    if player == 'p1':
        other_player = 'p2'
    else:
        other_player = 'p1'
    payoffs_player = game_sequence[game_number]['payoffs'][player]
    payoffs_other = game_sequence[game_number]['payoffs'][other_player]

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
        dict: A dictionary containing the strategies and their respective functions.
    """

    strategies = {
        'minimax': strat_minimax,
        'maxmin': strat_maxmin,
        'minimax_regret': strat_minimax_regret,
        'social_welfare': strat_social_welfare,
    }

    return strategies
