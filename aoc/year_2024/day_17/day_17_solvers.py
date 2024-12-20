LOG = set()
 
class ProgramRunner:
    def __init__(self, register_a: int, register_b: int, register_c: int):
        self.__register_a = register_a
        self.__register_b = register_b
        self.__register_c = register_c
        self.__program = []
        self.__instruction_pointer = 0
        self.__output = []
       
    def dump_registry(self):
        return self.__register_a, self.__register_b, self.__register_c
   
    def dump_output(self):
        return self.__output  
 
    def load_program(self, program: list[int]):
        self.__program = program
       
    def execute(self):
        while True:
            if self.__instruction_pointer >= len(self.__program):
                break
            LOG.add(self.__program[self.__instruction_pointer])
            self.execute_instruction()
           
    def execute_instruction(self):
        opcode = self.__program[self.__instruction_pointer]
        operand = self.__program[self.__instruction_pointer + 1]
        if opcode == 0:
            self.__adv(operand)
        elif opcode == 1:
            self.__blx(operand)
        elif opcode == 2:
            self.__bst(operand)
        elif opcode == 3:
            self.__jnz(operand)
        elif opcode == 4:
            self.__bxc(operand)
        elif opcode == 5:
            self.__out(operand)
        elif opcode == 6:
            self.__bdv(operand)
        elif opcode == 7:
            self.__cdv(operand)
        else:
            raise ValueError("Invalid opcode")
       
    def __get_combo_value(self, operand: int) -> int:
        if operand == 4:
            return self.__register_a
        elif operand == 5:
            return self.__register_b
        elif operand == 6:
            return self.__register_c
        else:
            return operand
       
   
    def __adv(self, operand: int):
        """The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register."""  
        value = self.__get_combo_value(operand)
        self.__register_a //= (2 ** value)
        self.__instruction_pointer += 2
       
    def __blx(self, operand: int):
        """The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B."""
        self.__register_b ^= operand
        self.__instruction_pointer += 2
         
    def __bst(self, operand: int):
        """The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register."""
 
        if operand == 4:
            self.__register_b = self.__register_a % 8
        elif operand == 5:
            self.__register_b = self.__register_b % 8
        elif operand == 6:
            self.__register_b = self.__register_c % 8
        else:
            self.__register_b = operand % 8
        self.__instruction_pointer += 2
       
    def __jnz(self, operand: int):
        """The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction."""
        # print("JUMP!")
        if self.__register_a != 0:
            self.__instruction_pointer = operand
        else:
            self.__instruction_pointer += 2
 

    def __bxc(self, operand: int):
        """The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)"""
        self.__register_b ^= self.__register_c
        self.__instruction_pointer += 2
   
    def __out(self, operand: int):
        """The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)"""
        if operand == 4:
            self.__output.append(self.__register_a % 8)
            # print("OUTPUT! A", self.__register_a % 8)
        elif operand == 5:
            self.__output.append(self.__register_b % 8)
            # print("OUTPUT! B", self.__register_b % 8)
        elif operand == 6:
            self.__output.append(self.__register_c % 8)
            # print("OUTPUT! C", self.__register_c % 8)
        else:
            self.__output.append(operand % 8)
            # print("OUTPUT!", operand % 8)
        self.__instruction_pointer += 2
       
    def __bdv(self, operand: int):
        """The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)"""
        value = self.__get_combo_value(operand)
        self.__register_b = self.__register_a // (2 ** value)
        self.__instruction_pointer += 2
       
    def __cdv(self, operand: int):
        """The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)"""
        value = self.__get_combo_value(operand)
        self.__register_c = self.__register_a // (2 ** value)
        self.__instruction_pointer += 2
 
def solve_part_1(register_a: int, register_b: int, register_c: int, program: list[int]) -> int:
   
         
    return
 
if __name__ == "__main__":
    # runner = ProgramRunner(0, 0, 9)
    # runner.load_program([2, 6])
    # runner.execute()
    # register_a, register_b, register_c = runner.dump_registry()
    # assert register_b == 1
   
    # runner = ProgramRunner(10, 0, 0)
    # runner.load_program([5,0,5,1,5,4])
    # runner.execute()
    # output = runner.dump_output()
    # assert output == [0, 1, 2]
   
    # runner = ProgramRunner(2024, 0, 0)
    # runner.load_program([0,1,5,4,3,0])
    # runner.execute()
    # output = runner.dump_output()
    # register_a, register_b, register_c = runner.dump_registry()
    # assert output == [4,2,5,6,7,7,7,7,3,1,0]
    # assert register_a == 0
   
    # runner = ProgramRunner(0, 29, 0)
    # runner.load_program([1, 7])
    # runner.execute()
    # register_a, register_b, register_c = runner.dump_registry()
    # assert register_b == 26
   
    # runner = ProgramRunner(0, 2024, 43690)
    # runner.load_program([4, 0])
    # runner.execute()
    # register_a, register_b, register_c = runner.dump_registry()
    # assert register_b == 44354
   
    # runner = ProgramRunner(729, 0, 0)
    # runner.load_program([0,1,5,4,3,0])
    # runner.execute()
    # output = runner.dump_output()
    # assert output == [4,6,3,5,6,3,5,2,1,0]
 
    # runner = ProgramRunner(37293246, 0, 0)
    # runner.load_program([2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0])
    # runner.execute()
    # output = runner.dump_output()
    # print("Part 1: ", ",".join(map(str, output)))
       
    # Part II               
    def binary_string_to_int(binary_str: str) -> int:
        return sum(int(bit) * (2 ** pos) for pos, bit in enumerate(reversed(binary_str)))
   
   
    def base_n_string_to_int(n, binary_str: str) -> int:
        return sum(int(bit) * (n ** pos) for pos, bit in enumerate(reversed(binary_str)))
   
    
    def find_candidates(program: list[int], pattern, bin_value: str) -> list[str]:
        candidates = []
        for suffix in ["000", "001", "010", "011", "100", "101", "110", "111"]:
        # for suffix in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            value = binary_string_to_int(bin_value + suffix)
            # value = base_n_string_to_int(8, bin_value + suffix)
            runner = ProgramRunner(value, 0, 0)
            runner.load_program(program)
            runner.execute()
            output = runner.dump_output()
            # print(output, pattern)
            if output == pattern:
                candidates.append(suffix)
        return candidates
    
    bin_value = [""]    
    program =  [2,4,1,6,7,5,4,4,1,7,0,3,5,5,3,0]
    # program = [0,3,5,4,3,0]
    
    for i in range(1, len(program) + 1):
        bin_value_new = []
        print("Search candidates for",  program[-i:])
        for value in bin_value:
            candidates = find_candidates(program, program[-i:], value)
            for candidate in candidates:
                bin_value_new.append(value + candidate)
        bin_value = [*bin_value_new]
        
        int_values = [binary_string_to_int(value) for value in bin_value]
        # int_values = [base_n_string_to_int(8, value) for value in bin_value]
        print("\n".join(map(str,int_values)))