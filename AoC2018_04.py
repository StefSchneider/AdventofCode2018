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
empty_shift = numpy.zeros((1,60), int)
shifts = numpy.array((1,60), int)
guards_shifts: dict = {} # guard : shift
awake_asleep: int = 0

def parse_minutes(date_time: str) -> int: # extracts number of minutes from string
    date_time = date_time.split()
    date, time = date_time[0][1:], date_time[1]
    minutes = int(time.split(':')[1])
    if time[0:2] != "00":
        minutes = 0

    return minutes


def parse_guard(part_line: str) -> int: # extracts number of guard from string
    parts = part_line.split()
    guard = parts[1][1:]

    return guard


def change_shift(current_shift, minutes: int, awake_asleep: int):
    print(minutes, awake_asleep, current_shift.size)
    for i in range(minutes, current_shift.size-1):
            current_shift[i] = awake_asleep
    print(current_shift)
    return current_shift

data_file = open(path_file).read().split("\n")
# use file with data for shifts

data_file.remove("")
data_file.sort()
print(data_file)
for line in data_file:
    parts = re.split(r"(.{16})] ", line)
    parts.remove("[")
    date_time = parts[0]
    print(date_time)
    code = parts[1]
    minutes = parse_minutes(date_time)
    code = re.split(" ",code)
    print(minutes, code)
#    print(code)
    if code[0] == "Guard":
        guard_number = code[1][1:]
#        shift = guards_shifts.get(guard_number, empty_shift)
        current_shift = empty_shift
        awake_asleep = 1
    elif code[0] == "falls":
        awake_asleep = 0
    elif code[0] == "wakes":
        awake_asleep = 1

    new_shift = change_shift(current_shift, minutes, awake_asleep)
#    print(new_shift)
    print(guard_number, minutes, awake_asleep, current_shift)
    current_shift = new_shift

print(guards_shifts)
#if re.match("Guard", line):
#    guard = parts[x].re.split(r"(#\d*")
#    guard = guard

# zeile aufteilen: parts = re.split(r"(.{16})]", line)

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html#numpy.vstack