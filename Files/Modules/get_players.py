""" Handling Players and strategies functions """


def get_players(strat_count):
    """ Create a list of players based on the number of players per strategy.

    Args:
        strat_count (dict): The number of players per strategy.

    Returns:
        list: A list of player identifiers in the format 'p1', 'p2',
    """
    import random

    # Initializing some variables
    num_players = 0
    num_strategy = 0
    cummulative_players = []
    player_strat = {}
    players = []
 
    # Creating a list of players based on the number of players per strategy
    for count in list(strat_count.values()):
        num_players += count
        cummulative_players.append(num_players)
    players = [i for i in range(1, num_players + 1)]

    # Assigning strategies to players based on the cumulative counts
    for i in range(1, num_players + 1):
        if i > cummulative_players[num_strategy]:
            num_strategy += 1
        player_strat[i] = list(strat_count.keys())[num_strategy]
    
    # Randomizing the order of strategies for players
    values = list(player_strat.values())
    random.shuffle(values)
    players = dict(zip(player_strat.keys(), values))
    
    return players

