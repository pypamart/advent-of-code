from collections import defaultdict
from itertools import combinations
from copy import deepcopy


def read_map(filename):
    with open(filename) as f:
        return [[char for char in line.strip()] for line in f]


if __name__ == "__main__":
    map = read_map("map_day08v2.txt")
    # map = read_map("map_day08.txt")
    map_size = (len(map), len(map[0]))
    antinode_map_positions = set()
    # Find all antennas
    antennas = defaultdict(list)
    nb_antennas = 0
    for i, row in enumerate(map):
        for j, item in enumerate(row):
            if item != '.':
                antennas[item].append((i, j))
                nb_antennas += 1

    for antenna_type, positions in antennas.items():
        print(f"Antenna {antenna_type} has {len(positions)} positions.")
        print("All pairs of positions:", list(combinations(positions, 2)))
        for pos1, pos2 in combinations(positions, 2):
            # Simplification de l'algorithme possible si pas de valeurs absolues : done
            delta_row = pos2[0] - pos1[0]
            delta_col = pos2[1] - pos1[1]

            is_antinode_1_out = False
            is_antinode_2_out = False
            counter = 0
            while not (is_antinode_1_out and is_antinode_2_out):
                counter += 1
                antinode_1_pos = (pos1[0] - counter*delta_row, pos1[1] - counter*delta_col)
                antinode_2_pos = (pos2[0] + counter*delta_row, pos2[1] + counter*delta_col)

                if 0 <= antinode_1_pos[0] < map_size[0] and 0 <= antinode_1_pos[1] < map_size[1]:
                    antinode_map_positions.add(antinode_1_pos)
                else:
                    is_antinode_1_out = True

                if 0 <= antinode_2_pos[0] < map_size[0] and 0 <= antinode_2_pos[1] < map_size[1]:
                    antinode_map_positions.add(antinode_2_pos)
                else:
                    is_antinode_2_out = True

    final_map = deepcopy(map)
    for pos1, pos2 in antinode_map_positions:
        if final_map[pos1][pos2] == ".":
            final_map[pos1][pos2] = "#"

    # Print the final map
    for row in final_map:
        print("".join(row))

    counter = 0
    # Count the number of character different from '.'
    for row in final_map:
        for char in row:
            if char != ".":
                counter += 1
    

    # print(antinode_map_positions)
    # print(len(antinode_map_positions))
    print(counter)