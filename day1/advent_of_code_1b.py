import os

PATH = "C:/Users/marcu/Desktop/input.txt"
with open(PATH) as input_file:
    prev_sum = -1
    increase_count = 0
    lines = input_file.readlines()
    for i in range(0, len(lines) - 2):
        measurements = [int(lines[i]), int(lines[i+1]), int(lines[i+2])]
        curr_sum = sum(measurements)
        if curr_sum > prev_sum and prev_sum != -1:
            increase_count += 1
        prev_sum = curr_sum
        
print(increase_count)