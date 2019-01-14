'''
Advent of Code - Day 16
Author: Stefan Schneider
Github: stefschneider1970
'''

import re
import collections # just for part two

path_file: str = 'AoC2018_16_data_registers.txt'
*samples, _, program = open(path_file).read().split('\n\n')
# use file with data for registers

register_before: list = [0, 0 ,0, 0]
register_after: list = [0, 0, 0, 0]
register_result: list = [0, 0, 0, 0]
register_operate: list = [0, 0, 0, 0]
triple_opcodes: int = 0
library_keys: dict = {}
mapping: dict = {}
delete_code: bool = False
register_zero: int = 0

OPCODES = ['addr', 'addi',
           'mulr', 'muli',
           'banr', 'bani',
           'borr', 'bori',
           'setr', 'seti',
           'gtir', 'gtri', 'gtrr',
           'eqir', 'eqri', 'eqrr']


def calculate_output_c(opcode: str, input_a: int, input_b: int, register_operate):
    return {
        'addr': lambda: register_operate[input_a]+register_operate[input_b], # add register
        'addi': lambda: register_operate[input_a]+input_b, # add immediate
        'mulr': lambda: register_operate[input_a]*register_operate[input_b], # multiply register
        'muli': lambda: register_operate[input_a]*input_b, # multiply immediate
        'banr': lambda: register_operate[input_a]&register_operate[input_b], # bitwise AND register
        'bani': lambda: register_operate[input_a]&input_b, # bitwise AND immediate
        'borr': lambda: register_operate[input_a]|register_operate[input_b], # bitwise OR register
        'bori': lambda: register_operate[input_a]|input_b, # bitwise OR immediate
        'setr': lambda: register_operate[input_a], # set register
        'seti': lambda: input_a, # set immediate
        'gtir': lambda: 1 if input_a > register_operate[input_b] else 0, # greater-than immediate/register
        'gtri': lambda: 1 if register_operate[input_a] > input_b else 0, # greater-than register/immediate
        'gtrr': lambda: 1 if register_operate[input_a] > register_operate[input_b] else 0, # greater-than register/register
        'eqir': lambda: 1 if input_a == register_operate[input_b] else 0, # equal immediate/register
        'eqri': lambda: 1 if register_operate[input_a] == input_b else 0, # equal register/immediate
        'eqrr': lambda: 1 if register_operate[input_a] == register_operate[input_b] else 0, # equal register/register
    }.get(opcode, lambda: None)()


def build_new_register(opcode: str, input_a: int, input_b: int, output_c: int, register_operate):
    register_operate = register_before[:]
    print('Register before: ', register_before)
    print('Opcode: ', OPCODES[command])
    register_operate[output_c] = calculate_output_c(opcode, operation[1], operation[2], register_operate)
    print('Register after operation: ', register_operate)

    return register_operate


def build_lib_keys() -> dict:
    for i in range(0, 16):
        library_keys.setdefault(i, {})
        mapping.setdefault(i, '')

    return library_keys, mapping


# ---------- PART ONE ----------

build_lib_keys() # preparation for part two


print('Starting part one...\r')

for sample in samples:
    register_before, operation, register_after = map(lambda s: list(map(int, re.findall(r'-?\d+', s))), sample.splitlines())
    count_opcodes: int = 0
    for command in range(0, len(OPCODES)):
        print('New operation')
        register_result = build_new_register(OPCODES[command], operation[1], operation[2], operation[3], register_operate)
        if register_result == register_after:
            print('EQUAL REGISTERS AT OPCODE: ', OPCODES[command], operation[0])
            count_opcodes += 1
            set_opcodes = set(library_keys[operation[0]])
            set_opcodes.add(OPCODES[command])
            library_keys[operation[0]] = set_opcodes
    if count_opcodes >= 3:
        triple_opcodes += 1

print('\r')
print('Examples with three or more opcodes: ', triple_opcodes)


# ---------- PART TWO ----------

print('Starting part two...\r')

while len(library_keys) > 0: # assigning opcodes to code numbers
    for number, codes in library_keys.items():
        if len(codes) == 1:
            delete_code = True
            del_code = list(codes)[0]
            del_key = number
            mapping[del_key] = del_code
    if delete_code:
        library_keys.pop(del_key)
        for i in library_keys.values():
            i.discard(del_code)
        delete_code = False

print('Assigned opcodes: ', mapping)

print(mapping[1])

#register_before = [0, 0, 0, 0]

for line in program.splitlines():
    print(line)
    line = (re.split(r'\s', line))
    opcode = mapping[int(line[0])]
    print(int(line[0]), opcode)
    register_before = build_new_register(opcode, int(line[1]), int(line[2]), int(line[3]), register_before)
    print(register_before[0])

