from pathlib import Path
from collections import defaultdict

from aoc.year_2024.day_12.input_reader import read_map

INPUT_FILE = Path(__file__).parent / "resources" / "map.txt"

# Pour le nombre de côtés, il existe une formule mathématique qui permet de calculer le nombre de côtés d'une région en fonction du nombre de cellules et du nombre de côtés de la région.
# Pour une région de n cellules, c'est 4 * n - s où s est le nombre de côtés adjacents.

# Les autres ont fait un Flood Fill https://en.wikipedia.org/wiki/Flood_fill

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
    
    print("The number of regions is:", len(regions))
    
    total_cost = 0
    for region_id, coordinates in regions.items():
        fences = []
        for i, j in coordinates:
            if i == 0 or ((i - 1, j) not in coordinates):
                fences.append([(i, j), "TOP"])
            
            if i == len(map) - 1 or ((i + 1, j) not in coordinates):
                fences.append([(i, j), "BOTTOM"])
            
            if j == 0 or ((i, j - 1) not in coordinates):
                fences.append([(i, j), "LEFT"])
            
            if j == len(map[0]) - 1 or ((i, j + 1) not in coordinates):
                fences.append([(i, j), "RIGHT"])
                
        # Walk throught all the fences, and connect them to compute sides
        current_fence = fences[0]
        visited_fences = []
        visited_fences.append(current_fence)
        nb_sides = 1
                
        while True:
            # print("Current fence:", current_fence)
            tmp_fence = current_fence
            (i, j), current_orientation = current_fence
             
            if current_orientation == "TOP":
                if [(i, j), "RIGHT"] in fences:
                    # nb_sides += 1
                    current_fence = [(i, j), "RIGHT"]
                    
                elif [(i, j + 1), "TOP"] in fences:
                    current_fence = [(i, j + 1), "TOP"]
                    
                elif [(i - 1, j + 1), "LEFT"] in fences:
                    # nb_sides += 1
                    current_fence = [(i - 1, j + 1), "LEFT"]
                    
            elif current_orientation == "RIGHT":
                if [(i, j), "BOTTOM"] in fences:
                    # nb_sides += 1
                    current_fence = [(i, j), "BOTTOM"]
                    
                elif [(i + 1, j), "RIGHT"] in fences:
                    current_fence = [(i + 1, j), "RIGHT"]
                    
                elif [(i + 1, j + 1), "TOP"] in fences:
                    # nb_sides += 1
                    current_fence = [(i + 1, j + 1), "TOP"]
                    
            elif current_orientation == "BOTTOM":
                if [(i, j), "LEFT"] in fences:
                    # nb_sides += 1
                    current_fence = [(i, j), "LEFT"]
                    
                elif [(i, j - 1), "BOTTOM"] in fences:
                    current_fence = [(i, j - 1), "BOTTOM"]
                    
                elif [(i + 1, j - 1), "RIGHT"] in fences:
                    # nb_sides += 1
                    current_fence = [(i + 1, j - 1), "RIGHT"]
                    
            elif current_orientation == "LEFT":
                if [(i, j), "TOP"] in fences:
                    # nb_sides += 1
                    current_fence = [(i, j), "TOP"]
                    
                elif [(i - 1, j), "LEFT"] in fences:
                    current_fence = [(i - 1, j), "LEFT"]
                    
                elif [(i - 1, j - 1), "BOTTOM"] in fences:
                    # nb_sides += 1
                    current_fence = [(i - 1, j - 1), "BOTTOM"]
            else:
                print("Error")
            
            if region_id == 1:
                print(tmp_fence, "=>", current_fence)
                
            if current_orientation != current_fence[1] and current_fence not in visited_fences:
                nb_sides += 1
                print("New side")
            elif current_orientation == current_fence[1] and current_fence in visited_fences:
                # Loop found
                nb_sides -= 1
            # print((i, j), current_orientation, "=>", current_fence)
            
            if current_fence not in fences:
                print("Error")
                break
            
            if current_fence not in visited_fences:
                visited_fences.append(current_fence)
                # print("Visited fence:", visited_fences)
            else:
                if len(visited_fences) < len(fences):
                    # print("All fences have not been visited, searching for a new one...")
                    for fence in fences:
                        if fence not in visited_fences:
                            current_fence = fence
                            print("CHANGE and NEW SIDE")
                            visited_fences.append(current_fence)
                            nb_sides += 1
                            break

                else:
                    # print("All fences have been visited",  len(fences))
                    # if nb_sides % 2 == 1:
                    #     print("Error: nb_sides is odd")
                    #     nb_sides += 1
                    # print(visited_fences)
                    break
  
        
  
    
        print(f"Region {region_id} has {nb_sides} sides and {len(coordinates)} cells : costs are {nb_sides * len(coordinates)}")
        total_cost += nb_sides * len(coordinates)
                 
    print("The total cost is:", total_cost)

    return total_cost
