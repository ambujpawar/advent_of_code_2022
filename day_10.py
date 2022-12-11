"""
Solution to Day 10, Advent of Code 2022
"""

from utils.read_input import read_input


def solve_part_1(input_data):
    cycle_count = 0
    register_x = 1
    values_at_cycle = {}

    for instruction in input_data:
        if 'noop' in instruction:
            cycle_count += 1
            values_at_cycle[cycle_count] = register_x

        elif 'addx' in instruction:
            cycle_count += 1
            values_at_cycle[cycle_count] = register_x
            cycle_count += 1
            values_at_cycle[cycle_count] = register_x

            y = int(instruction.split(' ')[1])
            register_x += y

        else:
            raise ValueError('Unknown instruction')

    count_at = range(20, cycle_count, 40)
    signal_strength = 0
    print(values_at_cycle)

    for cycle in count_at:
        signal_strength += cycle * values_at_cycle[cycle]

    return values_at_cycle, signal_strength


def solve_part_2(values_at_cycle):
    for cycle in range(1, 241, 40):
        crt = ''
        for i in range(cycle, cycle + 40):
            if abs(values_at_cycle[i] - (i - 1) % 40) < 2:
                crt += '#'
            else:
                crt += '.'
        print(crt)


def main():
    input_data = read_input('data/day_10.txt')
    values_at_cycle, answer = solve_part_1(input_data)
    print(f'Part 1: {answer}')
    print(solve_part_2(values_at_cycle))


if __name__ == '__main__':
    main()
