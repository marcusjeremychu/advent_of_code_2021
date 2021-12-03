import os

PATH = "C:/Users/marcu/Desktop/input.txt"
with open(PATH) as input_file:
    lines = input_file.readlines()
    horizontal = 0
    depth = 0

    for line in lines:
        value = int(line[-2])
        if line.startswith('f'):
            horizontal += value
        elif line.startswith('d'):
            depth += value
        else: #line strarts with u
            depth -= value
        
print(horizontal * depth)