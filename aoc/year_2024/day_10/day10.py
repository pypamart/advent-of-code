def read_map(filename):
    with open(filename) as f:
        return [[int(char) for char in line.strip()] for line in f]


def search_list_of_0(map):
    list_of_0 = []
    for i, row in enumerate(map):
        for j, item in enumerate(row):
            if item == 0:
                list_of_0.append((i, j))
    return list_of_0

def compute_score(map, i, j, visited_9, score=0):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    value = map[i][j]

    # PART I
    # if value == 9 and (i, j) not in visited_9:
    # PART II
    if value == 9: # and (i, j) not in visited_9:
        score += 1
        visited_9.append((i, j))
        # print(value, "+1")
    else:
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(map) and 0 <= nj < len(map[0]) and map[ni][nj] == value + 1:
                score = compute_score(map, ni, nj, visited_9, score)

    return score

if __name__ == "__main__":
    map = read_map("map2.txt")
    list_of_0 = search_list_of_0(map)
    print(map)

    total_score = 0
    for (i, j) in list_of_0:
        score = compute_score(map, i, j, [])
        print(f"0 at position ({i}, {j}) has a score of {score}.")
        total_score += score
        

    print(total_score)
