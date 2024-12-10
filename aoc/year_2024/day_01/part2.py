from pathlib import Path

from aoc.year_2024.day_01.input_reader import read_lists

INPUT_FILE = Path(__file__).parent / "resources" / "lists.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    list_1, list_2 = read_lists(filepath)

    similarity = 0
    for value in list_1:
        similarity += value * list_2.count(value)
    
    print("Part II solution: ", similarity)
    return similarity
