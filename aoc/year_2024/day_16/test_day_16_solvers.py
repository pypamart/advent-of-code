from pathlib import Path

from aoc.year_2024.day_16.day_16_solvers import solve_part_1, solve_part_2


TEST_MAP_1_PATH = Path(__file__).parent / "inputs" / "test_map_1.txt"
TEST_MAP_2_PATH = Path(__file__).parent / "inputs" / "test_map_2.txt"

# def test_solve_part1_map_1():
#     result = solve_part_1(TEST_MAP_1_PATH.absolute())
#     assert result == 7036
    
# def test_solve_part1_map_2():
#     result = solve_part_1(TEST_MAP_2_PATH.absolute())
#     assert result == 11048
    
def test_solve_part2_map_1():
    result = solve_part_2(TEST_MAP_1_PATH.absolute())
    assert result == 45
    
# def test_solve_part2_map_2():
#     result = solve_part_2(TEST_MAP_2_PATH.absolute())
#     assert result == 64
    
# def test_solve_part1_large_map():
#     result = solve_part_1(TEST_MAP_1_INITIAL_FILE_PATH.absolute(), TEST_MOVES_1_FILE_PATH.absolute())
#     assert result == 10092
    
# def test_solve_part2_litte_map():
#     result = solve_part_2(TEST_MAP_2_INITIAL_FILE_PATH.absolute(), TEST_MOVES_2_FILE_PATH.absolute())
#     assert result == 2028
    
# def test_solve_part2_large_map():
#     result = solve_part_2(TEST_MAP_1_INITIAL_FILE_PATH.absolute(), TEST_MOVES_1_FILE_PATH.absolute())
#     assert result == 9021
    
    
# def test_solve_part1_challenge():
#     result = solve_part_1(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56506

# def test_solve_part2():
#     result = solve_part_2(TEST_FILE_PATH_PART_2.absolute())
#     assert result == 281
    
# def test_solve_part2_challenge():
#     result = solve_part_2(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56017