
def count_blink(stone, nb_gen, current_gen=0):
    counter = 0
    if nb_gen == current_gen:
        return 1
    
    if stone =="0":
        counter += count_blink("1", nb_gen, current_gen + 1)
    elif len(stone) % 2 == 0:
        pos = int(len(stone) / 2)
        counter += count_blink(str(int(stone[:pos])), nb_gen, current_gen + 1)
        counter += count_blink(str(int(stone[pos:])), nb_gen, current_gen + 1)
    else:
        counter += count_blink(str(int(stone) * 2024), nb_gen, current_gen + 1) 
        
    return counter


if __name__ == "__main__":
    initial_arrangement = ["125", "17"]
    # initial_arrangement = ["64599",  "31", "674832", "2659361", "1", "0", "8867", "321"]
    counter = 0
    nb_gen = 25
    save_step = 5
    for i, stone in enumerate(initial_arrangement):
        print("Stone", i + 1, "/", len(initial_arrangement))
        nb_children = count_blink(stone, nb_gen)
        counter += nb_children
        print("For this stones ", nb_gen, " generates ", nb_children, " stones.")
        

    print("Sum of all stones is ", counter)