""" Handling Players and strategies functions """


def get_players(num_players):
    """ Create a list of players based on the number of players """
    digits = len(str(num_players))

    player_list = [f'p{str(i+1).zfill(digits)}' for i in range(num_players)]
    return player_list


def set_player_strategies(players, strategies):
    """ Assign strategies to players """
    return {player: strategies for player in players}
