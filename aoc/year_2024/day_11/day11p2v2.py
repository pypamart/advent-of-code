import json

# Plus propre avec un mécanisme demémoïzation ?
# A voir que le nombre max ne peut pas dépasser le plus grand nombre

def count_blink(stone, nb_gen, current_gen=0, cache=None):
    if cache is None:
        cache = {}

    # Create a unique key for the current state
    key = (stone, current_gen)

    # Check if the result is already in the cache
    if key in cache:
        return cache[key]

    counter = 0
    if nb_gen == current_gen:
        return 1

    if stone == "0":
        counter += count_blink("1", nb_gen, current_gen + 1, cache)
    elif len(stone) % 2 == 0:
        pos = int(len(stone) / 2)
        counter += count_blink(str(int(stone[:pos])), nb_gen, current_gen + 1, cache)
        counter += count_blink(str(int(stone[pos:])), nb_gen, current_gen + 1, cache)
    else:
        counter += count_blink(str(int(stone) * 2024), nb_gen, current_gen + 1, cache)

    # Store the result in the cache
    cache[key] = counter

    return counter


if __name__ == "__main__":
    # initial_arrangement = ["125", "17"]
    initial_arrangement = ["64599",  "31", "674832", "2659361", "1", "0", "8867", "321"]
    counter = 0
    nb_gen = 75
    save_step = 5
    cache = {}
    for i, stone in enumerate(initial_arrangement):
        print("Stone", i + 1, "/", len(initial_arrangement))
        nb_children = count_blink(stone, nb_gen, 0, cache)
        counter += nb_children
        print("For this stones ", nb_gen, " generates ", nb_children, " stones.")
        

    print("Sum of all stones is ", counter)
    
    with open('cache.txt', 'w') as f:
        for key, value in cache.items():
            print(f"{key}: {value}", file=f)  
    