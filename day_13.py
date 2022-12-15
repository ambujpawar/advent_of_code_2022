"""
Solution to Advent of Code 2022, Day 13.
"""
from typing import Union


def parse_input(filepath: str):
    """
    Parse the input data
    """
    with open(filepath, 'r') as f:
        raw = f.read().split('\n\n')
    input_data = []
    for i in raw:
        a, b = i.split('\n')
        input_line = []
        input_line.append(eval(a))
        input_line.append(eval(b))
        input_data.append(input_line)
    return input_data


def compare(x: Union[int, list], y: Union[int, list]):
    """
    Compare two values
    """
    max_len = max(len(x), len(y))
    for index in range(max_len):
        if index == len(x) and index < len(y):
            return True
        if index < len(x) and index == len(y):
            return False

        x_val = x[index]
        y_val = y[index]
        if isinstance(x_val, int) and isinstance(y_val, int):
            if x_val < y_val:
                return True
            if x_val > y_val:
                return False
        elif isinstance(x_val, list) and isinstance(y_val, list):
            result = compare(x_val, y_val)
            if result is not None:
                return result

        elif isinstance(x_val, int) and isinstance(y_val, list):
            result = compare([x_val], y_val)
            if result is not None:
                return result

        elif isinstance(x_val, list) and isinstance(y_val, int):
            result = compare(x_val, [y_val])
            if result is not None:
                return result
    return None


def solve_part_1(input_data):
    """
    Solve part 1 of the problem
    """
    pairs_in_order = 0
    for index, (a, b) in enumerate(input_data):
        if compare(a, b):
            pairs_in_order += index + 1
    return pairs_in_order


def solve_part_2(input_data):
    """
    Solve part 2 of the problem
    """
    input_for_second_part = []
    for a, b in input_data:
        input_for_second_part.append(a)
        input_for_second_part.append(b)

    index_2 = 1
    index_6 = 2

    for elem in input_for_second_part:
        # Just find the index of the first occurence of 2 and 6
        if compare(elem, [[2]]):
            index_2 += 1
            index_6 += 1
        elif compare(elem, [[6]]):
            index_6 += 1

    return index_2 * index_6


def main():
    input_data = parse_input('data/day_13.txt')
    print(f'Part 1: {solve_part_1(input_data)}')
    print(f'Part 2: {solve_part_2(input_data)}')


if __name__ == '__main__':
    main()
