"""
Advent of Code - Day 19
Author: Stefan Schneider
Github: StefSchneider
"""

import re

path_file: str = "AoC2018_19_input.txt"
ip: int = 0 # stores value of instruction pointer
ip_register: int = 0 # register manipulated by instruction pointer
register: list = [0, 0, 0, 0, 0, 0]
line: str = ""
fastlane: bool = False


def calculate_output_c(opcode: str, input_a: int, input_b: int, register_operate):
    return {
        "addr": lambda: register_operate[input_a] + register_operate[input_b], # add register
        "addi": lambda: register_operate[input_a] + input_b, # add immediate
        "mulr": lambda: register_operate[input_a] * register_operate[input_b], # multiply register
        "muli": lambda: register_operate[input_a] * input_b, # multiply immediate
        "banr": lambda: register_operate[input_a] & register_operate[input_b], # bitwise AND register
        "bani": lambda: register_operate[input_a] & input_b, # bitwise AND immediate
        "borr": lambda: register_operate[input_a] | register_operate[input_b], # bitwise OR register
        "bori": lambda: register_operate[input_a] | input_b, # bitwise OR immediate
        "setr": lambda: register_operate[input_a], # set register
        "seti": lambda: input_a, # set immediate
        "gtir": lambda: 1 if input_a > register_operate[input_b] else 0, # greater-than immediate/register
        "gtri": lambda: 1 if register_operate[input_a] > input_b else 0, # greater-than register/immediate
        "gtrr": lambda: 1 if register_operate[input_a] > register_operate[input_b] else 0, # greater-than register/register
        "eqir": lambda: 1 if input_a == register_operate[input_b] else 0, # equal immediate/register
        "eqri": lambda: 1 if register_operate[input_a] == input_b else 0, # equal register/immediate
        "eqrr": lambda: 1 if register_operate[input_a] == register_operate[input_b] else 0, # equal register/register
    }.get(opcode, lambda: None)()


def build_new_register(opcode: str, input_a: int, input_b: int, output_c: int, register_input: list, ip: int):
    register_operate = register_input[:]
    print("Register before: ", register_input)
    register_operate[output_c] = calculate_output_c(opcode, input_a, input_b, register_operate)
    print("Register after operation: ", register_operate)

    return register_operate


def operate(data_file: list, ip: int, ip_register:int, register: list) ->int:
    while ip < len(data_file):
        register[ip_register] = ip
        opcode, input_a, input_b, output_c = re.split(r"\s", data_file[ip])
        print("ip/line number: ", ip, opcode, input_a, input_b, output_c)
        register = build_new_register(opcode, int(input_a), int(input_b), int(output_c), register, ip)
        ip = register[ip_register] + 1

    return register[0]


def operate_fastlane(data_file: list, ip: int, ip_register:int, register: list) ->int:
    """
    :param data_file: input data
    :param ip: value of instruction pointer
    :param ip_register: number of register for pointer
    :param register: register to start with
    :return: sum of factors = result
    Values of registers in case value of register0 is changig:
    [1, 8, 1, 958, 958, 1]
    [3, 8, 1, 479, 958, 2]
    [482, 8, 1, 2, 958, 479]
    [1440, 8, 1, 1, 958, 958]
    result = sum of values of register5 when changing value of register0,
    equal to factors of maximum value of register4 divided without rest = fastlane
    """

    ip = 0
    maximum_register4: int = 0
    result: int = 0
    while ip < len(data_file):
        register[ip_register] = ip
        register_pointer = register[ip_register]
        opcode, input_a, input_b, output_c = re.split(r"\s", data_file[ip])
        print("ip/line number: ", ip, opcode, input_a, input_b, output_c)
        register = build_new_register(opcode, int(input_a), int(input_b), int(output_c), register, ip)
        if maximum_register4 == register[4] and register[ip_register] < register_pointer:
            # search for maximum value of register4
            break # stop loop when found maximum value of register4
        maximum_register4 = register[4]
        ip = register[ip_register] + 1
    print("\n", "Maximum value of register 4: ", maximum_register4, "\n")
    for i in range(1, maximum_register4+1):
        if maximum_register4 % i == 0: # find factors divided without rest
            result += i

    return result


# ---------- PART ONE ----------

decision: str = input("Solution by fastlane (y/n?")
if decision == "y":
    fastlane = True

data_file = open(path_file).read().split("\n")
ip_string, ip_register = data_file[0].split() # read register for instruction pointer
ip_register = int(ip_register)
data_file = data_file[1:] # cut first line of input

print("Starting part one...\r")

if fastlane == False:
    print("Result part one of register0 ", operate(data_file, ip, ip_register, register))
else:
    print("Result part one of register0 ", operate_fastlane(data_file, ip, ip_register, register))
print("\n")


# ---------- PART TWO ----------

print("Starting part two...\r")

register = [1, 0, 0, 0, 0, 0] # set register 0 to 1
if fastlane == False:
    print("Result part two of register0 ", operate(data_file, ip, ip_register, register))
else:
    print("Result part two of register0 ", operate_fastlane(data_file, ip, ip_register, register))