# https://adventofcode.com/2021/day/3
import os

PATH = "C:/Users/marcu/Desktop/advent_of_code/day3/input.txt"

with open(PATH) as input_file:
    lines = input_file.readlines()

    # For each bit position, get count of how many 1s there are
    rate_map = {}
    total = len(lines)
    for line in lines:
        for i, bit in enumerate(line.strip()):
            rate_map[i] = rate_map.get(i, 0) + int(bit == '1')
    
    # Reverse the order of the bits to add at each bit position
    keys = list(rate_map.keys())
    keys.reverse()

    gamma_rate = 0
    epsilon_rate = 0
    # For every bit position, check the ratio of ones/total
    for i, bit in enumerate(keys):
        # If there are less ones than zeroes, add the bit value to epsilon in decimal
        if rate_map[bit] / total < 0.5: 
            epsilon_rate += 2 ** i

        # otherwise, there are less zeroes than ones
        else:
            gamma_rate += 2 ** i
    
    print("gamma_rate: ", gamma_rate)
    print("epsilon_rate: ", epsilon_rate)
    print("power consumption: ", gamma_rate * epsilon_rate)
