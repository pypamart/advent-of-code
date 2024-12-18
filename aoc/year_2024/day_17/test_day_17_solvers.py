from aoc.year_2024.day_17.day_17_solvers import solve_part_1 #, solve_part_2



def test_solve_part1_map_1():
    result = solve_part_1(729, 0, 0, [0,1,5,4,3,0])
    assert result == 0
