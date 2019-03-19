"""
Advent of Code - Day 13
Author: Stefan Schneider
Github: StefSchneider
"""

import operator

path_file: str = "AoC2018_13_input_test.txt"
path_file: str = "AoC2018_13_input.txt"

map_list: list = []
map_entry: tuple = ((0, 0), "", 0) # order: x-pos of cart, y-pos of cart, direction, next direction intersection (0=left, 1=straight, 2=right)
carts: list = []
cart: tuple = ()
current_cart: tuple = ()
CART_DIRECTIONS: dict = {"<": ("left", "-"), # order value: direction cart, entry map
                         ">": ("right", "-"),
                         "^": ("up", "|"),
                         "v": ("down", "|")
                         }
INTERSECTION_DIRECTIONS: list = ["left", "straight", "right"]
DIRECTION_CHANGES: dict = {("+", "left", "left"): "down", # order: 1: track, 2: direction cart, 3: direction intersection, 4: new direction
                           ("+", "left", "straight"): "left",
                           ("+", "left", "right"): "up",
                           ("+", "right", "left"): "up",
                           ("+", "right", "straight"): "right",
                           ("+", "right", "right"): "down",
                           ("+", "down", "left"): "right",
                           ("+", "down", "straight"): "down",
                           ("+", "down", "right"): "left",
                           ("+", "up", "left"): "left",
                           ("+", "up", "straight"): "up",
                           ("+", "up", "right"): "right",
                           ("/", "left"): "down",
                           ("/", "right"): "up",
                           ("/", "down"): "left",
                           ("/", "up"): "right",
                           ("\\", "left"): "up",
                           ("\\", "right"): "down",
                           ("\\", "down"): "right",
                           ("\\", "up"): "left"
                           }
crash: bool = False
new_direction = ""


def move_cart(current_cart: tuple) -> tuple:
    x_pos = current_cart[0][0]
    y_pos = current_cart[0][1]
    direction = current_cart[1]
    direction_intersection = current_cart[2]
    new_direction = ""
    if direction == "left":
        x_pos -= 1
    elif direction == "right":
        x_pos += 1
    elif direction == "up":
        y_pos -= 1
    elif direction == "down":
        y_pos += 1

    for i in range(0, len(map_list)):
        if map_list[i][0][0] == x_pos and map_list[i][0][1] == y_pos:
            list_index = i
            new_direction = map_list[i][1]
    print("New direction", new_direction)

    if new_direction == "+":
        if direction == "down" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "left":
            direction = "right"
        elif direction == "up" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "left":
            direction = "left"
        elif direction == "up" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "right":
            direction = "right"
        elif direction == "down" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "right":
            direction = "left"
        elif direction == "left" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "left":
            direction = "down"
        elif direction == "right" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "left":
            direction = "up"
        elif direction == "left" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "rigtz":
            direction = "up"
        elif direction == "right" and INTERSECTION_DIRECTIONS[direction_intersection%3] == "right":
            direction = "down"
        direction_intersection += 1
    elif new_direction == "/" and direction == "up":
        direction = "right"
    elif new_direction == "/" and direction == "down":
        direction = "left"
    elif new_direction == "/" and direction == "left":
        direction = "down"
    elif new_direction == "/" and direction == "right":
        direction = "up"
    elif new_direction == "\\" and direction == "up":
        direction = "left"
    elif new_direction == "\\" and direction == "down":
        direction = "right"
    elif new_direction == "\\" and direction == "left":
        direction = "up"
    elif new_direction == "\\" and direction == "right":
        direction = "down"
    else:
        new_direction = direction

    current_cart = ((x_pos, y_pos), direction, direction_intersection)
    print("new cart position", current_cart)

    return current_cart



data_file = open(path_file).read().split("\n")
y: int = 0
for line in data_file: # transfer data in map_list and car_list
    for x in range(0, len(line)):
        element = data_file[y][x]
        if element != " ":
            if element in CART_DIRECTIONS:
                cart = ((x, y), CART_DIRECTIONS.get(element)[0], 0)
                carts.append(cart)
                element = CART_DIRECTIONS.get(element)[1]
            map_entry = ((x, y), element)
            map_list.append(map_entry)
    y += 1

while not crash:
#    count_double = 0
    carts.sort(key=lambda carts:carts[0][1])
    for i in range(0, len(carts)):
        count_double = 0
        print(carts[i])
        current_cart = move_cart(carts[i])
        print(current_cart)
        carts[i] = current_cart
        for j in range(0, len(carts)):
            print("Cart", carts[j])
            print("Check equal", current_cart[0], current_cart[1])
            print("Count double", count_double)
            if current_cart[0] == carts[j][0]:
                count_double += 1
        if count_double > 1:
            crash = True
            break
 #       if carts.count(current_cart[0] and current_cart[1]) > 1:
 #           crash = True
 #           break
 #       for j in range(0, len(carts)):
 #           if carts[j][0] == current_cart[0] and carts[j][1] == current_cart[1]:
 #               crash = True
 #               break
 #       carts.sort()

print(len(map_list), map_list)
print(len(carts), carts)
print(current_cart[0], current_cart[1])
