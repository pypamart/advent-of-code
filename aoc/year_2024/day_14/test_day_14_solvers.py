from pathlib import Path

from aoc.year_2024.day_14.day_14_solvers import solve_part_1
# , solve_part_2

TEST_FILE_PATH = Path(__file__).parent / "inputs" / "test_robots_positions.txt"
# CHALLENGE_FILE_PATH = Path(__file__).parent / "inputs" / "calibrations.txt"

def test_solve_part1():
    result = solve_part_1(TEST_FILE_PATH.absolute(), (11, 7))
    assert result == 12
    
# def test_solve_part1_challenge():
#     result = solve_part_1(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56506

# def test_solve_part2():
#     result = solve_part_2(TEST_FILE_PATH_PART_2.absolute())
#     assert result == 281
    
# def test_solve_part2_challenge():
#     result = solve_part_2(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56017