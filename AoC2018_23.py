'''
Advent of Code - Day 23
Author: Stefan Schneider
Github: stefschneider1970
'''

path_file: str = 'AoC2018_23_data_nanobots.txt'
nanobots: list = [] # creates an empty list for all nanobots
max_radius: int = 0
bot_number_max_radius: int = 0
number_bots_in_range: int = 0

class Nanobot:
    def __init__(self, number: int, x_position: int, y_position: int, z_position: int, bot_radius: int):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position
        self.z_position = z_position
        self.sum_positions = x_position+y_position+z_position
        self.bot_radius = bot_radius

    def __str__(self):

        return self.number, self.x_position, self.y_position, self.z_position, self.bot_radius


with open(path_file, 'r') as data_file:
    # use file with data for nanobots
    number_bot: int = 0
    for line in data_file: # load nanobots from data file
        number_bot += 1
        positions, radius = line.split(', r=')
        radius = int(radius.strip(''))
        positions = positions.lstrip('pos=<')
        positions = positions.rstrip('>')
        positions = positions.strip()
        x_position, y_position, z_position = positions.split(',')
        nanobot = Nanobot(number_bot, int(x_position), int(y_position), int(z_position), radius)
        nanobots.append(nanobot)
    print('Nanobots included: ', number_bot)

# ---------- PART ONE ----------

print('Starting part one...\r')

for count in range(0, number_bot): # find bot with maximum radius
    if nanobots[count].bot_radius > max_radius:
        max_radius = nanobots[count].bot_radius
        bot_number_max_radius = nanobots[count].number
        print('New maximum radius: ', max_radius, 'of bot: ',bot_number_max_radius)

for count in range(0, number_bot): # counts every nanobot in range
    if nanobots[count].sum_positions <= max_radius:
        number_bots_in_range += 1

if nanobots[bot_number_max_radius].sum_positions > max_radius: # includes nanobot with maximum radius
    number_bots_in_range += 1

print('Maximum Radius: ', max_radius, ' of bot:', bot_number_max_radius)
print('Bots in range: ', number_bots_in_range)
print('\r')


# ---------- PART TWO ---------

print('Starting part two...\r')

origin = Nanobot(0, 0, 0, 0, 0) # save own coordinates at 0, 0, 0 by using class Nanobot


