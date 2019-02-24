"""
Advent of Code - Day 4
Author: Stefan Schneider
Github: StefSchneider
"""

import numpy

path_file: str = "AoC2018_04_input.txt"
guard_number: int = 0
empty_shift = numpy.zeros((1,60), int)
shifts = numpy.array((1,60), int)
guards_shifts: dict = {} # guard : shift
awake_asleep: int = 0
current_shift = numpy.zeros((1,60), int)
max_minutes: int = 0
sum_minutes: int = 0
max_minute_guard: int = 0


def parse_minutes(date_time: str) -> int: # extracts number of minutes from string
    date_time = date_time.split()
    date, time = date_time[0][1:], date_time[1]
    minutes = int(time.split(':')[1])
    if time[0:2] != "00":
        minutes = 0

    return minutes


def change_shift(current_shift, minutes: int, awake_asleep: int):
    length = int(current_shift.size)
    for i in range(minutes, length):
        current_shift[0][i] = awake_asleep
    return current_shift

data_file = open(path_file).read().split("\n")
# use file with data for shifts

data_file.remove("")
data_file.sort()
print(data_file)
for line in data_file:
    print(line)
    parts = line.split("] ")
    parts[0] = parts[0].lstrip("[")
    date_time = parts[0]
    print(date_time)
    code = parts[1]
    minutes = parse_minutes(date_time)
    code = code.split(" ")
    print(minutes, code)
    if code[0] == "Guard":
        shift = guards_shifts.get(guard_number, empty_shift)
        shift = numpy.vstack((shift, current_shift))
        guards_shifts[guard_number] = shift
        print(guard_number, shift)
#        weiter = input()
        guard_number = int(code[1][1:])
        current_shift = numpy.copy(empty_shift)
        awake_asleep = 0
    elif code[0] == "falls":
        awake_asleep = 1
    elif code[0] == "wakes":
        awake_asleep = 0

    current_shift = change_shift(current_shift, minutes, awake_asleep)


print("Shifts")
for i in guards_shifts:
    print(i, guards_shifts[i])
    sum_minutes = numpy.sum(guards_shifts[i])
    if sum_minutes > max_minutes:
        max_minutes = sum_minutes
        max_minute_guard = i

print("Max guard", max_minute_guard)
print("Max. minutes", max_minutes)

sum_array = numpy.copy(guards_shifts[max_minute_guard])
print(sum_array)
length = sum_array.size
print(numpy.sum(sum_array, axis=0))