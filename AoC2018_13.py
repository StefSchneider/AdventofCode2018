"""
Advent of Code - Day 13
Author: Stefan Schneider
Github: StefSchneider
"""

path_file: str = "AoC2018_13_input_test.txt"
#path_file: str = "AoC2018_13_input.txt"

map_list: list = []
map_entry: tuple = (0, 0, "", 0) # order: x-pos of cart, y-pos of cart, direction, next direction intersection (0=left, 1=straight, 2=right)
carts: list = []
direction: str = ""
CART_DIRECTIONS: dict = {"<" : "left",
                         ">" : "right",
                         "^" : "top",
                         "v" : "down"}
INTERSECTION_DIRECTIONS: list = ["left", "straight", "right"]


def move_cart():
    pass


data_file = open(path_file).read().split("\n")
y: int = 0
for line in data_file:
    for x in range(0, len(line)):
        if data_file[y][x] != " ":
            map_entry = (x, y, data_file[y][x])
            if data_file[y][x] == ">":
                direction = "right"
                cart = (x, y, direction, 0)
                carts.append(cart)
                map_entry = (x, y, "-")
            elif data_file[y][x] == "<":
                direction = "left"
                cart = (x, y, direction, 0)
                carts.append(cart)
                map_entry = (x, y, "-")
            elif data_file[y][x] == "^":
                direction = "top"
                cart = (x, y, direction, 0)
                carts.append(cart)
                map_entry = (x, y, "|")
            elif data_file[y][x] == "v":
                direction = "down"
                cart = (x, y, direction, 0)
                carts.append(cart)
                map_entry = (x, y, "|")
            map_list.append(map_entry)

    y += 1



carts.sort()
print(len(map_list), map_list)
carts.sort()
print(len(carts), carts)
