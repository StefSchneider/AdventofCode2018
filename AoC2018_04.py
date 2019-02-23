"""
Advent of Code - Day 4
Author: Stefan Schneider
Github: StefSchneider
"""

import datetime
import numpy

path_file: str = "AoC2018_04_input.txt"
guard: int = 0
shift = numpy.zeros((1,60), int)
guards_shifts: dict = {} # guard : shift

def parse_minutes(line: str) -> int: # extracts number of minutes from string
    words = line.split()
    date, time = words[0][1:], words[1][:-1]

    return int(time.split(':')[1])


def parse_guard(part_line: str) -> int: # extracts number of guard from string
    pass


data_file = open(path_file).read().split("\n")
# use file with data for shifts

data_file.remove("")
data_file.sort()
print(data_file)
for line in data_file:

    print(line, int(time.split(':')[1]))


#https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html#numpy.vstack