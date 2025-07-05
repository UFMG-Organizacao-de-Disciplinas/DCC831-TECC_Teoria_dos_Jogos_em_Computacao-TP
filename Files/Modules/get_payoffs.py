""" Setting up the games:
    - Define which libraries to use and how they define the games
    - How to use correlated equilibrium?
    - How to repeat the same game?
"""


def get_payoffs(game_name: str = '') -> dict:
    """ Returns the payoffs for the specified game.

    Args:
        game_name (str): The name of the game to retrieve payoffs for.

    Returns:
        dict: A dictionary containing the payoffs for each player in the game.
    """

    games_payoffs = {
        'exam_presentation': {
            1: [[90.0, 86.0],
                [92.0, 88.0]],
            2: [[90.0, 92.0],
                [86.0, 88.0]], },
        'prisoners_dilemma': {
            1: [[-1.0, -10.0],
                [0.0, -4.0]],
            2: [[-1.0,   0.0],
                [-10.0, -4.0]], },
        'unb_coord_game': {
            1: [[1.0, 0.0],
                [0.0, 2.0]],
            2: [[1.0, 0.0],
                [0.0, 2.0]], },
        'matching_pennies': {
            1: [[1.0, -1.0],
                [-1.0,  1.0]],
            2: [[-1.0,  1.0],
                [1.0, -1.0]], },
        'rock_paper_scissors': {
            1: [[0.0, -1.0,  1.0],
                [1.0,  0.0, -1.0],
                [-1.0,  1.0,  0.0]],
            2: [[0.0,  1.0, -1.0],
                [-1.0, 0.0,  1.0],
                [1.0, -1.0, 0.0]], },
        'stag_hunt': {
            1: [[4.0, 0.0],
                [3.0, 3.0]],
            2: [[4.0, 3.0],
                [0.0, 3.0]], },
        'fun_game': {
            1: [[320.0, 40.0],
                [40.0, 80.0]],
            2: [[40.0, 80.0],
                [80.0, 40.0]], },
        'another_game_to_be_played': {
            1: [[0.48, 0.60],
                [0.40, 0.32]],
            2: [[0.12, 0.40],
                [0.60, 0.08]], },
        'another_solution_concept': {
            1: [[3.0, 0.0,  0.0],
                [1.0, 1.0, 10.0],
                [0.0, 4.0,  5.0]],
            2: [[1.0, 3.0, 0.0],
                [5.0, 1.0, 0.0],
                [0.5, 2.0, 0.0]], },
        'hawk_dove': {
            1: [[3, 1],
                [5, 0]],
            2: [[3, 5],
                [1, 0]], },
    }

    if not game_name:
        return games_payoffs

    return games_payoffs.get(game_name, {})
