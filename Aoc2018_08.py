"""
Advent of Code - Day 8
Author: Stefan Schneider
Github: StefSchneider
"""

path_file: str = "AoC2018_08_input.txt"
data_file = list(map(int, open(path_file).read().split(" "))) # convert list of strings in list of integers


def parse_node(data_file):
    number_children = data_file[0] # read number of children current node
    number_metadata = data_file[1] # read number of metadata current node
    data_file = data_file[2:] # raise pointer at data_file for 2 steps
    sum_metadata: int = 0
#    metadata: int = 0
    values: list = []
    sum_values: int = 0
    for i in range(0, number_children):
        metadata, value, data_file = parse_node(data_file)
        sum_metadata += metadata
        values.append(value)
    sum_metadata += sum(data_file[:number_metadata])

    if number_children == 0:
        print("child value:", sum_metadata)
        return (sum_metadata, sum_metadata, data_file[number_metadata:]) # sum_metadata
    else:
        print(sum_metadata)
        print(values, sum(values), data_file[:number_metadata])
        return(
            sum_metadata,
            sum(values[k - 1] for k in data_file[:number_metadata] if k > 0 and k <= len(values)),
            data_file[number_metadata:]
        )


 #       for k in data_file[:number_metadata]:
 #           print("K", k, data_file[:number_metadata])
 #           if k > 0 and k <= len(values):
 #               print(len(values), values, values[k-1], sum_values)
 #               sum_values += values[k-1]
 #       return (sum_metadata, sum_values, data_file[number_metadata:])


metadata, value, last = parse_node(data_file)
print(metadata)
print(value)

