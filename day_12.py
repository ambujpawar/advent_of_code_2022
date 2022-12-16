""""
Solution to Day 12 of Advent of Code 2022.

Use BFS to find the shortest path
"""

from collections import deque
from utils.read_input import read_input


def make_grid(filepath: str):
    """
    Make a grid from the input file
    """
    grid = [list(line) for line in read_input(filepath)]
    start_pos, end_pos = [0, 0], [0, 0]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                grid[r][c] = 0
                start_pos = [r, c]
            elif grid[r][c] == 'E':
                grid[r][c] = 25
                end_pos = [r, c]
            else:
                grid[r][c] = ord(grid[r][c]) - ord('a')
    return (start_pos, end_pos, grid)


def breadth_first_search(start_pos, end_pos, grid_data):
    """"
    BFS algorithm: https://en.wikipedia.org/wiki/Breadth-first_search
    Finding the shortest path
    """
    queue = deque([(0, start_pos)])
    valid_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set((start_pos[0], start_pos[1]))
    rows, cols = len(grid_data), len(grid_data[0])

    # Breadth first search
    while queue:
        num_steps, current_pos = queue.popleft()
        if current_pos == end_pos:
            return num_steps

        curr_r, curr_c = current_pos

        for r_inc, c_inc in valid_moves:
            new_r, new_c = curr_r + r_inc, curr_c + c_inc
            if 0 <= new_r < rows and 0 <= new_c < cols and \
                    grid_data[new_r][new_c] <= grid_data[curr_r][curr_c] + 1 and \
                    (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((num_steps + 1, [new_r, new_c]))

    # return -1 # Leaving it here to reference my stupid mistake
    return float('inf')


def solve_part_1(input_data):
    """
    Solve part 1 of the problem
    """
    start_pos, end_pos, grid_data = input_data
    return breadth_first_search(start_pos, end_pos, grid_data)


def solve_part_2(input_data):
    """
    Solve part 2 of the problem
    """
    min_distance = float('inf')
    start_pos, end_pos, grid_data = input_data
    rows, cols = len(grid_data), len(grid_data[0])
    for i in range(rows):
        for j in range(cols):
            if grid_data[i][j] == 0:
                distance = breadth_first_search([i, j], end_pos, grid_data)
                if distance < min_distance:
                    min_distance = distance
    return min_distance


def main():
    """
    Main function
    """
    input_data = make_grid('data/day_12.txt')
    print(solve_part_1(input_data))
    input_data = make_grid('data/day_12.txt')
    print(solve_part_2(input_data))


if __name__ == '__main__':
    main()
