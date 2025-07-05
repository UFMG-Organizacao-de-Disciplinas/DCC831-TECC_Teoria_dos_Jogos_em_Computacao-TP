""" Handling Players and strategies functions """


def get_players(num_players: int = 2) -> list[int]:
    """ Create a list of players based on the number of players

    Args:
        num_players (int): The number of players in the game.

    Returns:
        list: A list of player identifiers in the format 'p1', 'p2',
    """
    digits = len(str(num_players))

    player_list = [f'p{str(i+1).zfill(digits)}' for i in range(num_players)]
    return player_list


def set_player_strategies(players: list, strategies: dict) -> dict:
    """ Assign strategies to players

    Args:
        players (list): A list of player identifiers.
        strategies (dict): A dictionary where keys are player identifiers
            and values are lists of strategies available to each player.

    Returns:
        dict: A dictionary where each key is a player identifier and the value
    """
    player_strat = {player: strategies for player in players}
    return player_strat
