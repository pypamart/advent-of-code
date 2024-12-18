from pathlib import Path

INPUT_FILE = Path(__file__).parent / "resources" / "XXXX.txt"


def read_input(filepath: Path=INPUT_FILE.absolute()) -> str:
    with open(filepath) as f:
        return f.readlines()


def solve_part_1(filepath: Path=INPUT_FILE.absolute()) -> int:
    lines = read_input(filepath)
    result = "TODO"
    print("Part I solution: ", result)
    return result


def solve_part_2(filepath: Path=INPUT_FILE.absolute()) -> int:
    lines = read_input(filepath)
    result = "TODO"
    print("Part I solution: ", result)
    return result


if __name__ == "__main__":
    pass