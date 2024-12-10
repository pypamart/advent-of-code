from pathlib import Path

def read_lists(filepath: Path) -> tuple[list, list]:
    with filepath.open("r") as f:
        lines = f.readlines()
        zipped_lists = [list(map(int, line.strip().split())) for line in lines] 
        list_1, list_2 = list(zip(*zipped_lists))
        
        return list(list_1), list(list_2)