from pathlib import Path

INPUT_FILE = Path(__file__).parent / "inputs" / "robots_positions.txt"

class Robot:
    def __init__(self, x: int, y: int, vx: int, vy: int):
        self.__x = x
        self.__y = y
        self.__vx = vx
        self.__vy = vy
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    def move(self, map_size: tuple[int, int]):
        self.__x = (self.__x + self.__vx) % map_size[0]    
        self.__y = (self.__y + self.__vy) % map_size[1]
        
    def __str__(self):
        return f"Robot at {self.__x}, {self.__y} with speed {self.__vx}, {self.__vy}"
        
def read_input(filepath: Path=INPUT_FILE.absolute()) -> str:
    with open(filepath) as f:
        lines = f.readlines()

    robots = []
    for line in lines:
        x_block, v_block = line.split()
        x = int(x_block[2:].split(",")[0])
        y = int(x_block[2:].split(",")[1])
        vx = int(v_block[2:].split(",")[0])
        vy = int(v_block[2:].split(",")[1])
        robots.append(Robot(x, y, vx, vy))
              
    return robots
    

def compute_score(robots: list[Robot], map_size: tuple[int, int]) -> int:
    nb_robots = [0, 0, 0, 0]
    middle = (map_size[0] // 2, map_size[1] // 2)
    for robot in robots:
        if robot.x < middle[0] and robot.y < middle[1]:
            nb_robots[0] += 1
        elif robot.x > middle[0] and robot.y < middle[1]:
            nb_robots[1] += 1
        elif robot.x < middle[0] and robot.y > middle[1]:
            nb_robots[2] += 1
        elif robot.x > middle[0] and robot.y > middle[1]:
            nb_robots[3] += 1
    return nb_robots[0] * nb_robots[1] * nb_robots[2] * nb_robots[3]

def are_robots_in_positions_like_christmas_tree(robots: list[Robot], map_size: tuple[int, int], epoc) -> bool:
    map = [[0 for _ in range(map_size[1])] for _ in range(map_size[0])]
    for robot in robots:
        map[robot.x][robot.y] += 1
        
    map2 = [["." for _ in range(map_size[1])] for _ in range(map_size[0])]
    for robot in robots:
        map2[robot.x][robot.y] = "#"
    
    # Check if map2 is symetric
    is_symetric = True
    for i in range(map_size[0] // 2):
        for j in range(map_size[1]):
            if map2[i][j] != map2[map_size[0] - i - 1][j]:
                is_symetric = False
                break
        if not is_symetric:
            break
            
    if not is_symetric:
        # Check other axe
        is_symetric = True
        for i in range(map_size[0]):
            for j in range(map_size[1] // 2):
                if map2[i][j] != map2[i][map_size[1] - j - 1]:
                    is_symetric = False
                    break
            if not is_symetric:
                break
            
    if is_symetric:
    # Else print epoc and the map
        print("Epoc: ", epoc)
        for line in map2:
            print("".join(line))
        
        
    # middle = (map_size[0] // 2, map_size[1] // 2)
    
    # # if map[middle[0]][0] == 1 and sum([line[0] for line in map]) == 1:
    # if map[middle[0]] == [1] * map_size[1]:
    #     # Print the map
    #     print("Epoc: ", epoc)
        
    #     map2 = [["." for _ in range(map_size[1])] for _ in range(map_size[0])]
    #     for robot in robots:
    #         map2[robot.x][robot.y] = "#"
    #     map2[middle[0]][0] = "O"
        
    #     for line in map2:
    #         print("".join(line))
    
    return False

def compute_neightbourood(robots: list[Robot]):
    positions = []
    for robot in robots:
        positions.append((robot.x, robot.y))

    score = 0
    positions_to_control = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for robot in robots:
        nb_neighbour = 0
        for position in positions_to_control:
            if (robot.x + position[0], robot.y + position[1]) in positions:
                nb_neighbour += 1
        
        score += nb_neighbour
        
    return score
    
def print_map(robots: list[Robot], map_size: tuple[int, int], epoc: int):
    map = [["." for _ in range(map_size[0])] for _ in range(map_size[1])]
    for robot in robots:
        map[robot.y][robot.x] = "#"
        
    for line in map:
        print("".join(line))
    
    return map

def solve_part_1(filepath: Path=INPUT_FILE.absolute(), map_size: tuple[int, int]=(101, 103)) -> int:
    robots = read_input(filepath)
    for _ in range(100):
        for robot in robots:
            robot.move(map_size)
    
    score = compute_score(robots, map_size)
    print("Part I solution: ", score)
    return score

def solve_part_2(filepath: Path=INPUT_FILE.absolute(), map_size: tuple[int, int]=(101, 103)) -> int:
    robots = read_input(filepath)
    current_score = 0
    time = 0
    for i in range(10000):
        for robot in robots:
            robot.move(map_size)

        score = compute_neightbourood(robots)
        if score >= current_score:
            current_score = score
            time = i + 1
            print("Epoc: ", i)
            print("Score: ", current_score)
            map = print_map(robots, map_size, i)
            


    # For ten first highest scores print the map in files
    with open(f"maps_{time}.txt", "w") as f:
        for line in map:
            f.write("".join(line) + "\n")
    
    print("Part II solution: ", time)
    return


if __name__ == "__main__":
    pass


