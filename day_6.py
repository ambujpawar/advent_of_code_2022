"""
Solution to Day 6 of Advent of Code 2022
"""

from utils.read_input import read_input


def solve_part_1(input_data):
    num_start = 4
    for char in input_data[num_start:]:
        # If all 4 elements of list are different
        if len(set(input_data[num_start - 4:num_start])) == 4:
            print(num_start)
            break

        num_start += 1

    return num_start


def solve_part_2(input_data):
    num_start = 14
    for char in input_data[num_start:]:
        # If all 14 elements of list are different
        if len(set(input_data[num_start - 14:num_start])) == 14:
            print(num_start)
            break

        num_start += 1

    return num_start


def main():
    """
    Main function for Day 6
    """
    input_data = read_input('data/day_6.txt')
    print(f'Part 1: {solve_part_1(input_data[0])}')
    print(f'Part 2: {solve_part_2(input_data[0])}')


if __name__ == '__main__':
    main()
