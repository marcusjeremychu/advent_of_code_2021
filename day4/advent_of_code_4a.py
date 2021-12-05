# https://adventofcode.com/2021/day/4

PATH = "C:/Users/marcu/Desktop/advent_of_code/day4/input.txt"

def generate_possible_bingos(board):
    solutions = []
    column_solutions = [[] for i in range(0,5)]
    for i, row in enumerate(board):
        solutions.append(row)

        for col in range(0, len(board)):
            column_solutions[col].append(row[i])

    for col_sol in column_solutions:
        solutions.append(col_sol)
    return solutions
        
def calculate_score(remaining_board, draws_so_far):
    board_sum = 0
    for row in remaining_board:
        for val in row:
            if not (val in draws_so_far):
                board_sum += int(val)
    
    return board_sum * int(draws_so_far[-1])

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
                original_boards.append(board)
                board = []

    draws_so_far = []
    for draw in draws:
        draws_so_far.append(draw)
        for i, bingo_state in enumerate(bingo_states):
            for bingo_solution in bingo_state:
                if draw in bingo_solution:
                    bingo_solution.remove(draw)
                    if len(bingo_solution) == 0: # we hit bingo!!!
                        print(calculate_score(original_boards[i], draws_so_far))
                        quit()

            


if __name__ == "__main__":
    main()