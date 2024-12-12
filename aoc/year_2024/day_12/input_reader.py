from pathlib import Path

def read_map(filepath: Path) -> list[list[str]]:
    with filepath.open("r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]