from pathlib import Path
import networkx as nx

INPUT_MAP_FILEPATH = Path(__file__).parent / "inputs" / "map.txt"


def read_map(filepath: Path) -> list[list[str]]:
    with filepath.open("r") as f:
        lines = f.readlines()
     
    return [[char for char in line.strip()] for line in lines]


def solve_part_1(map_filepath: Path=INPUT_MAP_FILEPATH.absolute()) -> int:
    map = read_map(map_filepath)
    
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left 
    
    # Create the graph
    nodes = set()
    arcs = {}
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != "#":
                for k, (dx, dy) in enumerate(DIRS):
                    nodes.add((i, j, k))
                    
                    if map[i + dx][j + dy] != "#":
                        nodes.add((i + dx, j + dy, k))
                        arcs[((i, j, k), (i + dx, j + dy, k))] = 1
                        
                arcs[((i, j, 1), (i, j, 2))] = 1000
                arcs[((i, j, 2), (i, j, 1))] = 1000
                arcs[((i, j, 2), (i, j, 3))] = 1000
                arcs[((i, j, 3), (i, j, 2))] = 1000
                arcs[((i, j, 3), (i, j, 0))] = 1000
                arcs[((i, j, 0), (i, j, 3))] = 1000
                arcs[((i, j, 0), (i, j, 1))] = 1000
                arcs[((i, j, 1), (i, j, 0))] = 1000

            if char == "S":
                starting_node = (i, j, 1)
                
            if char == "E":
                ending_node = (i, j, 0)
                
    G = nx.MultiDiGraph()
    G.add_weighted_edges_from([(node1, node2, value) for (node1, node2), value in arcs.items()])
    path = nx.dijkstra_path(G, starting_node, ending_node)
    print(path)         
    
    score = 0
    for i in range(1, len(path)):
        node_1 = path[i - 1]
        node_2 = path[i]
        # coords_1 = (node_1[0], node_1[1])
        # coords_2 = (node_2[0], node_2[1])
        
        score += arcs[(node_1, node_2)]
        
        if node_2[0] == ending_node[0] and node_2[1] == ending_node[1]:
            break 
    
    print("len(path): ", len(path))
    
    print("Part 1: ", score)           
    return score

def solve_part_2(map_filepath: Path=INPUT_MAP_FILEPATH.absolute()) -> int:
    map = read_map(map_filepath)
    
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left 
    
    # Create the graph
    nodes = set()
    arcs = {}
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != "#":
                for k, (dx, dy) in enumerate(DIRS):
                    nodes.add((i, j, k))
                    
                    if map[i + dx][j + dy] != "#":
                        nodes.add((i + dx, j + dy, k))
                        arcs[((i, j, k), (i + dx, j + dy, k))] = 1
                        
                arcs[((i, j, 1), (i, j, 2))] = 1000
                arcs[((i, j, 2), (i, j, 1))] = 1000
                arcs[((i, j, 2), (i, j, 3))] = 1000
                arcs[((i, j, 3), (i, j, 2))] = 1000
                arcs[((i, j, 3), (i, j, 0))] = 1000
                arcs[((i, j, 0), (i, j, 3))] = 1000
                arcs[((i, j, 0), (i, j, 1))] = 1000
                arcs[((i, j, 1), (i, j, 0))] = 1000

            if char == "S":
                starting_node = (i, j, 1)
                
            if char == "E":
                ending_node = (i, j, 0)
               
    G = nx.MultiDiGraph()
    G.add_weighted_edges_from([(node1, node2, value) for (node1, node2), value in arcs.items()])
    optimal_path = nx.dijkstra_path(G, starting_node, ending_node)
    
    
    best_score = None
    best_path = None
    for path in nx.all_simple_paths(G, source=starting_node, target=ending_node, cutoff=len(optimal_path)):
        score = 0
        for i in range(1, len(path)):
            node_1 = path[i - 1]
            node_2 = path[i]
            score += arcs[(node_1, node_2)]  
            if node_2[0] == ending_node[0] and node_2[1] == ending_node[1]:
                break 
        print("score: ", score) 
        
        if best_score is None or score < best_score:
            best_score = score
            best_path = [path]
        elif score == best_score:
            best_path.append(path)
    
    seats = set()
    for path in best_path:
        for node in path:
            seats.add((node[0], node[1]))
            
    print("seats: ", len(seats))
        
    # print("len(path): ", len(path))
    
 
    
    
    print("Part 2: ", len(seats))           
    return len(seats)


if __name__ == "__main__":
    pass


