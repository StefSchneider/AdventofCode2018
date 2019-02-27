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
for line in data_file:
    position, velocity = re.findall(r"(<?\w*>)", line) #, velocity
    print(position, velocity) #, velocity


print(data_file)

#for line in data_file:
