"""
Advent of Code - Day 09
Author: Stefan Schneider
Github: StefSchneider
"""

import collections

max_players: int = 452
#max_players = 30
last_marble_point: int = 7078400
#last_marble_point = 5807
player: int = 1
current_marble: int = 1
max_point: int = 0


players_points = collections.defaultdict()
marbles = collections.deque([0])

for i in range(1, max_players+1):
    players_points[i] = 0


# insert current_marble at position 1

while current_marble <= last_marble_point:
#    print("current marble:", current_marble)
#    print("current player:", player)
    if current_marble % 23 == 0:
        marbles.rotate(8)
#        print(marbles[0])
        players_points[player] += (current_marble+marbles[0])
        marbles.popleft()
        marbles.rotate(1)
    else:
        marbles.insert(1, current_marble)
#    print(marbles)
    current_marble +=1
    marbles.rotate(-2)
    player += 1
    if player > max_players:
        player = 1

for i in range(1, max_players+1):
    if players_points[i] > max_point:
        max_point = players_points[i]

print(max_point)