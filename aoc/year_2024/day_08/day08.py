from collections import defaultdict
from itertools import combinations


def read_map(filename):
    with open(filename) as f:
        return [[char for char in line.strip()] for line in f]


if __name__ == "__main__":
    map = read_map("map_day08v2.txt")
    map_size = (len(map), len(map[0]))
    antinode_map_positions = set()
    # Find all antennas
    antennas = defaultdict(list)
    for i, row in enumerate(map):
        for j, item in enumerate(row):
            if item != '.':
                antennas[item].append((i, j))

    for antenna_type, positions in antennas.items():
        print(f"Antenna {antenna_type} has {len(positions)} positions.")
        print("All pairs of positions:", list(combinations(positions, 2)))
        for pos1, pos2 in combinations(positions, 2):
            # Simplification de l'algorithme possible si pas de valeurs absolues : done
            delta_row = pos2[0] - pos1[0]
            delta_col = pos2[1] - pos1[1]
            # if pos1[0] <= pos2[0]:
            #     if pos1[1] <= pos2[1]:
            #         antinode_1_pos = (pos1[0] - delta_row, pos1[1] - delta_col)
            #         antinode_2_pos = (pos2[0] + delta_row, pos2[1] + delta_col)
            #     else:
            #         antinode_1_pos = (pos1[0] - delta_row, pos1[1] + delta_col)
            #         antinode_2_pos = (pos2[0] + delta_row, pos2[1] - delta_col)
            # else:
            #     if pos1[1] <= pos2[1]:
            #         antinode_1_pos = (pos1[0] + delta_row, pos1[1] - delta_col)
            #         antinode_2_pos = (pos2[0] - delta_row, pos2[1] + delta_col)
            #     else:
            #         antinode_1_pos = (pos1[0] + delta_row, pos1[1] + delta_col)
            #         antinode_2_pos = (pos2[0] - delta_row, pos2[1] - delta_col)
            antinode_1_pos = (pos1[0] - delta_row, pos1[1] - delta_col)
            antinode_2_pos = (pos2[0] + delta_row, pos2[1] + delta_col)

            # Print antenna type, position of antennas, and antinode positions
            print(f"Antenna {antenna_type} at positions {pos1} and {pos2} has antinode positions {antinode_1_pos} and {antinode_2_pos}.")
            if 0 <= antinode_1_pos[0] < map_size[0] and 0 <= antinode_1_pos[1] < map_size[1]:
                antinode_map_positions.add(antinode_1_pos)
            if 0 <= antinode_2_pos[0] < map_size[0] and 0 <= antinode_2_pos[1] < map_size[1]:
                antinode_map_positions.add(antinode_2_pos)

    print(antinode_map_positions)
    print(len(antinode_map_positions))



        

