def read_input(file_path):
    return open(file_path).read().strip()


if __name__ == "__main__":
    diskmap = read_input("input_2.txt")
    print("The disk map is: ", diskmap) 

    # Step 1: compute rthe blocks
    blocks = []
    id = 0
    nb_empty = 0
    for pos, value in enumerate(diskmap):
        if pos % 2 == 0:
            blocks += [str(id)] * int(value)
            id += 1
        else:
            blocks += ["."] * int(value)
            nb_empty += int(value)


    print(blocks)

    # Step 2: move the blocks
    sorted_blocks = []
    last_pos = len(blocks) - 1
    for i in range(len(blocks) - nb_empty):
        if blocks[i] != ".":
            sorted_blocks.append(blocks[i])
        else:
            while blocks[last_pos] == ".":
                last_pos -= 1
            sorted_blocks.append(blocks[last_pos])
            last_pos -= 1


    print(sorted_blocks[:100])
        
    # Step 3: compute the checksum
    checksum = 0
    for pos, value in enumerate(sorted_blocks):
        checksum += int(value) * pos

    print("The checksum is: ", checksum) 

    

