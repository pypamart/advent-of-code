from pathlib import Path
from collections import defaultdict
from aoc.year_2024.day_12.input_reader import read_map

INPUT_FILE = Path(__file__).parent / "resources" / "map.txt"

def solve(filepath: Path = INPUT_FILE.absolute()) -> int:
    map = read_map(filepath)
    areas = compute_areas(map)
    regions = group_coordinates_by_region(areas)
    total_cost = compute_total_cost(map, regions)
    print("The total cost is:", total_cost)
    return total_cost

def compute_areas(map):
    areas = {}
    nb_areas = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if j > 0 and map[i][j] == map[i][j - 1] and i > 0 and map[i][j] == map[i - 1][j]:
                if areas[(i, j - 1)] != areas[(i - 1, j)]:
                    merge_areas(areas, (i, j - 1), (i - 1, j))
                areas[(i, j)] = areas[(i, j - 1)]
            elif j > 0 and map[i][j] == map[i][j - 1]:
                areas[(i, j)] = areas[(i, j - 1)]
            elif i > 0 and map[i][j] == map[i - 1][j]:
                areas[(i, j)] = areas[(i - 1, j)]
            else:
                nb_areas += 1
                areas[(i, j)] = nb_areas

    return areas

def merge_areas(areas, area1, area2):
    for key, value in areas.items():
        if value == areas[area1]:
            areas[key] = areas[area2]

def group_coordinates_by_region(areas):
    regions = defaultdict(list)
    for coordinates, region_id in areas.items():
        regions[region_id].append(coordinates)
    print("The number of regions is:", len(regions))
    return regions

def compute_total_cost(map, regions):
    total_cost = 0
    for region_id, coordinates in regions.items():
        fences = compute_fences(map, coordinates)
        nb_sides = count_sides(fences)
        region_cost = nb_sides * len(coordinates)
        print(f"Region {region_id} has {nb_sides} sides and {len(coordinates)} cells: costs are {region_cost}")
        total_cost += region_cost
    return total_cost

def compute_fences(map, coordinates):
    fences = []
    for i, j in coordinates:
        if i == 0 or (i - 1, j) not in coordinates:
            fences.append([(i, j), "TOP"])
        if i == len(map) - 1 or (i + 1, j) not in coordinates:
            fences.append([(i, j), "BOTTOM"])
        if j == 0 or (i, j - 1) not in coordinates:
            fences.append([(i, j), "LEFT"])
        if j == len(map[0]) - 1 or (i, j + 1) not in coordinates:
            fences.append([(i, j), "RIGHT"])
    return fences

def count_sides(fences):
    current_fence = fences[0]
    visited_fences = [current_fence]
    nb_sides = 0

    while True:
        (i, j), current_orientation = current_fence

        if current_orientation == "TOP":
            current_fence = get_next_fence(fences, (i, j), "RIGHT", (i, j + 1), "TOP", (i - 1, j + 1), "LEFT")
        elif current_orientation == "RIGHT":
            current_fence = get_next_fence(fences, (i, j), "BOTTOM", (i + 1, j), "RIGHT", (i + 1, j + 1), "TOP")
        elif current_orientation == "BOTTOM":
            current_fence = get_next_fence(fences, (i, j), "LEFT", (i, j - 1), "BOTTOM", (i + 1, j - 1), "RIGHT")
        elif current_orientation == "LEFT":
            current_fence = get_next_fence(fences, (i, j), "TOP", (i - 1, j), "LEFT", (i - 1, j - 1), "BOTTOM")
        else:
            print("Error")

        if current_orientation != current_fence[1]:
            nb_sides += 1

        if current_fence not in fences:
            print("Error")
            break

        if current_fence not in visited_fences:
            visited_fences.append(current_fence)
        else:
            if len(visited_fences) < len(fences):
                current_fence = find_unvisited_fence(fences, visited_fences)
            else:
                if nb_sides % 2 == 1:
                    print("Error: nb_sides is odd")
                    nb_sides += 1
                break

    return nb_sides

def get_next_fence(fences, *args):
    for arg in args:
        if arg in fences:
            return arg
    return None

def find_unvisited_fence(fences, visited_fences):
    for fence in fences:
        if fence not in visited_fences:
            return fence
    return None
