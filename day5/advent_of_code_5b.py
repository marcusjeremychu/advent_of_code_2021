# https://adventofcode.com/2021/day/4

PATH = "C:/Users/marcu/Desktop/advent_of_code/day5/input.txt"

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

    # if its diagonal at 45 degrees, ascending
    elif (y1-y0) / (x1-x0) > 0:
        min_x = min(x0, x1)
        max_x = max(x0, x1)
        min_y = min(y0, y1)
        for step in range(0, max_x - min_x + 1):
            inbetween_points.append((min_x + step, min_y + step))

    # if its diagonal at 45 degrees, descending
    elif (y1-y0) / (x1-x0) < 0:
        min_x = min(x0, x1)
        max_x = max(x0, x1)
        max_y = max(y0, y1)
        for step in range(0, max_x - min_x + 1):
            inbetween_points.append((min_x + step, max_y - step))

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

            for point in inbetween_points:
                vent_map[point] = vent_map.get(point, 0) + 1
            
        number_of_overlaps = 0
        for key, value in vent_map.items():
            if value > 1:
                number_of_overlaps += 1
        print(number_of_overlaps)


if __name__ == "__main__":
    main()