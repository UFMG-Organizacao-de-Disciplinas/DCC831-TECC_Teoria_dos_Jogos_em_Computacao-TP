from Modules.get_hyperparams import setting_up_hyperparameters
from Modules.get_payoffs import get_payoffs
from Modules.get_players import get_players
from Modules.get_strategies import get_strategies
from Modules.run_games import gen_games
from Modules.run_games import final_results
from Modules.plot_games import plot_games


def main():
    game_theory_classes = [
        {'minimax': 3, 'maxmin': 3, 'minimax_regret': 3, 'social_welfare': 3,
            'temptation': 3, 'pure_nash': 3, },  # Distributed Class
        {'minimax': 18, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 0,
            'temptation': 0, 'pure_nash': 0, },  # Full Minimax
        {'minimax': 0, 'maxmin': 18, 'minimax_regret': 0, 'social_welfare': 0,
            'temptation': 0, 'pure_nash': 0, },  # Full Maxmin
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 18, 'social_welfare': 0,
            'temptation': 0, 'pure_nash': 0, },  # Full Minimax Regret
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 18,
            'temptation': 0, 'pure_nash': 0, },  # Full Social Welfare
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 0,
            'temptation': 18, 'pure_nash': 0, },  # Full Temptation
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 0,
            'temptation': 0, 'pure_nash': 18, },  # Full Pure Nash
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 9,
            'temptation': 9, 'pure_nash': 0, },  # Benevolent vs Evil
        {'minimax': 0, 'maxmin': 9, 'minimax_regret': 0, 'social_welfare': 9,
            'temptation': 0, 'pure_nash': 0, },  # Benevolent vs Fearful
        {'minimax': 0, 'maxmin': 0, 'minimax_regret': 0, 'social_welfare': 9,
            'temptation': 0, 'pure_nash': 9, },  # Benevolent vs Rational
    ]

    agregated_results_per_game = []

    payoffs = get_payoffs()  # Get the payoffs for all the games
    strategies = get_strategies()  # Get the strategies functions for all the games

    gaming_parameters = setting_up_hyperparameters()  # Get the gaming parameters
    # Updates the number of expected rounds
    gaming_parameters['num_rounds'] = 10
    for game_class in game_theory_classes:  # Runs through all the game classes
        gaming_parameters['strat_count'] = game_class

        players = get_players(game_class)
        results = gen_games(game_class, gaming_parameters['num_rounds'])
        merged_results = final_results(results, list(payoffs.keys()))
        agregated_results_per_game.append(merged_results)
        # print(agregated_results_per_game)
        plot_games(
            payoffs,
            players,
            results,
            gaming_parameters,
            list(strategies.keys())
        )


main()
