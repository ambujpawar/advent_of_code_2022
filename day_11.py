"""
Solution to Day 11, Advent of Code 2022
"""
import math
from typing import List


class Monkey:
    def __init__(
        self,
        monkey_id: int,
        items: List[int],
        operation: str,
        test: int,
        throw_to_if_true: int,
        throw_to_if_false: int,
        lcm: int = 1,
    ):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to_if_true = throw_to_if_true
        self.throw_to_if_false = throw_to_if_false
        self.lcm = lcm
        self.num_inspected = 0

    def turn(self, use_lcm: bool = True):
        items_to_throw = []
        while len(self.items):
            old = self.items.pop(0)
            worry = eval(self.operation)
            if use_lcm:
                # (a+b) % lcm = (a%lcm + b%lcm) % lcm
                # (a*b) % lcm = (a%lcm * b%lcm) % lcm
                worry %= self.lcm
            else:
                # Normal Case
                worry //= 3
            if worry % self.test == 0:
                items_to_throw.append((self.throw_to_if_true, worry))
            else:
                items_to_throw.append((self.throw_to_if_false, worry))

            self.num_inspected += 1
        return items_to_throw


def solve_part_1(monkeys: List[Monkey], turns: int = 20):
    """
    Solve part 1 of the problem
    """
    for turn in range(1, turns + 1):
        for monkey in monkeys:
            throw = monkey.turn(use_lcm=False)
            for recipient, item in throw:
                monkeys[recipient].items.append(item)

    inspected = [monkey.num_inspected for monkey in monkeys]
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]


def solve_part_2(monkeys: List[Monkey], turns: int = 20):
    """
    Solve part 2 of the problem
    """
    all_tests = [monkey.test for monkey in monkeys]
    lcm = math.lcm(*all_tests)
    print(lcm)
    for monkey in monkeys:
        monkey.lcm = lcm

    for turn in range(1, turns + 1):
        for monkey in monkeys:
            throw = monkey.turn(use_lcm=True)
            for recipient, item in throw:
                monkeys[recipient].items.append(item)

    inspected = [monkey.num_inspected for monkey in monkeys]
    inspected.sort(reverse=True)
    return inspected[0]*inspected[1]


def main():
    monkey_0 = Monkey(0, [85, 79, 63, 72], 'old * 17', 2, 2, 6)
    monkey_1 = Monkey(
        1, [53, 94, 65, 81, 93, 73, 57, 92],
        'old * old', 7, 0, 2,
    )
    monkey_2 = Monkey(2, [62, 63], 'old + 7', 13, 7, 6)
    monkey_3 = Monkey(3, [57, 92, 56], 'old + 4', 5, 4, 5)
    monkey_4 = Monkey(4, [67], 'old + 5', 3, 1, 5)
    monkey_5 = Monkey(5, [85, 56, 66, 72, 57, 99], 'old + 6', 19, 1, 0)
    monkey_6 = Monkey(6, [86, 65, 98, 97, 69], 'old * 13', 11, 3, 7)
    monkey_7 = Monkey(7, [87, 68, 92, 66, 91, 50, 68], 'old + 2', 17, 4, 3)

    monkeys = [
        monkey_0, monkey_1, monkey_2, monkey_3,
        monkey_4, monkey_5, monkey_6, monkey_7,
    ]
    # answer = solve_part_1(monkeys, turns=20)
    # print(f"Part 1: {answer}")
    answer = solve_part_2(monkeys, turns=10000)
    print(f'Part 2: {answer}')


if __name__ == '__main__':
    main()
