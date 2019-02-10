"""
Advent of Code 2018 - Day 03
Author: Stefan Schneider
Github: StefSchneider
"""

path_file: str = 'AoC2018_03_input.txt'
id: str = ''
coordinates_size: str = ''
coordinates: str = ''
size: str = ''
x_pos: int = 0 # part of coordinates
y_pos: int = 0 # part of coordinates
x_size: int = 0 # part of size
y_size: int = 0 # part of size
claims = set()
overlap: int = 0
set_ids: set = set()

fabric = [[set(claims) for j in range(1000)] for i in range(1000)] # initialize 1000x1000 matrix

with open(path_file, "r") as data_file:
    print("Adding ids to claim sets...\r")
    for line in data_file: # split data of each line
        # use file with data for claims
        id, coordinates_size = line.strip().split(' @ ')
        set_ids.add(id)
        coordinates, size = coordinates_size.strip().split(': ')
        x_pos, y_pos = coordinates.strip().split(',')
        x_size, y_size = size.strip().split('x')
        x_size = int(x_size)
        y_size = int(y_size)
        x_pos = int(x_pos)
        y_pos = int(y_pos)
        for count_x in range(0, x_size):
            for count_y in range(0, y_size):
                fabric[x_pos+count_x][y_pos+count_y].add(id)


# ---------- PART ONE ----------

print("Starting part one...\r")
print("Count overlapping inches..\r")

for i in range(0, 1000): # count square inches used by more than one claims
    for j in range(0, 1000):
        if len(fabric[i][j]) > 1:
            overlap += 1
print("Result of part one:", overlap, "inches are overlapping.")
print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")
print("Deleting ids of inches used by more than one claim...\r")

for i in range(1, 1000):
    for j in range(0, 1000):
        if len(fabric[i][j]) > 1:
            set_ids.difference_update(fabric[i][j])
print("Result of part two:", list(set_ids)[0])