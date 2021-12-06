# https://adventofcode.com/2021/day/6

PATH = "./input.txt"
DAYS = 80

def main():
    with open(PATH) as input_file:
        fish_list = input_file.readlines()[0].split(',')
        fish_array = np.array(list(map(int, fish_list)))
        start = time.time()

        for day in range(0, DAYS):
            fish_array = fish_array - np.ones(fish_array.shape)
            indices = np.where(fish_array < 0)
            fish_array[indices] = 6
            
            if len(indices[0]) > 0:
                new_spawn = 8 * np.ones(indices[0].shape, dtype=np.int32)
                fish_array = np.concatenate([fish_array, new_spawn], axis=None)
            
            print("Day: {}, Number of Fish: {}".format(day, len(fish_array)))
                

if __name__ == "__main__":
    main()