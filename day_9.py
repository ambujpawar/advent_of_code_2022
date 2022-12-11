from utils.read_input import read_input

tail_moves = {
    (0, 2): (0, 1),  # R
    (0, -2): (0, -1),  # L
    (2, 0): (1, 0),  # U
    (-2, 0): (-1, 0),  # D

    (1, -2): (1, -1),  # UL
    (1, 2): (1, 1),  # UR
    (-1, 2): (-1, 1),  # DR
    (-1, -2): (-1, -1),  # DL
    (2, 1): (1, 1),  # RU
    (2, -1): (1, -1),  # LU
    (-2, 1): (-1, 1),  # RD
    (-2, -1): (-1, -1),  # LD
    (2, 2): (1, 1),
    (2, -2): (1, -1),
    (-2, 2): (-1, 1),
    (-2, -2): (-1, -1),
}


def solve_part_1(input_data):
    visited = set()
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    for line in input_data:
        direction, steps = line[0], int(line[1:])
        for _ in range(steps):
            if direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'R':
                head_x += 1
            else:
                raise ValueError('Invalid direction')

            # Move tail
            if (max(abs(head_x-tail_x), abs(head_y-tail_y)) > 1):
                diff = (head_x-tail_x, head_y-tail_y)
                tail_x += tail_moves[diff][0]
                tail_y += tail_moves[diff][1]

            visited.add((tail_x, tail_y))
    return len(visited)


def solve_part_2(input_data):
    visited = set()

    # 0 is head, 9 is tail
    all_knots = [(0, 0) for i in range(10)]

    for line in input_data:
        direction, steps = line[0], int(line[1:])
        for _ in range(steps):
            if direction == 'U':
                all_knots[0] = (all_knots[0][0], all_knots[0][1] + 1)
            elif direction == 'D':
                all_knots[0] = (all_knots[0][0], all_knots[0][1] - 1)
            elif direction == 'L':
                all_knots[0] = (all_knots[0][0] - 1, all_knots[0][1])
            elif direction == 'R':
                all_knots[0] = (all_knots[0][0] + 1, all_knots[0][1])
            else:
                raise ValueError('Invalid direction')

            # Move tail
            for i in range(1, 10):
                if max(
                    abs(all_knots[i-1][0] - all_knots[i][0]),
                    abs(all_knots[i-1][1] - all_knots[i][1]),
                ) > 1:
                    diff = (
                        all_knots[i-1][0] - all_knots[i]
                        [0], all_knots[i-1][1] - all_knots[i][1],
                    )
                    all_knots[i] = (
                        all_knots[i][0] + tail_moves[diff]
                        [0], all_knots[i][1] + tail_moves[diff][1],
                    )

            visited.add(all_knots[9])

    return len(visited)


def main():
    input_data = read_input('data/day_9.txt')
    print(f'Part 1: {solve_part_1(input_data)}')
    print(f'Part 2: {solve_part_2(input_data)}')


if __name__ == '__main__':
    main()
