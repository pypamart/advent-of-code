from pathlib import Path

from aoc.year_2024.day_01.part1 import solve as solve_part1
from aoc.year_2024.day_01.part2 import solve as solve_part2

TEST_FILE_PATH = Path(__file__).parent / "resources" / "lists_test.txt"

def test_solve_part1():
    result = solve_part1(TEST_FILE_PATH.absolute())
    assert result == 11


def test_solve_part2():
    result = solve_part2(TEST_FILE_PATH.absolute())
    assert result == 31