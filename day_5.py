"""
Solution to Day 5 of Advent of Code 2022
"""
import string
from parse import parse
from utils.read_input import read_input


def get_blocks_from_input(file_path):
    a = open(file_path).read()

    # Every stack of crates is a list with the lowest one
    #  as first element of respective list
    block_list = [[], [], [], [], [], [], [], [], []]
    for line in reversed(a.splitlines()[:8]):
        j = -1
        for i in range(1, len(line), 4):
            j += 1
            if line[i] in set(string.ascii_uppercase):
                block_list[j].append(line[i])

    return block_list


def solve_part_1(moves: list[str], blocks_list: list[list[str]]):
    """Blocks are moved from one stack to another in a reverse order"""
    for move in moves:
        crane_work = parse('move {v1} from {v2} to {v3}', move)
        num_blocks = int(crane_work['v1'])
        move_from = int(crane_work['v2']) - 1
        move_to = int(crane_work['v3']) - 1

        on_crane = blocks_list[move_from][-num_blocks:]
        blocks_list[move_from] = blocks_list[move_from][:-num_blocks]
        blocks_list[move_to].extend(reversed(on_crane))

    end_str = ''
    for stack in blocks_list:
        end_str += str(stack[-1:][0])
    return end_str


def solve_part_2(moves: list[str], blocks_list: list[list[str]]):
    """Blocks are moved from one stack to another in the same stacked order"""
    for move in moves:
        crane_work = parse('move {v1} from {v2} to {v3}', move)
        num_blocks = int(crane_work['v1'])
        move_from = int(crane_work['v2']) - 1
        move_to = int(crane_work['v3']) - 1

        on_crane = blocks_list[move_from][-num_blocks:]
        blocks_list[move_from] = blocks_list[move_from][:-num_blocks]
        blocks_list[move_to].extend(on_crane)

    end_str = ''
    for stack in blocks_list:
        end_str += str(stack[-1:][0])
    return end_str


def main():
    """Main function"""
    filepath = 'data/day_5.txt'
    blocks_list = get_blocks_from_input(filepath)
    moves = read_input(filepath)[10:]

    # print(f"Part 1: {solve_part_1(moves, blocks_list)}")
    print(f'Part 2: {solve_part_2(moves, blocks_list)}')


if __name__ == '__main__':
    main()
