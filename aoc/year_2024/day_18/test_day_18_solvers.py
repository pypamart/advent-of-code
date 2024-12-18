from pathlib import Path

from aoc.year_2024.day_18.day_18_solvers import solve_part_1, solve_part_2


TEST_CORRUPTED_BYTES_FILE_PATH = Path(__file__).parent / "inputs" / "test_corrupted_bytes.txt"


def test_solve_part1():
    result = solve_part_1(TEST_CORRUPTED_BYTES_FILE_PATH, nb_corrupted_bytes=12, grid_size=6)
    assert result == 22
    
def test_solve_part2():
    result = solve_part_2(TEST_CORRUPTED_BYTES_FILE_PATH, grid_size=6)
    assert result == [6, 1]