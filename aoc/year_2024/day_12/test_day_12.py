from pathlib import Path

from aoc.year_2024.day_12.part1 import solve as solve_part1
from aoc.year_2024.day_12.part2 import solve as solve_part2

TEST_FILE_PATH = Path(__file__).parent / "resources" / "map_test.txt"
TEST_FILE2_PATH = Path(__file__).parent / "resources" / "map_test2.txt"
TEST_FILE_E_SHAPE_PATH = Path(__file__).parent / "resources" / "map_test_e_shape.txt"
TEST_FILE_OX_PATH = Path(__file__).parent / "resources" / "map_test_OX.txt"
TEST_FILE4_PATH = Path(__file__).parent / "resources" / "map_test4.txt"

def test_solve_part1():
    result = solve_part1(TEST_FILE_PATH.absolute())
    assert result == 1930

def test_solve_part2():
    result = solve_part2(TEST_FILE_PATH.absolute())
    assert result == 1206
    
def test_solve_part2_2():
    result = solve_part2(TEST_FILE2_PATH.absolute())
    assert result == 80
    
def test_solve_part2_OX():
    result = solve_part2(TEST_FILE_OX_PATH.absolute())
    assert result == 436

def test_solve_part2_e_shape():
    result = solve_part2(TEST_FILE_E_SHAPE_PATH.absolute())
    assert result == 236
    
def test_solve_part2_4():
    result = solve_part2(TEST_FILE4_PATH.absolute())
    assert result == 368