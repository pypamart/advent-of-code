

if __name__ == "__main__":
    with open("current_sorted_block_p2.txt") as f:
        data = f.readlines()

    pos = 0
    checksum = 0
    for line in data:
        value = line.split("'")[1]
        occurence = int(line.split(",")[1])
        for i in range(occurence):
            if value != ".":
                # print(pos, int(value))
                checksum += int(value) * pos
            pos += 1

    print(checksum)