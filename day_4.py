"""
Solution to Day 4 of Advent of Code 2022
"""

from utils.read_input import read_input


def solve_part_1(input_data: list[str]):
    """
    Solve part 1 of the puzzle.
    """
    duplicate_pairs = 0

    for line in input_data:
        elf_one, elf_two = line.split(',')
        elf_one_left, elf_one_right = map(int, elf_one.split('-'))
        elf_two_left, elf_two_right = map(int, elf_two.split('-'))

        elf_one_cleans = set(range(elf_one_left, elf_one_right+1))
        elf_two_cleans = set(range(elf_two_left, elf_two_right+1))

        if elf_one_cleans.union(elf_two_cleans) == elf_one_cleans \
                or elf_one_cleans.union(elf_two_cleans) == elf_two_cleans:
            duplicate_pairs += 1

    return duplicate_pairs


def solve_part_2(input_data: list[str]):
    """
    Solve part 2 of the puzzle.
    """
    duplicate_pairs = 0

    for line in input_data:
        elf_one, elf_two = line.split(',')
        elf_one_left, elf_one_right = map(int, elf_one.split('-'))
        elf_two_left, elf_two_right = map(int, elf_two.split('-'))

        elf_one_cleans = set(range(elf_one_left, elf_one_right+1))
        elf_two_cleans = set(range(elf_two_left, elf_two_right+1))

        if elf_one_cleans.intersection(elf_two_cleans):
            duplicate_pairs += 1

    return duplicate_pairs


def main():
    """
    Main function
    """
    input_data = read_input('data/day_4.txt')
    duplicate_pairs = solve_part_1(input_data)
    print(f'Part 1: Total number of duplicate pairs: {duplicate_pairs}')

    duplicate_pairs = solve_part_2(input_data)
    print(f'Part 2: Total number of duplicate pairs: {duplicate_pairs}')


if __name__ == '__main__':
    main()
