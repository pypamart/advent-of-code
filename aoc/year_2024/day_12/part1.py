from pathlib import Path
from collections import defaultdict

from aoc.year_2024.day_12.input_reader import read_map

INPUT_FILE = Path(__file__).parent / "resources" / "map.txt"


def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    map = read_map(filepath)
    areas = {}
    nb_areas = 0
    
    # Compute each region
    for i in range(len(map)):
        for j in range(len(map[0])):
            if j > 0 and map[i][j] == map[i][j-1] and i > 0 and map[i][j] == map[i-1][j]:
                # Check if the two regions are different
                if areas[(i, j-1)] != areas[(i-1, j)]:
                    print("Merging 2 areas...")
                    # Merge the two regions
                    for key, value in areas.items():
                        if value == areas[(i, j-1)]:
                            areas[key] = areas[(i-1, j)]
                areas[(i, j)] = areas[(i, j-1)]           
            elif j > 0 and map[i][j] == map[i][j-1]:
                areas[(i, j)] = areas[(i, j-1)]
            elif i > 0 and map[i][j] == map[i-1][j]:
                areas[(i, j)] = areas[(i-1, j)]
            else:
                nb_areas += 1
                areas[(i, j)] = nb_areas

    # For each region, compute the number of limits
    regions = defaultdict(list)
    for coordinates, region_id in areas.items():
        regions[region_id].append(coordinates)
    
    # print("The number of regions is:", len(regions))
    
    total_cost = 0
    for region_id, coordinates in regions.items():
        nb_fences = 0
        for i, j in coordinates:
            if i == 0 or (i - 1, j) not in coordinates:
                nb_fences += 1
            if i == len(map) - 1 or (i + 1, j) not in coordinates:
                nb_fences += 1
            if j == 0 or (i, j - 1) not in coordinates:
                nb_fences += 1
            if j == len(map[0]) - 1 or (i, j + 1) not in coordinates:
                nb_fences += 1
        
        # print(f"Region {region_id} has {nb_fences} fences and {len(coordinates)} cells : costs are {nb_fences * len(coordinates)}")
        total_cost += nb_fences * len(coordinates)
                 
    print("The total cost is:", total_cost)

    return total_cost
