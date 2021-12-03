import os

PATH = "C:/Users/marcu/Desktop/input.txt"
with open(PATH) as input_file:
    lines = input_file.readlines()
    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        value = int(line[-2])
        if line.startswith('f'):
            horizontal += value
            depth += value * aim
        elif line.startswith('d'):
            aim += value
        else: #line strarts with u
            aim -= value
        
print(horizontal * depth)