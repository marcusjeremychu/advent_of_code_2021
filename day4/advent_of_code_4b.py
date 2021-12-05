# https://adventofcode.com/2021/day/4

import copy
import pprint

PATH = "C:/Users/marcu/Desktop/advent_of_code/day4/input.txt"
pp = pprint.PrettyPrinter()

def generate_possible_bingos(board):
    solutions = []
    column_solutions = [[] for i in range(0,5)]
    for i, row in enumerate(board):
        solutions.append(row)

        for col in range(0, len(board)):
            column_solutions[col].append(row[col])

    for col_sol in column_solutions:
        solutions.append(col_sol)
    return solutions
        
def calculate_score(original_board, draws_so_far):
    board_sum = 0
    for row in original_board:
        for val in row:
            if not (val in draws_so_far):
                board_sum += int(val)
    return board_sum * int(draws_so_far[-1])

def search_solutions_for_bingo(bingo_states, draw):
    indices_to_pop = set()
    index = 0
    for bingo_state in bingo_states:
        for bingo_solution in bingo_state:
            if draw in bingo_solution:
                bingo_solution.remove(draw)
                if len(bingo_solution) == 0: # we hit bingo!!!
                    indices_to_pop.add(index)
        index += 1
    return indices_to_pop

def main():
    with open(PATH) as input_file:
        lines = input_file.readlines()
        
        draws = lines[0].split(',')
        lines = lines[2:]

        original_boards = []
        bingo_states = []
        board = []
        lines.append("\n") # address one off error
        for line in lines:
            if line != "\n":
                board.append(line.split())
            else:
                bingos = generate_possible_bingos(board)
                bingo_states.append(bingos)
                original_boards.append(copy.deepcopy(board))
                board = []

    draws_so_far = []

    for i, draw in enumerate(draws):
        draws_so_far.append(draw)
        indices_to_pop = search_solutions_for_bingo(bingo_states, draw)
        
        if len(indices_to_pop) > 0:
            for index in sorted(indices_to_pop, reverse=True):
                original_boards.pop(index)
                bingo_states.pop(index)

            if len(original_boards) == 1:
                break

    # We are now at the last board, but we have to keep drawing until we lose

    for draw in draws[i + 1:]:
        draws_so_far.append(draw)
        for bingo_solution in bingo_states[0]:
            if draw in bingo_solution:
                bingo_solution.remove(draw)
                if len(bingo_solution) == 0: # we hit bingo!!!
                    print(calculate_score(original_boards[0], draws_so_far))
                    quit()
            
    


if __name__ == "__main__":
    main()