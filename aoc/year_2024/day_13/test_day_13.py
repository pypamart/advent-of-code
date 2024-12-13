#.__..  .._. __ .  .  .__..  ..__   .__ ._..__ .___..   ,   __..__..   .  ..___.._..__..  .
#|  ||  | | /  `|_/   [__]|\ ||  \  |  \ | [__)  |   \./   (__ |  ||   |  |  |   | |  ||\ |
#|__\|__|_|_\__.|  \  |  || \||__/  |__/_|_|  \  |    |    .__)|__||___|__|  |  _|_|__|| \|
 

from pathlib import Path

from aoc.year_2024.day_13.part1_solver import solve as solve_part1
# from aoc.year_2024.day_01.part2_solver import solve as solve_part2

TEST_FILE_PATH = Path(__file__).parent / "resources" / "behaviors_test.txt"

def test_solve_part1():
    result = solve_part1(TEST_FILE_PATH.absolute())
    assert result == 480


# def test_solve_part2():
#     result = solve_part2(TEST_FILE_PATH.absolute())
#     assert result == 31