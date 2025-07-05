""" Setting up the games """


def set_games(games_payoffs):
    """
    Set up the games with their payoffs.

    Args:
        games_payoffs (dict): A dictionary containing the payoffs for each game.

    Returns:
        dict: A dictionary containing the games and their respective payoffs.
    """
    game_sequence = {
        'g01': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['exam_presentation'], 'name': 'exam_presentation'},
        'g02': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['prisoners_dilemma'], 'name': 'prisoners_dilemma'},
        'g03': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['unb_coord_game'], 'name': 'unb_coord_game'},
        'g04': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['matching_pennies'], 'name': 'matching_pennies'},
        'g05': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['rock_paper_scissors'], 'name': 'rock_paper_scissors'},
        'g06': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['stag_hunt'], 'name': 'stag_hunt'},
        'g07': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['fun_game'], 'name': 'fun_game'},
        'g08': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['another_game_to_be_played'], 'name': 'another_game_to_be_played'},
        'g09': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['another_solution_concept'], 'name': 'another_solution_concept'},
        'g10': {'players': 2, 'same_players': True, 'repetitions': 1, 'payoffs': games_payoffs['hawk_dove'], 'name': 'hawk_dove'},
    }

    # print(f'We are going to play {len(game_sequence)} different games')

    return game_sequence
