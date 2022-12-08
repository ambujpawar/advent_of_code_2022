"""
Solution to Day 8, Advent of Code 2022
"""

from utils.read_input import read_input_as_grid


def solve_part_1(input_data):
    """
    Read part 1 as a grid of 5*5 and count the number of trees visible.
    The input data represents height of a tree.
    Tree is only visible if:
    1. Its higher than the trees between in and an edge of the grid
    2. If its at an edge
    """
    trees_visible = 0
    shape = (len(input_data), len(input_data[0]))

    def is_tree_visible(x: int, y: int, grid: any) -> bool:
        """ Check if a tree is visible"""
        tree_height = grid[x][y]
        if x == 0 or y == 0:
            return True
        elif x == shape[0] - 1 or y == shape[1] - 1:
            return True
        else:
            fix_row = x
            fix_column = y
            # If all the trees to the left are shorter than the current one
            # then the tree is visible
            all_trees_left = [grid[fix_row][col] for col in range(0, y)]
            all_trees_right = [
                grid[fix_row][col]
                for col in range(y+1, shape[1])
            ]
            all_trees_top = [grid[row][fix_column] for row in range(0, x)]
            all_trees_bottom = [
                grid[row][fix_column]
                for row in range(x+1, shape[1])
            ]

            if tree_height > max(all_trees_left):
                return True
            # If all the trees to the right are shorter than the current one
            # then the tree is visible
            if tree_height > max(all_trees_right):
                return True

            # If all the trees to the top are shorter than the current one
            # then the tree is visible
            if tree_height > max(all_trees_top):
                return True

            # If all the trees to the bottom are shorter than the current one
            # then the tree is visible
            if tree_height > max(all_trees_bottom):
                return True
            return False

    for row in range(0, shape[0]):
        for column in range(0, shape[1]):
            if is_tree_visible(row, column, input_data):
                trees_visible += 1

    return trees_visible


def solve_part_2(input_data):
    shape = (len(input_data), len(input_data[0]))

    def _num_trees_visible(tree_height, list_trees):
        num_trees_visible = 1
        if len(list_trees) == 1:
            return 1

        if tree_height > max(list_trees):
            return len(list_trees)

        for tree in list_trees:
            if tree_height > tree:
                num_trees_visible += 1
            else:
                break
        return num_trees_visible

    def _compute_tree_score(x: int, y: int, grid: any) -> bool:
        """ Check if a tree is visible"""
        tree_height = grid[x][y]
        if x == 0 or y == 0:
            return 0
        elif x == shape[0] - 1 or y == shape[1] - 1:
            return 0
        else:
            fix_row = x
            fix_column = y
            trees_to_left = 0
            trees_to_right = 0
            trees_to_top = 0
            trees_to_bottom = 0

            # Calculate the number of trees visible to the left
            # Reverse traverse the list to compute the number of trees visible
            all_trees_left = [grid[fix_row][col] for col in range(0, y)]
            reversed_all_trees_left = all_trees_left[::-1]
            trees_to_left = _num_trees_visible(
                tree_height, reversed_all_trees_left,
            )

            # Calculate the number of trees visible to the right
            # No need to reverse the list when traversing right
            all_trees_right = [
                grid[fix_row][col]
                for col in range(y+1, shape[1])
            ]
            trees_to_right = _num_trees_visible(tree_height, all_trees_right)

            # Calculate the number of trees visible to the top
            # Reverse traverse the list to compute the number of trees visible
            all_trees_top = [grid[row][fix_column] for row in range(0, x)]
            reversed_all_trees_top = all_trees_top[::-1]
            trees_to_top = _num_trees_visible(
                tree_height, reversed_all_trees_top,
            )

            all_trees_bottom = [
                grid[row][fix_column]
                for row in range(x+1, shape[1])
            ]
            trees_to_bottom = _num_trees_visible(tree_height, all_trees_bottom)

            score = trees_to_left*trees_to_right*trees_to_top*trees_to_bottom
            return score

    max_tree_score = 0
    for row in range(0, shape[0]):
        for column in range(0, shape[1]):
            tree_score = _compute_tree_score(row, column, input_data)
            if tree_score > max_tree_score:
                max_tree_score = tree_score
    return max_tree_score


def main():
    input_data = read_input_as_grid('data/day_8.txt')
    trees_visible = solve_part_1(input_data)
    print(f'Part 1: {trees_visible}')
    tree_scores = solve_part_2(input_data)
    print(f'Part 2: {tree_scores}')


if __name__ == '__main__':
    main()
