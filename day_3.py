"""
Solution to day 3 of Advent of Code 2022.
"""
from utils.read_input import read_input


# Convert character to integer. a is 1, b is 2, etc.
def small_to_int(char):
    return ord(char) - 96

# Convert captial letter to integer. A is 1, B is 2, etc.


def capital_to_int(char):
    return ord(char) - 64 + 26


def split_string(string):
    return string[:len(string)//2], string[len(string)//2:]


def solve_part_1(input_data: list[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    total_score = 0
    for line in input_data:
        first_half, second_half = split_string(line)
        common_letter = list(set(first_half) & set(second_half))
        if common_letter[0].isupper():
            total_score += capital_to_int(common_letter[0])
        else:
            total_score += small_to_int(common_letter[0])
    return total_score


def solve_part_2(input_data: list[str]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    # Merge 3 elements of input_data into 1
    merged_input = []
    total_score = 0

    for i in range(0, len(input_data), 3):
        a = []
        a.append(input_data[i])
        a.append(input_data[i+1])
        a.append(input_data[i+2])
        merged_input.append(a)

    for gift_line in merged_input:
        first, second, third = gift_line
        common = list(set(first) & set(second) & set(third))
        if common[0].isupper():
            total_score += capital_to_int(common[0])
        else:
            total_score += small_to_int(common[0])
    return total_score


def main():
    """
    Main entry point of the script.
    """
    input_data = read_input('data/day_3.txt')
    total_score = solve_part_1(input_data)
    print(f'Part 1: The total score is {total_score}.')

    total_score = solve_part_2(input_data)
    print(f'Part 2: The total score is {total_score}.')


if __name__ == '__main__':
    main()
