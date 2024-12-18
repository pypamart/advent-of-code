from pathlib import Path
import networkx as nx

CORRUPTED_BYTES_FILE_PATH = Path(__file__).parent / "inputs" / "corrupted_bytes.txt"
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

def read_map(corrupted_bytes_coords, grid_size) -> None:
    text = [["."] * (grid_size + 1) for _ in range(grid_size + 1)]
    # print(text)
    for i, j in corrupted_bytes_coords:
        text[i][j] = "#"
    # print("\n".join(["".join(line) for line in text]))
    return text

def read_corrupted_bytes_positions(filepath: Path, nb_corrupted_bytes_to_read=None) -> list[tuple[int, int]]:
    with open(filepath) as f:
        lines = f.readlines()
        
    nb_lines = len(lines) if nb_corrupted_bytes_to_read is None else nb_corrupted_bytes_to_read
    return [list(map(int, line.split(","))) for line in lines[:nb_lines]]


def solve_part_1(corrupted_bytes_filepath: Path=CORRUPTED_BYTES_FILE_PATH.absolute(), nb_corrupted_bytes: int=1024, grid_size: int=70) -> int:
    corrupted_bytes = read_corrupted_bytes_positions(corrupted_bytes_filepath, nb_corrupted_bytes)
    map = read_map(corrupted_bytes, grid_size)

    
    # Create the graph
    nodes = set()
    arcs = {}
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != "#":
                nodes.add((i, j))
    
    for node in nodes:
        for dx, dy in DIRS:
            if (node[0] + dx, node[1] + dy) in nodes:
                arcs[(node, (node[0] + dx, node[1] + dy))] = 1
    
    G = nx.MultiDiGraph()
    G.add_edges_from([(node1, node2) for node1, node2 in arcs.keys()])
    path = nx.shortest_path(G, (0, 0), (grid_size, grid_size))
    # print(path)         
    
    result = len(path) - 1
    print("Part 1: ", result)           
    return result

def solve_part_2(corrupted_bytes_filepath: Path=CORRUPTED_BYTES_FILE_PATH.absolute(), grid_size: int=70) -> int: 
    all_corrupted_bytes = read_corrupted_bytes_positions(corrupted_bytes_filepath)
    
    for k in range(1024, len(all_corrupted_bytes)):
        print(k)
        corrupted_bytes = all_corrupted_bytes[:k]
        map = read_map(corrupted_bytes, grid_size)

    
        # Create the graph
        nodes = set()
        arcs = {}
        for i, row in enumerate(map):
            for j, char in enumerate(row):
                if char != "#":
                    nodes.add((i, j))
        
        for node in nodes:
            for dx, dy in DIRS:
                if (node[0] + dx, node[1] + dy) in nodes:
                    arcs[(node, (node[0] + dx, node[1] + dy))] = 1
        
        G = nx.MultiDiGraph()
        G.add_edges_from([(node1, node2) for node1, node2 in arcs.keys()])
        try:
            path = nx.shortest_path(G, (0, 0), (grid_size, grid_size))
            # print(path)   
        except nx.NetworkXNoPath:
            print("Part 2: ", corrupted_bytes[-1])           
            return corrupted_bytes[-1]     
    
    # result = len(path) - 1
    # print("Part 1: ", result)           
    # return result
    return None


# def solve_part_2(map_filepath: Path=INPUT_MAP_FILE.absolute(), moves_filepath: Path=INPUT_MOVES_FILE.absolute()) -> int:
#     result = None
#     print("Part 2: ", result)           
#     return result


if __name__ == "__main__":
    pass


