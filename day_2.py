"""
Solution to Day 2 of Advent of Code 2022.
"""
from enum import Enum
from utils.read_input import read_input


OPPONENT_MOVE = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
}

YOUR_MOVE = {
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS',
}


class GameResult(int, Enum):
    """
    Enum representing the result of a game.
    """
    WIN = 6
    LOSS = 0
    DRAW = 3


EXPECTED_RESULT = {
    'X': GameResult.LOSS,
    'Y': GameResult.DRAW,
    'Z': GameResult.WIN,
}


class MoveScore(int, Enum):
    """
    Enum representing the extra score for a game.
    """
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def main():
    """
    Main entry point of the script.
    """
    input_data = read_input('data/day_2.txt')
    total_score = solve_part_1(input_data)
    print(f'Part 1: The total score is {total_score}.')

    total_score = solve_part_2(input_data)
    print(f'Part 2: The total score is {total_score}.')


def solve_part_1(input_data: list[str]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    score = 0
    for game in input_data:
        opponent_move, your_move = game.split(' ')
        # Read move from enum
        opponent_move = OPPONENT_MOVE[opponent_move]
        your_move = YOUR_MOVE[your_move]
        if your_move == opponent_move:
            score += GameResult.DRAW.value + MoveScore[your_move]
        elif your_move == 'ROCK' and opponent_move == 'SCISSORS':
            score += GameResult.WIN.value + MoveScore.ROCK.value
        elif your_move == 'PAPER' and opponent_move == 'ROCK':
            score += GameResult.WIN.value + MoveScore.PAPER.value
        elif your_move == 'SCISSORS' and opponent_move == 'PAPER':
            score += GameResult.WIN.value + MoveScore.SCISSORS.value
        else:
            score += GameResult.LOSS.value + MoveScore[your_move]
    return score


def solve_part_2(input_data: list[str]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    score = 0
    for game in input_data:
        opponent_move, game_result = game.split(' ')
        opponent_move = OPPONENT_MOVE[opponent_move]
        game_result = EXPECTED_RESULT[game_result]
        # Read move from enum
        if game_result == GameResult.DRAW:
            score += GameResult.DRAW.value + MoveScore[opponent_move]
        elif game_result == GameResult.WIN:
            if opponent_move == 'ROCK':
                score += GameResult.WIN.value + MoveScore.PAPER.value
            elif opponent_move == 'PAPER':
                score += GameResult.WIN.value + MoveScore.SCISSORS.value
            elif opponent_move == 'SCISSORS':
                score += GameResult.WIN.value + MoveScore.ROCK.value
        elif game_result == GameResult.LOSS:
            if opponent_move == 'ROCK':
                score += GameResult.LOSS.value + MoveScore.SCISSORS.value
            elif opponent_move == 'PAPER':
                score += GameResult.LOSS.value + MoveScore.ROCK.value
            elif opponent_move == 'SCISSORS':
                score += GameResult.LOSS.value + MoveScore.PAPER.value
    return score


if __name__ == '__main__':
    main()
