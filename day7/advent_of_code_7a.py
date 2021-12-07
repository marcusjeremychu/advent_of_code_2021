# https://adventofcode.com/2021/day/6

PATH = "./input.txt"

def main():
    with open(PATH) as input_file:
        crab_positions = input_file.readlines()[0].split(',')
        
        min_fuel = float('inf')
        for goal_pos in range(0, len(crab_positions)):
            curr_fuel = 0
            for crab_pos in crab_positions:
                curr_fuel += abs(goal_pos - int(crab_pos))

            if curr_fuel < min_fuel:
                min_fuel = curr_fuel

        print("Minimum Fuel Cost: ", min_fuel)

if __name__ == "__main__":
    main()