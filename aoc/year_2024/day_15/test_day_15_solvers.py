from pathlib import Path

from aoc.year_2024.day_15.day_15_solvers import solve_part_1, solve_part_2


TEST_MAP_1_INITIAL_FILE_PATH = Path(__file__).parent / "inputs" / "map_1_initial_state_test.txt"
TEST_MAP_2_INITIAL_FILE_PATH = Path(__file__).parent / "inputs" / "map_2_initial_state_test.txt"
TEST_MAP_1_FINAL_FILE_PATH = Path(__file__).parent / "inputs" / "map_1_final_state_test.txt"
TEST_MAP_2_FINAL_FILE_PATH = Path(__file__).parent / "inputs" / "map_2_final_state_test.txt"
TEST_MOVES_1_FILE_PATH = Path(__file__).parent / "inputs" / "moves_1_test.txt"
TEST_MOVES_2_FILE_PATH = Path(__file__).parent / "inputs" / "moves_2_test.txt"

# def test_solve_part1_litte_map():
#     result = solve_part_1(TEST_MAP_2_INITIAL_FILE_PATH.absolute(), TEST_MOVES_2_FILE_PATH.absolute())
#     assert result == 2028
    
# def test_solve_part1_large_map():
#     result = solve_part_1(TEST_MAP_1_INITIAL_FILE_PATH.absolute(), TEST_MOVES_1_FILE_PATH.absolute())
#     assert result == 10092
    
# def test_solve_part2_litte_map():
#     result = solve_part_2(TEST_MAP_2_INITIAL_FILE_PATH.absolute(), TEST_MOVES_2_FILE_PATH.absolute())
#     assert result == 2028
    
def test_solve_part2_large_map():
    result = solve_part_2(TEST_MAP_1_INITIAL_FILE_PATH.absolute(), TEST_MOVES_1_FILE_PATH.absolute())
    assert result == 9021
    
    
# def test_solve_part1_challenge():
#     result = solve_part_1(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56506

# def test_solve_part2():
#     result = solve_part_2(TEST_FILE_PATH_PART_2.absolute())
#     assert result == 281
    
# def test_solve_part2_challenge():
#     result = solve_part_2(CHALLENGE_FILE_PATH.absolute())
#     assert result == 56017