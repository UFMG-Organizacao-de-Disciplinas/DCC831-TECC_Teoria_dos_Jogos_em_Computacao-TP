""" Module for drawing unique players for games.

This module provides a function to randomly pair players for games, ensuring that
if the number of players is odd, one player is left to play alone.
It uses the `random` module to shuffle the player list and create pairs.
"""

from Modules.get_payoffs import get_payoffs
from Modules.get_players import get_players
from Modules.get_strategies import get_strategies


def draw_unique_players(hyperparams: dict, gen: int, alone_player: list[str] | None = None) -> list:
    """ Function receives as input the player list, and returns the list of players
    per game ordering

    Args:
        players (list): List of players to be drawn.
        alone_player (list | None): Optional player who will stay for next round if
            the number of players is odd.

    Returns:
        player_sequence (list): List with a tuple of the players drawn.
        alone_player (list | None): Optional player who will stay for next round if
            the number of players is odd.
    """

    import random

    random.seed(gen)  # For reproducibility, can be removed in production
    # Copying the players list so it will not be modified
    players_left = list(get_players(hyperparams).keys()).copy()
    # Shuffling the players_left list to be drawn
    random.shuffle(players_left)
    # Defining as empty the player sequence
    player_sequence = []

    # Draw considering the player left behind in the i-1 round
    if alone_player in players_left:
        players_left.remove(alone_player)
        player01 = alone_player
        player02 = players_left.pop()
        player_sequence.append((player01, player02))

    # Draw considering the normal case when there are more than 2 player left
    while len(players_left) >= 2:
        player01 = players_left.pop()
        player02 = players_left.pop()
        player_sequence.append((player01, player02))

    # Special case when there is one player left to be the first priority on the next round
    if len(players_left) == 1:
        alone_player = players_left[0]
    else:
        alone_player = None

    return player_sequence, alone_player


def lets_play_the_game(hyperparams: dict, gen: int) -> tuple[int, int]:
    """ Function that runs the game for the players in the player_sequence
    Args:
        player_sequence (list): List of tuples with the players to play the game.
        strategies (dict): Dictionary with the strategies of each player.
        game_name (str): Name of the game to be played.
    Returns:
        tuple: Payoffs for player 1 and player 2.
    """
    players = get_players(hyperparams)
    alone_player = None
    payoff_summary = []

    (player_sequence, alone_player) = draw_unique_players(hyperparams, alone_player)

    num_games = min(len(get_payoffs()), len(player_sequence))

    class_composition = f'Class composition: {max(list(players.keys()))} students\n'

    for i, key in enumerate(hyperparams):
        total_players = sum(hyperparams.values())
        percentage_players = hyperparams[key] / total_players * 100
        player_strat_msg = f'{key}:\t{hyperparams[key]} players, '
        percentage_msg = f'approximately {percentage_players:.2f}% of the class\n'
        class_composition += '\t' + player_strat_msg + percentage_msg

    class_composition += '-' * 40
    print(class_composition)

    for i in range(num_games):

        game_name = list(get_payoffs().keys())[i]

        # Assigning the label of each player to p1 and p2
        p1 = player_sequence[i][0]
        p2 = player_sequence[i][1]

        # Run of the game for the players based on their strategies
        action_1 = get_strategies()[players[p1]](game_name, 1)
        action_2 = get_strategies()[players[p2]](game_name, 2)

        # Payoffs for the players at (action_1, action_2) profile
        payoff_1 = get_payoffs(game_name)[1][action_1][action_2]
        payoff_2 = get_payoffs(game_name)[2][action_1][action_2]

        # Collecting the games' summary
        payoff_summary.append({p1: payoff_1, p2: payoff_2})

        # Print the results of the game
        result_msg = f'Game {i + 1} of {num_games}:\t'
        result_msg += f'Players: ({p1}, {p2}) -> ({action_1}, {action_2})\t'
        result_msg += f'Payoffs: ({p1}, {p2}) -> ({payoff_1}, {payoff_2})\n'
        result_msg += '-' * 40
        print(result_msg)
        if i == len(get_payoffs()) - 1 and alone_player is not None:
            print(f'Player left behind: {alone_player}')

    return payoff_summary


def get_class_points(payoff_summary: dict) -> dict:
    """ Function that receives the payoff summary and returns the class points
    Args:
        payoff_summary (dict): Dictionary with the payoffs for each game.
    Returns:
        class_points (dict): Dictionary with the class points for each player.
    """

    class_points = []

    for row in payoff_summary:
        # Each row is a dict like {p1: payoff_1, p2: payoff_2}
        keys = list(row.keys())
        if len(keys) == 2:
            k1, k2 = keys
            v1, v2 = row[k1], row[k2]
            if v1 > v2:
                class_points.append({k1: 2, k2: 0})
            elif v2 > v1:
                class_points.append({k1: 0, k2: 2})
            else:
                class_points.append({k1: 1, k2: 1})
        else:
            # Handle the case where there is only one player (alone)
            k1 = keys[0]
            class_points.append({k1: 1})

    return class_points



def gen_games(hyperparams: dict, gen: int) -> list:
    """ Function that runs the game for the players in the player_sequence
    Args:
        hyperparams (dict): Dictionary with the strategies of each player.
        gen (int): Number of rounds to play.
    Returns:
        list: List of tuples with the payoffs for each game.
    """
    general_summary = []
    for gen_i in range(1, gen + 1):
        print(f'Round {gen_i} of {gen}')
        class_points = get_class_points(lets_play_the_game(hyperparams, gen_i))
        general_summary.append(class_points)

    return general_summary


from collections import defaultdict

def agrega_resultados(lista_de_jogos, nomes_dos_jogos):
    """
    lista_de_jogos: [jogos_1, jogos_2, ..., jogos_n]
        onde cada jogos_i é uma lista de dicionários, um dicionário por jogo.
    nomes_dos_jogos: ['dilema_prisioneiros', 'hawk dove', ...] — 
        mesmo comprimento de cada jogos_i.
    Retorna um dict no formato desejado.
    """
    # inicializa estrutura vazia
    resultado_final = {
        nome: defaultdict(list)
        for nome in nomes_dos_jogos
    }

    # percorre cada rodada (índice i)
    for rodada in lista_de_jogos:
        # para cada jogo na rodada, associa ao nome
        for nome, dict_jogo in zip(nomes_dos_jogos, rodada):
            # para cada jogador e payoff, apenda ao histórico
            for jogador, payoff in dict_jogo.items():
                resultado_final[nome][jogador].append(float(payoff))
    
    # converte os defaultdicts de volta para dicts normais
    return {
        nome: dict(histórico)
        for nome, histórico in resultado_final.items()
    }