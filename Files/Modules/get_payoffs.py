""" Setting up the games
    - Descobrir como a biblioteca aceita a definição de jogos
    - Como usar equilíbrio correlacionado?
    - Como repetir o mesmo jogo?
"""


def get_payoffs(game_name=''):
    """ Returns the payoffs for the specified game.

    Args:
        game_name (str): The name of the game to retrieve payoffs for.

    Returns:
        dict: A dictionary containing the payoffs for each player in the game.
    """

    games_payoffs = {
        'exam_presentation': {
            'p1': [
                [90.0, 86.0],
                [92.0, 88.0]],
            'p2': [
                [90.0, 92.0],
                [86.0, 88.0]],
        },
        'prisoners_dilemma': {
            'p1': [
                [-1.0, -10.0],
                [0.0, -4.0]],
            'p2': [
                [-1.0,   0.0],
                [-10.0, -4.0]],
        },
        'unb_coord_game': {
            'p1': [
                [1.0, 0.0],
                [0.0, 2.0]],
            'p2': [
                [1.0, 0.0],
                [0.0, 2.0]],
        },
        'matching_pennies': {
            'p1': [
                [1.0, -1.0],
                [-1.0,  1.0]],
            'p2': [
                [-1.0,  1.0],
                [1.0, -1.0]],
        },
        'rock_paper_scissors': {
            'p1': [
                [0.0, -1.0,  1.0],
                [1.0,  0.0, -1.0],
                [-1.0,  1.0,  0.0]],
            'p2': [
                [0.0,  1.0, -1.0],
                [-1.0, 0.0,  1.0],
                [1.0, -1.0, 0.0]],
        },
        'stag_hunt': {
            'p1': [
                [4.0, 0.0],
                [3.0, 3.0]],
            'p2': [
                [4.0, 3.0],
                [0.0, 3.0]],
        },
        'fun_game': {
            'p1': [
                [320.0, 40.0],
                [40.0, 80.0]],
            'p2': [
                [40.0, 80.0],
                [80.0, 40.0]],
        },
        'another_game_to_be_played': {
            'p1': [
                [0.48, 0.60],
                [0.40, 0.32]],
            'p2': [
                [0.12, 0.40],
                [0.60, 0.08]],
        },
        'another_solution_concept': {
            'p1': [
                [3.0, 0.0,  0.0],
                [1.0, 1.0, 10.0],
                [0.0, 4.0,  5.0]],
            'p2': [
                [1.0, 3.0, 0.0],
                [5.0, 1.0, 0.0],
                [0.5, 2.0, 0.0]],
        },
        'hawk_dove': {
            'p1': [
                [3, 1],
                [5, 0]],
            'p2': [
                [3, 5],
                [1, 0]],
        },
    }
    if not game_name:
        return game_name

    return games_payoffs.get(game_name, None)
