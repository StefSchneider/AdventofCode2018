"""
Advent of Code 2018 - Day 2
Author: Stefan Schneider
github stefschneider1970
"""

import operator
from collections import Counter
from itertools import cycle # only for Part 2

path_file: str = "AoC2018_02_input.txt"
count_double_elements: int = 0
count_triple_elements: int = 0
check_double_elements: bool = False
check_triple_elements: bool = False
checksum: int = 0


# ---------- PART ONE ----------

print("Starting part one...\r")

with open(path_file, "r") as data_file:
    # use file with data for ids
    for line in data_file:
        line = line.strip()
        check_double_elements = False
        check_triple_elements = False
        id_count = dict(Counter(line).most_common())
        if ((2 in id_count.values()) and (check_double_elements == False)):
            count_double_elements += 1
            check_double_elements = True
        if ((3 in id_count.values()) and (check_triple_elements == False)):
            count_triple_elements += 1
            check_triple_elements = True

print("Found double elements: ", count_double_elements)
print("Found triple elements: ", count_triple_elements)
print("Checksum: ", count_double_elements * count_triple_elements)
print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")
