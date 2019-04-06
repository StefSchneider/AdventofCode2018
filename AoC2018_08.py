"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""

path_file: str = "AoC2018_08_input.txt"
data: list = list(map(int, open(path_file).read().split(" "))) # convert list of strings in list of integers


def parse_node(data):
    number_children = data[0] # read number of children current node
    number_metadata = data[1] # read number of metadata current node
    data = data[2:] # raise pointer at data_file for 2 steps
    sum_metadata: int = 0
    values: list = []
    sum_values: int = 0
    for i in range(0, number_children):
        metadata, value, data = parse_node(data)
        sum_metadata += metadata
        values.append(value)
    sum_metadata += sum(data[:number_metadata])
    print("Metadata of node", sum_metadata)

    if number_children == 0:
        print("child value:", sum_metadata)
        return (sum_metadata, sum_metadata, data[number_metadata:]) # just collect metadata of node
    else:
        for k in data[:number_metadata]: # collect metadata of child nodes
            if k > 0 and k <= len(values):
                sum_values += values[k-1]
        return (sum_metadata, sum_values, data[number_metadata:]) # result of child nodes

# start collecting data from nodes
metadata, value, last = parse_node(data) # use recursive structure
print("\n")
print("Part one: sum of metadata entries:", metadata, "\n")
print("Part two: value of root node:", value)
