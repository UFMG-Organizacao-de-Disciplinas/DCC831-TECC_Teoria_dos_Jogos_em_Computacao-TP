""" Running Games """


import random

players = ['Rangel', 'João', 'Hard-Enzo']

      
def draw_unique_players(players, alone_player = None):
  """"  Function receives as input the player list , and returns the list of players per game ordering"""

  # Making the shuffle of the players left to play in class
  players_left = players
  random.shuffle(players_left)
  player_sequence = []

  while len(players_left) >= 2:
    if alone_player:
      player01 = players_left.pop(players.index(alone_player))
      player02 = players_left.pop()
      player_sequence.append((player01, player02))

    else:
      player01 = players_left.pop()
      player02 = players_left.pop()
      player_sequence.append((player01, player02))


  if len(players_left) == 1:
        alone_player = players_left[0]

  return player_sequence, alone_player


player_sequence, alone_player = draw_unique_players(players)


print(player_sequence)
print(alone_player)


