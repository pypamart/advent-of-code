from pathlib import Path

import pytest

from aoc.utils.errors import EmptyFileError
from aoc.utils.readers import parse_char_matrix_by_columns_from


RESOURCE_DIRPATH = Path(__file__).parent / "resources"
EMPTY_FILE_FILEPATH = RESOURCE_DIRPATH / "empty_file.txt"
ONE_CHAR_COLUMN_FILEPATH = RESOURCE_DIRPATH / "4x1_char_matrix.txt"
ONE_INT_COLUMN_FILEPATH = RESOURCE_DIRPATH / "4x1_int_matrix.txt"
TW0_CHAR_COLUMNS_FILEPATH = RESOURCE_DIRPATH / "4x2_char_matrix.txt"
TW0_INT_COLUMNS_FILEPATH = RESOURCE_DIRPATH / "4x2_int_matrix.txt"  


def test_parse_empty_file_shall_raise_error(filepath=EMPTY_FILE_FILEPATH):
    with pytest.raises(EmptyFileError):
        parse_char_matrix_by_columns_from(filepath)


def test_parse_char_1_column_char_matrix(filepath=ONE_CHAR_COLUMN_FILEPATH):
    list_1 = parse_char_matrix_by_columns_from(filepath)
    assert list_1[0] == ["A", "b", "1", "#"]
    
    
def test_parse_char_1_column_int_matrix(filepath=ONE_INT_COLUMN_FILEPATH):
    list_1 = parse_char_matrix_by_columns_from(filepath)
    assert list_1[0] == ["1", "2", "3", "4"]
    

def test_parse_char_2_columns_char_matrix(filepath=TW0_CHAR_COLUMNS_FILEPATH,):
    [list_1, list_2] = parse_char_matrix_by_columns_from(filepath)
    assert list_1 == ["A", "b", "1", "#"]
    assert list_2 == ["c", "2", "@", "D"]
    
    
def test_parse_char_2_columns_int_matrix(filepath=TW0_INT_COLUMNS_FILEPATH,):
    [list_1, list_2] = parse_char_matrix_by_columns_from(filepath)
    assert list_1 == ["11", "21", "31", "41"]
    assert list_2 == ["12", "22", "32", "42"]

