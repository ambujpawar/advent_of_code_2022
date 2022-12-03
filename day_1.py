"""
Welcome to the first day of Advent of Code 2022!
"""
from typing import Any, List
from utils.read_input import read_input


def solve_part_1(input_data: List[Any]):
    """
    Iterate through the input
    """
    elf_num = 1
    calories = 0
    max_calories = 0

    for cal in input_data:
        if cal:
            calories += int(cal)
        else:
            if calories > max_calories:
                max_calories = calories
                max_elf = elf_num
            elf_num += 1
            calories = 0

    return max_elf, max_calories


def solve_part_2(input_data: List[Any], k: int = 3):
    """
    Solve part 2 of the puzzle.
    """
    # Find top-k sum of calories
    calories = 0
    calorie_list = []

    for cal in input_data:
        if cal:
            calories += int(cal)
        else:
            calorie_list.append(calories)
            calories = 0

    sorted_calories = sorted(calorie_list, reverse=True)
    return sum(sorted_calories[:k])


def main():
    """
    Main entry point of the script.
    """
    input_data = read_input('data/day_1.txt')
    elf_num, calories = solve_part_1(input_data)
    print(f'Part 1: Elf {elf_num} has {calories} calories with him.')

    top_k_calories = solve_part_2(input_data, k=3)
    print(f'Part 2: The top 3 elves have {top_k_calories} calories with them.')


if __name__ == '__main__':
    main()
