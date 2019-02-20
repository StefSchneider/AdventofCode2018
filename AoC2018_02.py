"""
Advent of Code 2018 - Day 2
Author: Stefan Schneider
github StefSchneider
"""

import operator
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

combi = itertools.combinations(data_file, 2)
for elements in combi:
    diff_1 = False
    differenz = 0
    diff_content = []
    for i in range(len(elements[0])):
        if (elements[0])[i] != (elements[1])[i]:
            differenz += 1
            diff_content.append((elements[0])[i])
            diff_content.append((elements[1])[i])
    if differenz == 1:
        print(diff_content)
        print(elements[0], elements[1])








#    schnittmenge = set(elements[0])-set(elements[1])
#    diff_1 = set(elements[0])-schnittmenge
#    diff_2 = set(elements[1])-schnittmenge
#    if (len(schnittmenge) > 1) and (diff_1 == diff_2) and (len(diff_1) == len(elements[0])-1):
#        print(schnittmenge)
#        print((set(elements[0])-schnittmenge), (set(elements[1])-schnittmenge))
#        print(elements)
