from pathlib import Path

from aoc.utils.readers import parse_char_vertical_lists_from_text_file

INPUT_FILE = Path(__file__).parent / "resources" / "lists.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    list_1, list_2 = parse_char_vertical_lists_from_text_file(filepath)
    list_1.sort()
    list_2.sort()
    result = sum(map(lambda item: abs(item[0] - item[1]), zip(list_1, list_2)))
    print("Part I solution: ", result)
    return result
