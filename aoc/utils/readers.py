from pathlib import Path

from aoc.utils.errors import EmptyFileError


def parse_char_matrix_by_columns_from(filepath: Path, separator=" ") -> list[list[str]]:
    with filepath.open("r") as f:
        lines = f.readlines()

    if not lines:
        raise EmptyFileError(f"File {filepath} is empty.")

    zipped_lists = [line.strip().split(separator) for line in lines]

    # lists = [list(column) for column in zip(*zipped_lists)]
    lists = list(map(list, zip(*zipped_lists)))

    return lists
