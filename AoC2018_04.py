"""
Advent of Code - Day 4
Author: Stefan Schneider
Github: StefSchneider
"""

import numpy

path_file: str = "AoC2018_04_input.txt"
guard_ID: int = 0
empty_shift = numpy.zeros((1,60), int) # creates an empty shift
shifts = numpy.array((1,60), int)
guards_shifts: dict = {}
awake_asleep: int = 0 # minutes asleep = 1, minutes awake = 1
current_shift = numpy.zeros((1,60), int)
guard_ID_max_minute: int = 0 # guard with maximum minutes on sleep (part one)
max_minute_guard: int = 0 # maximum minute guard is on sleep (part two)
final_minute: int = 0 # minute of all a guard is most asleep
maximum_minute: int = 0
max_minutes_per_guard: int = 0
list_minutes: list = []
pos_max_minute: int = 0


def parse_minutes(date_time: str) -> int: # extracts number of minutes from string
    date_time = date_time.split()
    date, time = date_time[0][1:], date_time[1]
    minutes = int(time.split(':')[1])
    if time[0:2] != "00":
        minutes = 0

    return minutes


def find_pos_maximum(list_to_check: list) -> int: # finds number of minute most alseep
    maximum_minute: int = 0
    pos_maximum: int = 0
    for i in range(0, len(list_to_check)):
        if list_to_check[i] > maximum_minute:
            maximum_minute = list_to_check[i]
            pos_maximum = i

    return pos_maximum


print("Build shifts from input...")
print("\r")

data_file = open(path_file).read().split("\n") # use file with data for shifts
data_file.sort()
for line in data_file:
    parts = line.split("] ")
    date_time = parts[0].lstrip("[")
    minutes = parse_minutes(date_time)
    code = parts[1].split(" ")
    if code[0] == "Guard" or data_file == None:
        shift = guards_shifts.get(guard_ID, empty_shift) # if guard is not in dictionary default = empty shift
        if not numpy.array_equal(current_shift, empty_shift):
            shift = numpy.vstack((shift, current_shift)) # adds new shift to shifts of current guard
        guards_shifts[guard_ID] = shift
        guard_ID = int(code[1][1:])
        current_shift = numpy.copy(empty_shift)
        awake_asleep = 0
    elif code[0] == "falls":
        awake_asleep = 1 # set minutes guard is asleep on 1
    elif code[0] == "wakes":
        awake_asleep = 0 # set  minutes guard is awake on 0
    for i in range(minutes, int(current_shift.size)): # update shift of guard
        current_shift[0][i] = awake_asleep


# ---------- PART ONE ----------

print("Starting part one...\r")

for guard in guards_shifts: # pick guard with most minutes of sleep
    if numpy.sum(guards_shifts[guard]) > max_minutes_per_guard:
        max_minutes_per_guard = numpy.sum(guards_shifts[guard])
        guard_ID_max_minute = guard

sum_array = numpy.sum(guards_shifts[guard_ID_max_minute], axis=0)
print("Guard with maximum minutes on sleep:", guard_ID_max_minute,)
print("Minute with maximum sleep:", find_pos_maximum(list(sum_array)))
print("Result of part one:", guard_ID_max_minute*find_pos_maximum(list(sum_array)))
print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")

for guard in guards_shifts:
    list_minutes = list(numpy.sum(guards_shifts[guard], axis = 0))
    maximum_minute_guard = max(list_minutes)
    pos_max_minute = find_pos_maximum(list_minutes)
    if maximum_minute_guard > maximum_minute:
        maximum_minute = maximum_minute_guard
        guard_ID_max_minute = guard
        final_pos = pos_max_minute

print("Guard with minute with maximum on sleep:", guard_ID_max_minute)
print("Minute with maximum sleep:", final_pos)
print("Result of part two:", guard_ID_max_minute*final_pos)