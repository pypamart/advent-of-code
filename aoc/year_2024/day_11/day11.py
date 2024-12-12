
def blink(arrangement):
    new_arrangement = []
    for stone in arrangement:
        if stone == "0":
            new_arrangement.append("1")
        elif len(stone) % 2 == 0:
            pos = int(len(stone) / 2)
            new_arrangement.append(str(int(stone[:pos])))
            new_arrangement.append(str(int(stone[pos:])))
        else:
            new_arrangement.append(str(int(stone) * 2024)) 
    return new_arrangement


if __name__ == "__main__":
    arrangement = ["125", "17"]
    arrangement = ["64599",  "31", "674832", "2659361", "1", "0", "8867", "321"]
    print(" ".join(arrangement))
    for iteration in range(30):
        print("Iteration:", iteration)
        arrangement = blink(arrangement)
    
    print(" ".join(arrangement))
    print(len(arrangement))