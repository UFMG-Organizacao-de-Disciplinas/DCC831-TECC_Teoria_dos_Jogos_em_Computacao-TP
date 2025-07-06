# If you need to install packages, do so in your terminal:
# pip install matplotlib numpy pandas nashpy


from Modules.get_hyperparams import setting_up_hyperparameters
from Modules.get_payoffs import get_payoffs
from Modules.get_players import get_players
from Modules.get_strategies import get_strategies
from Modules.run_games import gen_games
from Modules.run_games import get_class_points
from Modules.run_games import draw_unique_players
from Modules.run_games import lets_play_the_game
from Modules.plot_games import plot_games

def main():
    game_theory_classes = [
       {
            'minimax': 4,
            'maxmin': 4,
            'minimax_regret': 4,
            'social_welfare': 4,
            'temptation': 4,
            'pure_nash': 4,
        }, 
        {
            'minimax': 20,
            'maxmin': 0,
            'minimax_regret': 0,
            'social_welfare': 0,
            'temptation': 0,
            'pure_nash': 0,
        }, 
        {
            'minimax': 0,
            'maxmin': 20,
            'minimax_regret': 0,
            'social_welfare': 0,
            'temptation': 0,
            'pure_nash': 0,
        }, 
        {
            'minimax': 0,
            'maxmin': 0,
            'minimax_regret': 20,
            'social_welfare': 0,
            'temptation': 0,
            'pure_nash': 0,
        }, 
        {
            'minimax': 0,
            'maxmin': 0,
            'minimax_regret': 0,
            'social_welfare': 20,
            'temptation': 0,
            'pure_nash': 0,
        }, 
        {
            'minimax': 0,
            'maxmin': 0,
            'minimax_regret': 0,
            'social_welfare': 0,
            'temptation': 20,
            'pure_nash': 0,
        }, 
        {
            'minimax': 0,
            'maxmin': 0,
            'minimax_regret': 0,
            'social_welfare': 0,
            'temptation': 0,
            'pure_nash': 20,
        },
        {
            'minimax': 0,
            'maxmin': 0,
            'minimax_regret': 0,
            'social_welfare': 10,
            'temptation': 10,
            'pure_nash': 0,
        }, 
        {
            'minimax': 4,
            'maxmin': 4,
            'minimax_regret': 2,
            'social_welfare': 5,
            'temptation': 5,
            'pure_nash': 1,
        }, 
        {
            'minimax': 10,
            'maxmin': 10,
            'minimax_regret': 0,
            'social_welfare': 0,
            'temptation': 0,
            'pure_nash': 0,
        },
    ]
    
    num_rounds = 1000
    
    games = get_payoffs()
    gaming_parameters = setting_up_hyperparameters()
    for game_class in game_theory_classes:
        
        players = get_players(game_class)
        results = gen_games(game_class, num_rounds)
        plot_games(
            games,
            players,
            results,
            gaming_parameters
        )
        
main()

        

        

        
    
    
    
    
    
    
    
