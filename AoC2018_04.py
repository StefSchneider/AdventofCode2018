"""
Advent of Code - Day 4
Author: Stefan Schneider
Github: StefSchneider
"""

import datetime
import numpy
import re

path_file: str = "AoC2018_04_input.txt"
guard: int = 0
shift = numpy.zeros((1,60), int)
guards_shifts: dict = {} # guard : shift

def parse_minutes(date_time: str) -> int: # extracts number of minutes from string
    date_time = line.split()
    date, time = date_time[0][1:], date_time[1][:-1]

    return int(time.split(':')[1])


def parse_guard(part_line: str) -> int: # extracts number of guard from string
    parts = part_line.split()
    guard = parts[1][1:]

    return guard


def change_shift(guard: int, minutes: int, wake_asleep: str) -> list:
    pass

data_file = open(path_file).read().split("\n")
# use file with data for shifts

data_file.remove("")
data_file.sort()
print(data_file)
for line in data_file:
    parts = re.split(r"(.{16})] ", line)
    parts.remove("[")
    date_time = parts[0]
    code = parts[1]
    minutes = parse_minutes(date_time)
    code = re.split(" ",code)
    print(code)
    if code[0] == "Guard":
        guard_number = code[1][1:]
    elif code[0] == "falls":
        pass
    elif code[0] == "wakes":
        pass


#if re.match("Guard", line):
#    guard = parts[x].re.split(r"(#\d*")
#    guard = guard

# zeile aufteilen: parts = re.split(r"(.{16})]", line)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html#numpy.vstack