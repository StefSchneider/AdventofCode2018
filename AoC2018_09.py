"""
Advent of Code - Day 09
Author: Stefan Schneider
Github: StefSchneider
"""

import collections

players:int = 452
last_marble_point: int = 70784
player: int = 1
current_marble: int = 1


players_points = collections.defaultdict()
marbles = collections.deque([0])


# insert current_marble at position 1

print(marbles[0])
