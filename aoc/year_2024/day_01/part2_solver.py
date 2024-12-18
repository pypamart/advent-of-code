from pathlib import Path

from collections import Counter

from aoc.utils.readers import parse_char_vertical_lists_from_text_file

INPUT_FILE = Path(__file__).parent / "resources" / "lists.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    list_1, list_2 = parse_char_vertical_lists_from_text_file(filepath)
        
    counter_list_2 = Counter(list_2)
    similarity = sum(value * counter_list_2[value] for value in list_1)

    print("Part II solution: ", similarity)
    return similarity
