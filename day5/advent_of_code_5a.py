# https://adventofcode.com/2021/day/4

PATH = "C:/Users/marcu/Desktop/advent_of_code/day5/input.txt"

# Valid only for straight lines
# Returns a list of points between x0,y0 and x1,y1 inclusive
def find_all_inbetween_points(x0,y0,x1,y1):
    inbetween_points = []
      # if its a horizontal line
    if y0 == y1: 
        for x in range(min(x1,x0), max(x1,x0) + 1):
            inbetween_points.append((x, y0))
    # its a vertical line
    elif x0 == x1:
        for y in range(min(y1,y0), max(y1,y0) + 1):
            inbetween_points.append((x0, y))
    
    return inbetween_points


def main():
    with open(PATH) as input_file:
        lines = input_file.readlines()
        vent_map = {}
        for line in lines:
            origin, end = line.strip().split('->')
            x0, y0 = origin.split(",")
            x1, y1 = end.strip().split(",")
            inbetween_points = find_all_inbetween_points(int(x0), int(y0), int(x1), int(y1))

            if len(inbetween_points) != 0: # if not diagonal
                for point in inbetween_points:
                    vent_map[point] = vent_map.get(point, 0) + 1
            
        count = 0
        for key, value in vent_map.items():
            if value > 1:
                count += 1
        print(count)


if __name__ == "__main__":
    main()