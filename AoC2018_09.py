"""
Advent of Code - Day 09
Author: Stefan Schneider
Github: StefSchneider
"""

import collections

max_players: int = 452 # from input
last_marble_point: int = 70784 # from input
player: int = 1
current_marble: int = 1
max_point: int = 0


players_points: dict = {}
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


max_point = sorted(players_points.values(), reverse = True)[0]

print(max_point)