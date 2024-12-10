from pathlib import Path

from aoc.year_2024.day_01.input_reader import read_lists

INPUT_FILE = Path(__file__).parent / "resources" / "lists.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    list_1, list_2 = read_lists(filepath)
    list_1.sort()
    list_2.sort()
    result = sum(map(lambda item: abs(item[0] - item[1]), zip(list_1, list_2)))
    print("Part I solution: ", result)
    return result
