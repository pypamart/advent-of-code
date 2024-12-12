from calendar import c
from copy import deepcopy


def read_input(file_path):
    return open(file_path).read().strip()


if __name__ == "__main__":
    diskmap = read_input("input_2.txt")
    # print("The disk map is: ", diskmap) 

    # Step 1: compute the blocks
    blocks = []
    id = 0
    nb_empty = 0
    
    for pos, value in enumerate(diskmap):
        if pos % 2 == 0:
            item = str(id)
            id += 1
        else:
            item = "."
    
        blocks.append([item, int(value), True])    

    # print("".join([ str(value) * nb for value, nb, _ in blocks]))

    # Step 2: move the blocks
    # sorted_blocks = deepcopy(blocks)
    # is_finished = False
    # while not is_finished:
        













    # Il faudrait plutot un dictionnaire pour stocker les blocks selon leur taille en heap queue puis combler
    # A faire dans une v2, puis on comble les gap en fifo des espaces






    # Step 2: move the blocks
    last_pos = len(blocks) - 1
    is_finished = False
    current_sorted_block = deepcopy(blocks)
    counter = 1
    while True:
        # print("Iteration: ", counter)
        counter += 1
        # Find the last block
        previous_current_sorted_block = deepcopy(current_sorted_block)

        last_block = None
        last_pos = len(current_sorted_block) - 1
        while last_pos >= 0 and (last_block is None):
            if current_sorted_block[last_pos][0] != "." and current_sorted_block[last_pos][2]:
                last_block = current_sorted_block[last_pos]
                last_block_pos = last_pos
                # print(last_block)
            last_pos -= 1

        if last_block is None:
            break
        # Find the gap that allow to replace the block
        gap = None
        pos = 0
        while pos < len(current_sorted_block) and (gap is None):
            if current_sorted_block[pos][0] == "." and current_sorted_block[pos][1] >= last_block[1]:
                gap = current_sorted_block[pos]
                gap_pos = pos
            pos += 1
                
        # Replace the block
        if gap is not None and last_block is not None and gap_pos < last_block_pos: 
            current_sorted_block[last_block_pos] = [".", last_block[1], False]
            if last_block[1] == gap[1]:
                current_sorted_block[gap_pos] = [last_block[0], last_block[1], False]
            else:
                current_sorted_block = current_sorted_block[:gap_pos] + [[last_block[0], last_block[1], False]] + [[".", gap[1] - last_block[1], True]] + current_sorted_block[gap_pos + 1:]
        else:
            # print("No gap found")
            last_block[2] = False
            # break

        # print(current_sorted_block)
        #print("".join([ str(value) * nb for value, nb, _ in current_sorted_block]))
        # break
        if previous_current_sorted_block == current_sorted_block:
            break 

    # while not is_finished:
    #     sorted_blocks = []

    #     for i in range(len(current_sorted_block)):
    #         if current_sorted_block[i][0] != ".":
    #             sorted_blocks.append(current_sorted_block[i])
    #         else:
    #             max_size = current_sorted_block[i][1]
    #             is_block_matched = False
    #             pos = len(current_sorted_block) - 1
    #             while not is_block_matched:
    #                 if current_sorted_block[pos][0] != "." and current_sorted_block[pos][1] <= max_size and current_sorted_block[pos][2]:
    #                     is_block_matched = True
    #                     block_matched = current_sorted_block[pos]
    #                     block_matched_pos = pos
    #                     current_sorted_block[pos][2] = False

    #                     sorted_blocks.append(block_matched)
    #                     if block_matched[1] <= max_size:
    #                         sorted_blocks.append([".", max_size - current_sorted_block[pos][1], False])
                        
    #                 pos -= 1
    #                 if pos < 0:
    #                     break

    #             print("".join([ str(value) * nb for value, nb, _ in sorted_blocks]))
        
    #     if sorted_blocks == current_sorted_block:
    #         is_finished = True
    #     else: 
    #         current_sorted_block = deepcopy(sorted_blocks)
    #         for i in range(len(current_sorted_block)):
    #             current_sorted_block[i][2] = True

    #     # if current_sorted_block == sorted_blocks:
    #     #     is_finished = True
    #     # else:
    #     #     current_sorted_block = sorted_blocks
    #     # print([block for block in blocks if block[0] != "." and block[2]])
    #     # is_finished = True


    # # print(sorted_blocks)   
    with open("current_sorted_block.txt", "w") as f:
        for block in current_sorted_block:
            f.write(str(block) + "\n")

    # Checksum : voir checksum.py

    # # # Step 2.5
    # sorted_blocks = ":".join([value * nb for value, nb, _ in current_sorted_block])
    # print(sorted_blocks) 


    # # # Step 3: compute the checksum
    # checksum = 0
    # for pos, block in enumerate(current_sorted_block.split(":")):
    #     if value != ".":
    #         checksum += int(value) * pos

    # print("The checksum is: ", checksum) 

    

