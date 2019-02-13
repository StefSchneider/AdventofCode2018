"""
Advent of Code - Day 12
Author: Stefan Schneider
Github: stefschneider
"""

initial_state = list("#..######..#....#####..###.##..#######.####...####.##..#....#.##.....########.#...#.####........#.#.")

path_file: str = "AoC2018_12_input.txt"
current_list: list = [] # list for current generation
new_list: list = [] # list for next generation
current_generation: str = ""
number_pot: list = []
sum_pots: int = 0

class Pot():
    def __init__(self, content: str, number: int):
        self.content = content
        self.number = number

    def __str__(self):

        return self.content

# ---------- PART ONE ----------

print("Starting part one...\r")

for count in range(0, len(initial_state)): # generates list of content and position from initial_state
    pot = Pot(initial_state[count], count)
    current_list.append(pot)

for count in range(-1, -6, -1): # inserts 5 empty pots in initial list at the left side and at the right side
    pot = Pot(".", count)
    current_list.insert(0, pot) # insert empty pot at the beginning
    pot = Pot(".", current_list[len(current_list) - 1].number + 1)
    current_list.append(pot) # insert empty pot at the end

for count in range(0, len(current_list)): # just to show the result of initial state
    current_generation += current_list[count].content
    number_pot.append(current_list[count].number)
    if current_list[count].content == "#":
        sum_pots += current_list[count].number
print("Round: initial state")
print("Pots current generation: ", current_generation)
print("Number of Pots", number_pot)
print("Sum of Pots with plant: ", sum_pots, "\r")

for round in range(20): # for 20 generations
    current_generation = ""
    number_pot = []
    sum_pots = 0
    new_list = []
    print("Round:", round+1)

    for count in range(0, len(current_list)): # fills new list with empty content and number of pots
        pot = Pot(".", current_list[count].number - 1)
        # creates one more pot (with new nummber at the left side) in new list than in current generation
        new_list.append(pot)
    for count in range(0, 2): # adds 2 empty pots at the end of empty list
        pot = Pot(".", new_list[len(new_list) - 1].number + 1)
        new_list.append(pot)

    with open(path_file, "r") as data_file:
        # use file with data for sliders
        for line in data_file:
            slider, next_generation = line.split(" => ")
            next_generation = next_generation.strip()
            for position in range(0,len(current_list)-4):
                part: str = ""
                for count in range(0,5): # creates part of the current list to compare with slider
                    part += current_list[position+count].content
                if part == slider:
                    new_list[position+3].content = next_generation

    current_list = new_list

    for count in range(0, len(current_list)): # just to show results of each step
        current_generation += current_list[count].content
        number_pot.append(current_list[count].number)
        if current_list[count].content == "#":
            sum_pots += current_list[count].number
    print("Pots current generation:", current_generation)
    print("Number of Pots", number_pot)
    print('Sum of Pots with plant: ',sum_pots)
    print("\r")


# ---------- PART TWO ----------

print("Starting part two...\r")



