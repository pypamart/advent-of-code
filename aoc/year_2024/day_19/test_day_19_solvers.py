from pathlib import Path

from day_19_solvers import Designer, read_patterns

TEST_PATTERNS = read_patterns(Path(__file__).parent / "inputs" / "test_patterns.txt")


def test_brwrr_solver_1():
    print("\nbrwrr")
    designer = Designer(TEST_PATTERNS)
    assert designer.solve("brwrr") != [] 
    