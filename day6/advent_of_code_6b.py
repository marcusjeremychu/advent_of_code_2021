# https://adventofcode.com/2021/day/6

import numpy as np
import time

PATH = "./input.txt"
DAYS = 256

def main():
    with open(PATH) as input_file:
        fish_list = input_file.readlines()[0].split(',')
        fish_list = list(map(int, fish_list))
        fish_counts = [0 for i in range(0, 9)]
        for fish in fish_list:
            fish_counts[fish] += 1
    
        for day in range(0, DAYS):
            print("Day: {}, counts: {}".format(day, fish_counts))
            number_of_new_fish_spawns = fish_counts[0]
            for i in range(0, 8):
                fish_counts[i] = fish_counts[i+1]
            
            fish_counts[6] += number_of_new_fish_spawns
            fish_counts[8] = number_of_new_fish_spawns
            
        print(sum(fish_counts))
            
if __name__ == "__main__":
    main()