# Project Idea

## Find a non trivial scenario

Considering the Game Theory course where we can earn gamepoints that will later be converted into a grade, we can think of a scenario where students are players in a game involving playing games to earn points. We consider that each student has as its objective to maximize their own grade, which is a function of the gamepoints they earn. However, focusing solely on their own behalf may not be the best strategy, as it can lead to suboptimal outcomes for the group as a whole.

## Describe this scenario informally: players, actions, conflicts, utilities, complications

Having said that, we could consider that our game could be described as "a sequence of Game Theory games where students, picked at random, play against each other to earn gamepoints". In this game, each student is a player, and their actions consist of, given a certain game, the actions they have available for them.

The conflicts arise from the fact that students are competing for the same gamepoints, and not necessarily cooperating will lead them to their best outcome, since their utilities are their conversion of gamepoints into grades, and we could also consider that the ones that have the least gamepoints will have the most to gain from earning more gamepoints.

The scenarion becomes even more complex when we consider that students may have different levels of knowledge and skills in game theory. They may consider different strategies based on their own understanding of the game and of the other players.

## Model one or more configurations for this scenario formally

### game type

A sequence of games where students play against each other to earn gamepoints.

### players

- Students enrolled in the Game Theory course
  - 1~5 picked at random#
    - #: the randomness considers that the same player will only be picked again after all other players have been picked

### strategies

many strategies are available and they differ between games.

### payoffs

the scores on the game table, which will be converted into grades

### solutions

It's what we are going to analyse: the different ways students can play the game, the strategies they can use, and how these affect their outcomes.

- **Maxmin:** Players choose strategies that maximize their minimum payoff, ensuring a baseline level of success.
- **Minimax:** Players choose strategies that minimize their maximum loss, focusing on avoiding the worst outcome.
- **Nash Equilibrium:** A situation where no player can benefit by changing their strategy while others keep theirs unchanged, leading to a stable outcome.
- **Pareto Optimality:** An outcome where no player can be made better off without making another player worse off, indicating an efficient allocation of resources.
- **Mixed Strategies:** Players randomize their strategies to keep opponents uncertain, potentially leading to more favorable outcomes.
- **Social Welfare:** The overall well-being of all players, considering the collective outcomes rather than individual gains, promoting cooperation and fairness.

## Discussion and conclusions

- We expect that throughout the experiment the Solution maximizing Social Welfare will be the most effective one as to increse the whole group's gamepoints, and consequently each student's grade.
