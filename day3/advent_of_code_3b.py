# https://adventofcode.com/2021/day/3
import os

PATH = "C:/Users/marcu/Desktop/advent_of_code/day3/input.txt"

# Parameters: - lines = a list of lines of 12 bit values 
# Returns:    The life support rating, which is oxygen rating * co2 rating
def solve_life_support(lines):
    # Start with the full list of lines
    ox_list = lines.copy()
    co_list = lines.copy()

    # Continuosly filter the 12 bit values in the list based on the current bit position
    curr_pos = 0
    while len(ox_list) > 1 or len(co_list) > 1:
        # Count the number of ones in each bit
        rate_map_ox = build_frequency_map(ox_list)
        rate_map_co = build_frequency_map(co_list)

        # Based on the mode at each bit position
        # We need to only keep the relevant 12 bit values in our list
        ox_list = update_list(rate_map_ox, True, ox_list, curr_pos)
        co_list = update_list(rate_map_co, False, co_list, curr_pos)
        curr_pos += 1
    
    return binary_string_to_decimal(ox_list[0]) * binary_string_to_decimal(co_list[0])   

# Paramters: - lines  = a list of lines of 12 bit values 
# For each bit position, get count of how many 1s there are
# Returns a dictionary of keys=bit position and value=counts at bit position
def build_frequency_map(lines):
    rate_map = {}
    for line in lines:
        for i, bit in enumerate(line):
            rate_map[i] = rate_map.get(i, 0) + int(bit == '1')
    return rate_map

# Parameters: - rate_map = the count of 1s at each bit position
#             - isOx = whether its oxygen rating or c02 rating to determine logic
#             - old_list = the current list values in binary           
#             - curr_pos = the current bit position in the value 
# Returns:    A new list depending given the rate_map, the rating type, and the position
def update_list(rate_map, isOx, old_list, curr_pos):
    if len(old_list) == 1:
        return old_list
        
    total = len(old_list)
    new_list = []
    ratio = rate_map[curr_pos] / total
    # equal number of zeroes and ones OR more ones than zeroes
    if ratio == 0.5 or ratio > 0.5:
        if isOx:
            new_list = make_list_at_position(old_list, curr_pos, 1)
        else:
            new_list = make_list_at_position(old_list, curr_pos, 0)
            
    # there are less ones than zeroes
    elif ratio < 0.5:
        if isOx:
            new_list = make_list_at_position(old_list, curr_pos, 0)
        else:
            new_list = make_list_at_position(old_list, curr_pos, 1)

    return new_list

# Parameters: - old_list = the current list values in binary
#             - curr_pos = the current bit position in the value
#             - bit_value = the bit that should match the bit at curr_pos in the list value
# Returns:    A new list based on old_list which only contains values where
#             value[curr_pos] == bit_value
def make_list_at_position(old_list, curr_pos, bit_value):
    new_list = []
    for line in old_list:
        if line[curr_pos] == str(bit_value):
            new_list.append(line)
    return new_list
    
# Converts a binary string to a decimal value
def binary_string_to_decimal(input_string):
    result = 0
    new_str = input_string[::-1]
    for i, bit in enumerate(new_str):
        result += int(bit) * (2 ** i)
    return result

def main():
    with open(PATH) as input_file:
        lines = input_file.readlines()
        life_support = solve_life_support([line.strip() for line in lines])
        print("life support: ", life_support)

if __name__ == "__main__":
    main()