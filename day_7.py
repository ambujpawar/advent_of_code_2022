"""
Solution to Day 7 of Advent of Code 2022
"""

from utils.read_input import read_input

TOTAL_SIZE = 70000000
REQUIRED_SIZE = 30000000

part1_size = 0
dir_sizes = []


def construct_tree_dir(input_data):
    filesystem = {}
    current_path = [filesystem]
    for line in input_data:
        # If the line starts with a $, it's a command
        if '$' in line:
            # If the command is cd, change the current path
            if 'cd' in line:
                if 'cd ..' in line:
                    current_path.pop()
                elif 'cd /' in line:
                    current_path = [filesystem]
                else:
                    current_path.append(current_path[-1][line.split(' ')[-1]])
        elif 'dir' in line:
            current_path[-1][line.split(' ')[-1]] = {}
        else:
            size, name = line.split()
            current_path[-1][name] = int(size)
    return filesystem


def sum_files_in_directory(tree_dir: dict):
    total_size = 0
    global part1_size

    for item in tree_dir.values():
        if isinstance(item, int):
            total_size += item
        else:
            total_size += sum_files_in_directory(item)

    if total_size <= 100000:
        part1_size += total_size

    dir_sizes.append(total_size)
    return total_size


def solve_part_1(tree_dir: dict):
    """"
    Solution to Part 1 of Day 7
    """
    sum_files_in_directory(tree_dir)
    return part1_size


def solve_part_2(tree_dir: dict):
    """"
    Solution to Part 2 of Day 7
    """
    root_dir_space = sum_files_in_directory(tree_dir)
    free_space = TOTAL_SIZE - root_dir_space
    space_needed = REQUIRED_SIZE - free_space
    sorted_dir_sizes = sorted(dir_sizes)

    for dir_size in sorted_dir_sizes:
        if dir_size > space_needed:
            dir_size_to_delete = dir_size
            break
    return dir_size_to_delete


def main():
    input_data = read_input('data/day_7.txt')
    tree_dir = construct_tree_dir(input_data)
    print(f'Part 1: {solve_part_1(tree_dir)}')
    print(f'Part 2: {solve_part_2(tree_dir)}')


if __name__ == '__main__':
    main()
