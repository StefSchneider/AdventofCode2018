"""
Advent of Code - Day 10
Author: Stefan Schneider
Github: StefSchneider
"""

import re

path_file: str = "AoC2018_10_input.txt"

"""
split input data in

1. lstrip("position=<")
2. rstrip(">"

finde alle Ziffern zwischen "<" und ">"
1. Ziffernpaar: position
2. Ziffernpaar: Velocity
"""

data_file = open(path_file).read()
data_file = re.split(r"\n", data_file)
data_file.remove("")
for i in range(0, 20):
    for line in data_file:
        pos_x, pos_y, velo_x, velo_y = re.findall(r"(-?\d+)", line)
        max_x = pos_x+i*velo_x
        max_y = pos_y+i*velo_y



# abs()
