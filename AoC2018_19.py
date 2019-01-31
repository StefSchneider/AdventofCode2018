'''
Advent of Code - Day 16
Author: Stefan Schneider
Github: StefSchneider
'''

import re

path_file: str = 'AoC2018_19_data_opcode.txt'

ip: int = 0 # stores value of instruction pointer
ip_register: int = 0 # register manipulated by instruction pointer
register: list = [0, 0, 0, 0, 0, 0]
line: str = ''


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


def build_new_register(opcode: str, input_a: int, input_b: int, output_c: int, register_input: list, ip: int):
    register_operate = register_input[:]
    print('Register before: ', register_input)
    print('Opcode: ', opcode, '| Input A: ', input_a, '| Input B:', input_b, '| Output-Register:', output_c)
    register_operate[output_c] = calculate_output_c(opcode, input_a, input_b, register_operate)
    print('Register after operation: ', register_operate)

    return register_operate





# ---------- PART ONE ----------

print('Starting part one...\r')

data_file = open(path_file).read().split('\n')
ip_string, ip_register = data_file[0].split()
ip_register = int(ip_register)
data_file = data_file[1:]
print(data_file)
while ip < len(data_file):
    print('ip/line number:', ip)
    register[ip_register] = ip
    opcode, input_a, input_b, output_c = re.split(r'\s', data_file[ip])
    print(opcode, input_a, input_b, output_c)
    register = build_new_register(opcode, int(input_a), int(input_b), int(output_c), register, ip)
#    if register[3] > register[ip_register] and register[5] <= register[ip_register]:
#        ip = 12
#        print('SPRUNG AUS SCHLEIFE 1')
#    elif register[5] > register[ip_register]:
#        ip = 16
#        print('SPRUNG AUS SCHLEIFE 2')
#    else:
    ip = register[ip_register]+1

    press_key = input('Taste drücken')
#    if register[5] > register[ip_register]:
#        ip = 16
 #   else:
 #       ip = register[ip_register]+1
print(register[0])