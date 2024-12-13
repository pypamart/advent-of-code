#.__..  .._. __ .  .  .__..  ..__   .__ ._..__ .___..   ,   __..__..   .  ..___.._..__..  .
#|  ||  | | /  `|_/   [__]|\ ||  \  |  \ | [__)  |   \./   (__ |  ||   |  |  |   | |  ||\ |
#|__\|__|_|_\__.|  \  |  || \||__/  |__/_|_|  \  |    |    .__)|__||___|__|  |  _|_|__|| \|
 
 
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "resources" / "behaviors.txt"

def parse_machine_instruction(instructions: str) -> tuple:
    configuration = dict()
    instructions = instructions.split("\n")
    
    configuration["XA"] = int(instructions[0].split("X+")[1].split(",")[0])
    configuration["YA"] = int(instructions[0].split("Y+")[1])
    
    configuration["XB"] = int(instructions[1].split("X+")[1].split(",")[0])
    configuration["YB"] = int(instructions[1].split("Y+")[1])
    
    configuration["XP"] = int(instructions[2].split("X=")[1].split(",")[0])
    configuration["YP"] = int(instructions[2].split("Y=")[1])
    return configuration
    
def compute_solution(machine: dict) -> int:
    # Verify if a solution exists
    determinant = machine["XA"] * machine["YB"] - machine["XB"] * machine["YA"]
    if determinant == 0:
        return None
    # (yb*x-y*xb)/(xa*yb-xb*ya)
    n_a = machine["YB"] * machine["XP"] - machine["XB"] * machine["YP"]
    n_a /= determinant
    n_b = machine["XA"] * machine["YP"] - machine["YA"] * machine["XP"]
    n_b /= determinant
    return n_a, n_b

    
    

    

def solve(filepath: Path=INPUT_FILE.absolute()) -> int:
    with open(filepath) as f:
        lines = f.read()
    lines = lines.split("\n\n")
    
    machines = []
    for line in lines:
        machines.append(parse_machine_instruction(line))
        
    cost = 0
    cost_a = 3
    cost_b = 1
    for machine in machines:
        result = compute_solution(machine)
        # print(machine, result)
        if result is None:
            continue
        n_a, n_b = result
        if 0 <= n_a <= 100 and 0 <= n_b <= 100 and int(n_a) == n_a and int(n_b) == n_b:
            cost += int(n_a) * cost_a + int(n_b) * cost_b
            print(machine, result,n_a * cost_a + n_b * cost_b, cost)
                
    print("Part I solution: ", cost)
    return cost
    
    
