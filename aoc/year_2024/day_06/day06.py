class Map:
    def __init__(self, map_matrix):
        self.__matrix = map_matrix
        self.__size = (len(map_matrix), len(map_matrix[0]))

    @property
    def size(self):
        return self.__size

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            return cls([[char for char in line.strip()] for line in f])

    def find_initial_guard_position(self):
        for row, line in enumerate(self.__matrix):
            if "^" in line:
                return row, line.index("^"), "UP"
            elif "v" in line:
                return row, line.index("v"), "DOWN"
            elif "<" in line:
                return row, line.index("<"), "LEFT"
            elif ">" in line:
                return row, line.index(">"), "RIGHT"
        return None
    
    def get_type_at(self, row, col):
        if row < 0 or col < 0 or row >= len(self.__matrix) or col >= len(self.__matrix[0]):
            return "OUTSIDE"
        elif self.__matrix[row][col] == "#":
            return "OBSTACLE"
        elif self.__matrix[row][col] == "^":
            return "GUARD"
        else:
            return "EMPTY"

    def add_obstacle_at(self, row, col):
        self.__matrix[row][col] = "#"

    def remove_obstacle_at(self, row, col):
        self.__matrix[row][col] = "."

class Guard:
    def __init__(self, initial_row, initial_col, initial_direction):
        self.__row_pos = initial_row
        self.__col_pos = initial_col
        self.__direction = initial_direction
        self.__visited_cells = set()
        self.__visited_cells.add((initial_row, initial_col, initial_direction))
        self.__walk_in_a_loop = False
        self.__is_out_of_map = False

    @property
    def is_out_of_map(self):
        return self.__is_out_of_map
    
    @property
    def walk_in_a_loop(self):
        return self.__walk_in_a_loop

    def __change_direction(self):
        if self.__direction == "UP":
            self.__direction = "RIGHT"
        elif self.__direction == "RIGHT":
            self.__direction = "DOWN"
        elif self.__direction == "DOWN":
            self.__direction = "LEFT"
        elif self.__direction == "LEFT":
            self.__direction = "UP"

    def move_one_step(self, map):
        if self.__direction == "UP":
            next_cell_row,  next_cell_col = (self.__row_pos - 1, self.__col_pos)
        elif self.__direction == "DOWN":
            next_cell_row,  next_cell_col = (self.__row_pos + 1, self.__col_pos)
        elif self.__direction == "LEFT":
            next_cell_row,  next_cell_col = (self.__row_pos, self.__col_pos - 1)
        elif self.__direction == "RIGHT":
            next_cell_row,  next_cell_col = (self.__row_pos, self.__col_pos + 1)

        next_cell_type = map.get_type_at(next_cell_row, next_cell_col)

        if next_cell_type == "OBSTACLE":
            self.__change_direction()
        elif next_cell_type == "OUTSIDE":
            # print("OUTSIDE")
            self.__is_out_of_map = True
        else:
            self.__row_pos = next_cell_row
            self.__col_pos = next_cell_col
            
            if (self.__row_pos, self.__col_pos, self.__direction) in self.__visited_cells:
                # print("LOOP")
                self.__walk_in_a_loop = True
            else:
                self.__visited_cells.add((self.__row_pos, self.__col_pos, self.__direction))

    def count_visited_cells(self):
        return len(set([(row, col) for row, col, _ in self.__visited_cells]))

if __name__ == "__main__":
    # Part I
    map = Map.from_file("map2.txt")
    guard = Guard(*map.find_initial_guard_position())
    while not guard.is_out_of_map and not guard.walk_in_a_loop:
        guard.move_one_step(map)

    print(guard.count_visited_cells())


    # Part II
    count_loop = 0
    nb_row, nb_col = map.size
    for row in range(nb_row):
        for col in range(nb_col):
            if map.get_type_at(row, col) == "EMPTY":
                map.add_obstacle_at(row, col)
                guard = Guard(*map.find_initial_guard_position()) 

                while (not guard.is_out_of_map) and (not guard.walk_in_a_loop):
                    guard.move_one_step(map)

                map.remove_obstacle_at(row, col)
                if guard.walk_in_a_loop:
                    count_loop += 1
    
    print( count_loop)