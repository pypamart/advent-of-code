from pathlib import Path

from collections import Counter

from aoc.year_2024.day_01.input_reader import read_lists

INPUT_FILE = Path(__file__).parent / "resources" / "lists.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    list_1, list_2 = read_lists(filepath)
        
    counter_list_2 = Counter(list_2)
    similarity = sum(value * counter_list_2[value] for value in list_1)

    print("Part II solution: ", similarity)
    return similarity
