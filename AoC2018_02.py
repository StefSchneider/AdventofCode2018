"""
Advent of Code 2018 - Day 2
Author: Stefan Schneider
github StefSchneider
"""

from collections import Counter
import itertools # only for Part 2

path_file: str = "AoC2018_02_input.txt"
count_double_elements: int = 0
count_triple_elements: int = 0
check_double_elements: bool = False
check_triple_elements: bool = False
checksum: int = 0


# ---------- PART ONE ----------

print("Starting part one...\r")

data_file = open(path_file).read().split("\n")
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

string_combination = itertools.combinations(data_file, 2) # combine every line of input with all others
for elements in string_combination:
    difference: int = 0
    difference_position: int = 0
    difference_content: list = []
    final_string: str = ""
    for i in range(len(elements[0])):
        if (elements[0])[i] != (elements[1])[i]:
            difference += 1
            difference_position = i
            difference_content.append((elements[0])[i])
            difference_content.append((elements[1])[i])
    if difference == 1:
        print("Elements", elements[0], "and", elements[1], "differ in:", difference_content)
        final_string = elements[0][0:difference_position]+elements[0][difference_position+1:]
        print("Solution of part two:", final_string)