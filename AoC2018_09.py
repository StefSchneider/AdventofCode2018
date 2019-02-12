"""
Advent of Code - Day 09
Author: Stefan Schneider
Github: StefSchneider
"""

import collections

max_players:int = 452
max_players = 5
last_marble_point: int = 70784
last_marble_point = 24
player: int = 1
current_marble: int = 1


players_points = collections.defaultdict()
marbles = collections.deque([0])


# insert current_marble at position 1

while current_marble <= last_marble_point:
    print("current marble:", current_marble)
    print("current player:", player)
    if current_marble % 23 == 0:
        marbles.rotate(8)
        print(marbles[0])
        marbles.popleft()
        marbles.rotate(1)
    else:
        marbles.insert(1, current_marble)
    print(marbles)
    current_marble +=1
    marbles.rotate(-2)
    player += 1
    if player > max_players:
        player = 1

