from pathlib import Path

from aoc.year_2023.day_01.day_01_solvers import solve_part_1, solve_part_2

TEST_FILE_PATH_PART_1 = Path(__file__).parent / "inputs" / "calibrations_test_part_1.txt"
TEST_FILE_PATH_PART_2 = Path(__file__).parent / "inputs" / "calibrations_test_part_2.txt"
CHALLENGE_FILE_PATH = Path(__file__).parent / "inputs" / "calibrations.txt"

def test_solve_part1():
    result = solve_part_1(TEST_FILE_PATH_PART_1.absolute())
    assert result == 142
    
def test_solve_part1_challenge():
    result = solve_part_1(CHALLENGE_FILE_PATH.absolute())
    assert result == 56506

def test_solve_part2():
    result = solve_part_2(TEST_FILE_PATH_PART_2.absolute())
    assert result == 281
    
def test_solve_part2_challenge():
    result = solve_part_2(CHALLENGE_FILE_PATH.absolute())
    assert result == 56017