from pathlib import Path

INPUT_MOVES_FILE = Path(__file__).parent / "inputs" / "moves.txt"
INPUT_MAP_FILE = Path(__file__).parent / "inputs" / "map.txt"

MOVES_DIR = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}

def read_moves(filepath: Path) -> list[str]:
    with open(filepath) as f:
        moves = f.read()
    moves = "".join(moves.split("\n")   ) 
    return moves


def read_map(filepath: Path) -> list[list[str]]:
    with filepath.open("r") as f:
        lines = f.readlines()
        
    return [[char for char in line.strip()] for line in lines]

def read_map_v2(filepath: Path) -> list[list[str]]:
    with filepath.open("r") as f:
        lines = f.readlines()
    
    lines = [line.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.") for line in lines if line.strip()]
    
    return [[char for char in line.strip()] for line in lines]

# def update_map(map: list[list[str]], move: str) -> None:
#     # Find the robot position '@'
#     x, y = None, None
#     for i, line in enumerate(map):
#         for j, char in enumerate(line):
#             if char == "@":
#                 x, y = i, j
#                 break
#         if x is not None:
#             break
    
#     # Move the robot
#     is_move_posible = True

def move_item(map: list[list[str]], item_pos: tuple[int, int], move: str, do_move=True) -> bool:
    i, j = item_pos
    di, dj = MOVES_DIR[move]
    item_type = map[i][j]
    
    if item_type in ["#", "."]:
        return False
    else:
        if map[i + di][j + dj] == "#":
            return False
        
        if map[i + di][j + dj] == ".":
            if do_move:
                map[i + di][j + dj] = item_type
                map[i][j] = "."
            return True
        
        if map[i + di][j + dj] == "O": # faudra intégrer can move mais pas besoin pour part II
            has_moved = move_item(map, (i + di, j + dj), move)
            if has_moved:
                map[i + di][j + dj] = item_type
                map[i][j] = "."
                return True
               
        if map[i + di][j + dj] in ["[", "]"]:
            if move in ["<", ">"]:
                has_moved = move_item(map, (i + di, j + dj), move)
                if has_moved:
                    if do_move:
                        map[i + di][j + dj] = item_type
                        map[i][j] = "."
                    return True
            else:
                item_pos = (i + di, j + dj)
                linked_item_pos = (i + di, j + dj + 1) if map[i + di][j + dj] == "[" else (i + di, j + dj - 1)
                
                can_move_1 = move_item(map, item_pos, move, do_move=False)
                can_move_2 = move_item(map, linked_item_pos, move, do_move=False)
                
                # print("Can move!", do_move)
                
                if not can_move_1 or not can_move_2:
                    return False
                
                if not do_move:
                    return True
                
                # Move the 2 items !
                has_moved_1 = move_item(map, item_pos, move, do_move=True)
                has_moved_2 = move_item(map, linked_item_pos, move, do_move=True)
                
                # print("Has moved: ", has_moved_1 and has_moved_2)
                
                if has_moved_1 and has_moved_2:
                    map[i + di][j + dj] = item_type
                    map[i][j] = "."
                    return True
                else:
                    raise Exception("Error")
                
                

                # if can_moved_1 and can_moved_2 and do_move:
                #     has_moved_1 = move_item(map, (i + di, j + dj), move, do_move=True)
                #     if map[i + di][j + dj] == "[":
                #         has_moved_2 = move_item(map, (i + di, j + dj + 1), move, do_move=True)
                #     else:
                #         has_moved_2 = move_item(map, (i + di, j + dj - 1), move, do_move=True)
                #     # move_item(map, (i + di, j + dj), move, do_move=True)
   
                #     if has_moved_1 and has_moved_2:     
                #         map[i + di][j + dj] = item_type
                #         map[i][j] = "."
                    
                    
                #     # show_map(map)
                #     # print("#" * 100)
                #     return True
                # else:
                #     return False

        
        return False
    
def show_map(map: list[list[str]]) -> None:
    # for line in map:
    #     print("".join(line))
    # print("\n")    
    
    text = ""
    for line in map:
        text += "".join(line) + "\n"
    return text
      
def compute_score(i, j) -> int:
    return i * 100 + j

def compute_coordinates_score(map: list[list[str]]) -> int:
    score = 0
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char in ["O", "["]:
                score += compute_score(i, j)
    return score
     

def solve_part_1(map_filepath: Path=INPUT_MAP_FILE.absolute(), moves_filepath: Path=INPUT_MOVES_FILE.absolute()) -> int:
    moves = read_moves(moves_filepath)
    map = read_map(map_filepath)
    
    # Find the robot position '@'
    robot_pos = [None, None]
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == "@":
                robot_pos = [i, j]
                break
        if robot_pos != [None, None]:
            break
    
    for move in moves:
        has_moved = move_item(map, robot_pos, move)
        if has_moved:
            di, dj = MOVES_DIR[move]
            robot_pos[0] += di
            robot_pos[1] += dj
        
    result = compute_coordinates_score(map)
    print("Part 1: ", result)           
    return result

def solve_part_2(map_filepath: Path=INPUT_MAP_FILE.absolute(), moves_filepath: Path=INPUT_MOVES_FILE.absolute()) -> int:
    moves = read_moves(moves_filepath)
    map = read_map_v2(map_filepath)
    # print("Map: ")
    # show_map(map)
   
    with open("output.txt", "w") as f:
        # Find the robot position '@'
        robot_pos = [None, None]
        for i, line in enumerate(map):
            for j, char in enumerate(line):
                if char == "@":
                    robot_pos = [i, j]
                    break
            if robot_pos != [None, None]:
                break
        
        
        for i, move in enumerate(moves):
            has_moved = move_item(map, robot_pos, move)
            f.write(f"Move: {move}\n")
            f.write(show_map(map))
            
            # if move == "^" or moves[i + 1] == "^":
                # print("Move: ", move)
                # show_map(map)
            if has_moved:
                di, dj = MOVES_DIR[move]
                robot_pos[0] += di
                robot_pos[1] += dj
            
    result = compute_coordinates_score(map)
    print("Part 2: ", result)           
    return result


if __name__ == "__main__":
    pass


