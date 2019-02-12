"""
Advent of Code - Day 09
Author: Stefan Schneider
Github: StefSchneider
"""

import collections

max_players: int = 452 # from input
last_marble_point: int = 70784 # from input
players_points: dict = {}
max_point: int = 0


def calculate_points(max_players: int, last_marble_point: int):
    current_marble: int = 1
    player: int = 1
    marbles = collections.deque([0]) # insert marble No. 0
    for i in range(1, max_players + 1):  # fill players points with zeor
        players_points[i] = 0
    while current_marble <= last_marble_point:
        if current_marble % 23 == 0:
            marbles.rotate(8)
            players_points[player] += (current_marble+marbles[0])
            marbles.popleft()
            marbles.rotate(1)
        else:
            marbles.insert(1, current_marble)
        current_marble +=1
        marbles.rotate(-2)
        player += 1
        if player > max_players:
            player = 1
    max_point = sorted(players_points.values(), reverse = True)[0] # sort highscore at pos. 0

    return max_point


# ---------- PART ONE ----------

print("Starting part one...\r")

print("Highscore part one:", calculate_points(max_players, last_marble_point), "\r")
print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")

print("Highscore part two:", calculate_points(max_players, last_marble_point*100))
# multipy last_marble_point with 100 as per task